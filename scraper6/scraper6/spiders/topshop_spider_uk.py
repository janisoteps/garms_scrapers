import scrapy
from scrapy.selector import Selector
from scraper6.items import TopshopItem
import hashlib
import re
import requests
import json
import datetime


class TopshopSpider(scrapy.Spider):
    name = "topshop_spider_uk"

    # The main start function which initializes the scraping URLs and triggers parse function
    def start_requests(self):
        urls = [
            'http://www.topshop.com/?geoip=home'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.link_collection)

    # Go through the top menu in initial response to collect links of each category
    def link_collection(self, response):
        links = Selector(response).xpath('.//li[contains(@class, "category")]/a')

        for link in links:
            cat_url = link.xpath("./@href").extract_first()
            if len(cat_url.split('topshop.com')) != 2:
                cat_url = f'http://www.topshop.com{cat_url}'
            print(f'Cat URL: {cat_url}')
            cat_name = link.xpath('./text()').extract_first()
            print(f'Cat name: {cat_name}')

            print(f'Category URL: {cat_url}')
            yield scrapy.Request(
                url=cat_url,
                callback=self.infinite_request,
                meta={
                    'cat_name': cat_name
                }
            )

    # Topshop has infinite scrolling, so we need to simulate ajax call to server requesting product data for scrolling
    # From ajax response then extract each product URL and trigger a scraping request
    def infinite_request(self, response):
        ajax_url_1 = 'http://www.topshop.com/webapp/wcs/stores/servlet/CatalogNavigationAjaxSearchResultCmd'
        cat_name = response.meta['cat_name']

        def gen_url_string(offset, input_string):
            split_cat = input_string.split('Nrpp=', 1)
            part_2 = split_cat[1].split('&siteId=', 1)
            url_string = f'{split_cat[0]}Nrpp={offset}&siteId={part_2[1]}'
            return url_string

        STORE_ID_SELECTOR = './/li[@id = "header_welcome"]/a/@href'
        store_id_match = response.xpath(STORE_ID_SELECTOR).re('storeId=[0-9]{5}')
        print(response.xpath(STORE_ID_SELECTOR).extract_first())
        if len(store_id_match) > 0:
            store_id = str(store_id_match[0])
        else:
            store_id = '12556'
        print(f'Store id: {store_id}')

        if store_id is not None:
            catalog_id = str(response.xpath(STORE_ID_SELECTOR).re('catalogId=[0-9]{5}')[0])
            if catalog_id is None:
                catalog_id = '33057'
            print('catalog id: ' + catalog_id)

            ajax_url_2 = '?' + store_id + '&' + catalog_id + '&langId=-1&dimSelected='

            CATEGORY_NAME_SELECTOR = './/select[@name = "sort-field"]/option[@selected = "selected"]/@value'
            category_name = response.xpath(CATEGORY_NAME_SELECTOR).extract_first()

            # Some matches will not have any products on them as outdated links
            if isinstance(category_name, str):
                # ajax_url_3 = category_name[0:-45]

                ajax_url_3 = category_name
                print('category name: ' + ajax_url_3)

                ajax_url = ajax_url_1 + ajax_url_2 + ajax_url_3
                print('AJAX call URL: ' + ajax_url)

                ajax_req = requests.get(ajax_url)
                json_dict = json.loads(ajax_req.text)

                record_count = json_dict['results']['contents'][0]['totalNumRecs']
                ajax_full_url = f'{ajax_url_1}{ajax_url_2}{gen_url_string(record_count, category_name)}'
                ajax_full_req = requests.get(ajax_full_url)
                json_full_dict = json.loads(ajax_full_req.text)

                results = json_full_dict['results']
                contents = results['contents'][0]
                records = contents['records']

                for record in records:
                    product_url = f'http://eu.topshop.com/{record["productUrl"]}'
                    name = record['name']
                    try:
                        colour_string = record['colour']
                    except:
                        colour_string = None

                    now_price = record['nowPrice']
                    try:
                        description = record['longDescription']
                    except:
                        description = None

                    print('Product URL: ' + product_url)
                    yield scrapy.Request(
                        url=product_url,
                        callback=self.parse,
                        meta={
                            'cat_name': cat_name,
                            'name': name,
                            'colour_string': colour_string,
                            'now_price': now_price,
                            'description': description
                        }
                    )

    def parse(self, response):

        # Write out xpath and css selectors for all fields to be retrieved
        item = TopshopItem()
        # NAME_SELECTOR = './/div[contains(@class, "product_details")]/h1/text()'
        # PRICE_SELECTOR = 'normalize-space(.//span[@class = "product_price"]/text())'
        IMAGE_SELECTOR = './/ul[contains(@class, "product_hero__wrapper")]/li/a/img/@src'
        SALE_WASPRICE_SELECTOR = './/div[@class = "product_prices"]/span[1]/text()'
        SALE_PRICE_SELECTOR = './/div[@class = "product_prices"]/span[3]/text()'
        SIZES_SELECTOR = './/select[@class="product_size"]/option[contains(@class, "stock")]/@value'
        STOCK_SELECTOR = './/select[@class="product_size"]/option/@class'

        # Assemble the item object which will be passed then to pipeline
        item['shop'] = 'Top Shop'
        item['name'] = response.meta['name']
        item['price'] = response.meta['now_price']

        if item['price'] == ['']:
            item['price'] = (response.xpath(SALE_WASPRICE_SELECTOR)).re('[.0-9]+')

        item['prod_url'] = response.url
        item['image_urls'] = response.xpath(IMAGE_SELECTOR).extract()
        saleprice_match = response.xpath(SALE_PRICE_SELECTOR)
        if saleprice_match is not None:
            saleprice_match_re = saleprice_match.re('[.0-9]+')
        else:
            saleprice_match_re = None
        print(f'saleprice match: {saleprice_match_re}')
        if len(saleprice_match_re) > 0:
            item['saleprice'] = float('.'.join(saleprice_match_re))
        else:
            item['saleprice'] = None
        print(f'saleprice: {item["saleprice"]}')

        brand_regex = re.search('_BRANDS_22:\"(.*)\",ECMC_PROD_FIT', response.text)
        if brand_regex is not None:
            item['brand'] = brand_regex.group(1)

        currency_regex = re.search('currency\": \"(.*?)\"', response.text)
        if currency_regex is not None:
            item['currency'] = currency_regex.group(1)

        # Check if page is sales or not, add boolean value of result
        m = re.search('sale', response.url)

        if m:
            item['sale'] = True
        else:
            item['sale'] = False

        # Top Shop has only women fashion
        item['sex'] = 'women'
        item['date'] = int(datetime.datetime.now().timestamp())
        item['description'] = response.meta['description']
        item['color_string'] = response.meta['colour_string']
        item['category'] = response.meta['cat_name']

        sizes_match = response.xpath(SIZES_SELECTOR).extract()
        if len(sizes_match) == 0:
            sizes_match = response.xpath('.//input[@name = "attrValue"]/@value').extract()
        print('sizes match')
        print(sizes_match)
        sizes = [{'size': x} for x in sizes_match if sizes_match.index(x) != 0 or x.isdigit()]
        print(f'sizes:')
        print(sizes)
        sizes_stock_match = response.xpath(STOCK_SELECTOR).extract()
        if len(sizes_stock_match) == 0:
            sizes_stock_match = response.xpath('.//input[@name = "attrValue"]/@title').extract()
        print(f'sizes stock match')
        print(sizes_stock_match)
        sizes_stock = [
            {
                'stock': el_class,
                'size': sizes[sizes_stock_match.index(el_class)]['size']
            } for el_class in sizes_stock_match
        ]
        print('SIZES STOCK:')
        print(sizes_stock)
        item['size_stock'] = sizes_stock

        # Calculate SHA1 hash of image URL to make it easy to find the image based on hash entry and vice versa
        # Add the hash to item
        img_strings = item['image_urls']

        item['image_hash'] = []

        for img_string in img_strings:
            # Check if image string is a string, if not then do not pass this item
            if isinstance(img_string, str):
                # print(img_string)
                hash_object = hashlib.sha1(img_string.encode('utf8'))
                hex_dig = hash_object.hexdigest()
                item['image_hash'].append(hex_dig)

        yield item
