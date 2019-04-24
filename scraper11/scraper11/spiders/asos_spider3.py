import scrapy
from scraper11.scraper11.items import AsosItem
import hashlib
import re
import requests
import json


class AsosSpider(scrapy.Spider):
    name = "asos_spider"

    # The main start function which initializes the scraping URLs and triggers parse function
    def start_requests(self):
        urls = [
            'http://www.asos.com/women/'
        ]

        for url in urls:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
            yield scrapy.Request(url=url, headers=headers, callback=self.link_collection)


    # Go through the top menu in initial response to collect links of each category
    def link_collection(self, response):
        # cat_urls = Selector(response).xpath('.//a[@data-testid = "text-link"]')
        cat_urls = response.xpath('.//a[@data-testid = "text-link"]/@href').extract()
        counter = 0
        for cat_url in cat_urls:
            counter += 1

        for cat_url in cat_urls:
            cat_url_string = str(cat_url)
            print('category URL: ', cat_url_string)
            try:
                cat_id = (re.search('cid=.[0-9]+', str(cat_url_string))[0])
                cat_id = re.search('[0-9]+', cat_id)[0]
            except:
                cat_id = None

            if cat_id is not None:
                STORE_DATA_SELECTOR = './/a[@data-testid = "accountIcon"]/@href'
                store_data_version = re.search('(?<=keyStoreDataversion=).{8,12}(?=\&)', response.text)[0]
                # store_data_version = (re.search('=.*', store_data_version_str))[0][1:]

                print('Category ID: ' + cat_id)
                print('Store Data Version: ' + store_data_version)
                print('Category Count: ', str(counter))
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

                yield scrapy.Request(
                    url=cat_url_string,
                    headers=headers,
                    callback=self.infinite_request,
                    meta={
                        'cat_id': cat_id,
                        'store_data_version': store_data_version,
                        'cat_url_count': counter
                    }
                )


    # Asos has infinite scrolling, so we need to simulate ajax call to server requesting product data for scrolling
    # From ajax response then extract each product URL and trigger a scraping request
    def infinite_request(self, response):
        cat_id = response.meta['cat_id']
        store_data_version = response.meta['store_data_version']

        ajax_url_1 = 'https://api.asos.com/product/search/v1/categories/' + str(cat_id)

        ajax_url_2 = '?channel=desktop-web&country=GB&currency=GBP&keyStoreDataversion=' + str(store_data_version)

        ajax_url_3 = '&lang=en&limit=72&offset=0&rowlength=4&store=1'

        ajax_url = ajax_url_1 + ajax_url_2 + ajax_url_3
        ajax_req = requests.get(ajax_url)
        json_dict = json.loads(ajax_req.text)
        item_count = json_dict['itemCount']
        page_count = int(item_count / 72)

        for i in range(0, page_count, 1):
            ajax_url_3_pag = '&lang=en&limit=72&offset=' + str(i*72) + '&rowlength=4&store=1'
            ajax_url_pag = ajax_url_1 + ajax_url_2 + ajax_url_3_pag
            ajax_pag_req = requests.get(ajax_url_pag)
            pag_json_dict = json.loads(ajax_pag_req.text)
            products_list = pag_json_dict['products']

            for product in products_list:
                name = product['name']
                currency = product['price']['current']['text'][0]
                is_sale = product['price']['isMarkedDown']
                if is_sale is True:
                    price = product['price']['previous']['value']
                    price_sale = product['price']['current']['value']
                else:
                    price = product['price']['current']['value']
                    price_sale = ''
                brand = product['brandName']
                color = product['colour']
                product_url = 'http://www.asos.com/' + product['url']
                cat_name = pag_json_dict['categoryName']
                print('Product URL: ' + product_url)
                headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

                yield scrapy.Request(
                    url=product_url,
                    headers=headers,
                    callback=self.parse,
                    meta={
                        'name': name,
                        'currency': currency,
                        'is_sale': is_sale,
                        'price': price,
                        'price_sale': price_sale,
                        'brand': brand,
                        'color': color,
                        'cat_name': cat_name,
                        'cat_url_count': response.meta['cat_url_count']
                    }
                )

    # Scrape the product page
    def parse(self, response):
        item = AsosItem()

        item['shop'] = 'Asos'
        item['name'] = response.meta['name']
        item['price'] = response.meta['price']
        item['prod_url'] = response.url

        # IMAGE_SELECTOR = './/img[@class = "img"]/@src'
        # IMAGE_SELECTOR = 'img[class*=img] img::attr(src)'
        # item['image_urls'] = response.css(IMAGE_SELECTOR).extract()
        img_urls = re.findall('http://images.asos-media.com/.+?(?=\?\$)', str(response.body))
        img_urls = img_urls[1:]

        # print('image urls:', img_urls)
        img_url_list = []
        for img_url in img_urls:
            img_url_list.append(str(img_url + '?$XXL$&wid=513&fit=constrain'))

        item['image_urls'] = list(img_url_list)

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

        gender_search = re.search('gender:.+(?=\')', str(response.body))
        women = re.search('women', gender_search.group(0))
        print('sex regex found: ', women)
        print('category url count: ', str(response.meta['cat_url_count']))
        if women:
            item['sex'] = 'women'
        else:
            item['sex'] = 'men'

        item['sale'] = response.meta['is_sale']
        item['saleprice'] = response.meta['price_sale']
        item['color'] = response.meta['color']
        item['brand'] = response.meta['brand']
        item['currency'] = (response.meta['currency'])

        yield item

