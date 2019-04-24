import scrapy
from scraper6.items import TopshopItem
import hashlib
import re
import requests
import json
import datetime


class TopmanSpider(scrapy.Spider):
    name = "topman_spider_uk_2"

    # The main start function which initializes the scraping URLs and triggers parse function
    def start_requests(self):
        urls = [
            'http://www.topman.com/?geoip=home'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.infinite_request)

    # Topshop has infinite scrolling, so we need to simulate ajax call to server requesting product data for scrolling
    # From ajax response then extract each product URL and trigger a scraping request
    def infinite_request(self, response):
        cat_dict_arr = re.findall('(?<=NAV_ENTRY_TYPE_CATEGORY).*?(?=\})', response.text)
        cat_name_arr = [re.search('(?<=label\"\:\").*?(?=\")', cat_dict).group(0) for cat_dict in cat_dict_arr]
        cat_filter_arr = [re.search('(?<=categoryFilter\"\:\").*?(?=\")', cat_dict).group(0) for cat_dict in
                          cat_dict_arr]
        cat_info_arr = [{'cat_name': cat_name, 'cat_filter': cat_filter_arr[cat_name_arr.index(cat_name)]} for cat_name
                        in cat_name_arr]
        headers = {'BRAND-CODE': 'tmuk'}

        for cat_info in cat_info_arr:
            req_url = f'https://www.topman.com/api/products?currentPage=1&pageSize=24&category={cat_info["cat_filter"]}'
            ajax_req = requests.get(req_url, headers=headers)
            json_dict = json.loads(ajax_req.text)
            prod_count = json_dict['totalProducts']
            page_count = int(prod_count / 24)
            for page_nr in range(1, page_count):
                page_req_url = f'https://www.topman.com/api/products?currentPage={page_nr}&pageSize=24&category={cat_info["cat_filter"]}'
                page_ajax_req = requests.get(page_req_url, headers=headers)
                page_json_dict = json.loads(page_ajax_req.text)
                products = page_json_dict['products']
                for product in products:
                    prod_name = product['name']
                    # price = None
                    saleprice = None
                    unit_price = product['unitPrice']
                    # was_price = None
                    try:
                        was_price = product['wasPrice']
                    except:
                        was_price = None
                    if was_price is not None:
                        price = was_price
                        saleprice = unit_price
                    else:
                        price = unit_price
                    prod_url = f'https://www.topman.com{product["productUrl"]}'
                    image_urls = [
                        product['productBaseImageUrl'],
                        product['outfitBaseImageUrl']
                    ]
                    yield scrapy.Request(
                        url=prod_url,
                        callback=self.parse,
                        meta={
                            'cat_name': cat_info['cat_name'],
                            'prod_name': prod_name,
                            'price': price,
                            'saleprice': saleprice,
                            'prod_url': prod_url,
                            'image_urls': image_urls
                        }
                    )

    def parse(self, response):
        # Write out xpath and css selectors for all fields to be retrieved
        item = TopshopItem()

        # Assemble the item object which will be passed then to pipeline
        item['shop'] = 'Top Man'
        item['name'] = response.meta['prod_name']
        item['price'] = response.meta['price']
        item['saleprice'] = response.meta['saleprice']

        item['prod_url'] = response.meta['prod_url']
        item['image_urls'] = response.meta['image_urls']
        item['brand'] = 'Top Man'
        item['currency'] = 'GBP'
        if item['saleprice'] is not None:
            item['sale'] = True
        else:
            item['sale'] = False

        item['sex'] = 'men'
        item['date'] = int(datetime.datetime.now().timestamp())
        item['description'] = '\n'.join(response.xpath('.//div[@class="ProductDescription-content"]/ul/li/text()').extract())
        color_string = re.search('(?<=color\"\:\").*?(?=\")', response.text)
        item['color_string'] = color_string.group(0)
        item['category'] = response.meta['cat_name']

        sizes_arr = response.xpath('.//select[@id="productSizes"]/option[@role="option"]/text()').extract()
        try:
            sizes_stock = list(map(lambda x: {
                'stock': x.split(': ')[1],
                'size': x.split('Size ')[1].split(':')[0]
            }, sizes_arr))
        except:
            sizes_stock = list(map(lambda x: {
                'stock': 'In stock',
                'size': x.split('Size ')[1]
            }, sizes_arr))

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
