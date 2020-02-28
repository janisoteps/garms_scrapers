import scrapy
# from scrapy.selector import Selector
from collusion.items import CollusionItem
import hashlib
import re
import json
import time
# from urllib.parse import urlparse


class CollusionSpider(scrapy.Spider):
    name = "collusion_spider_uk"

    def start_requests(self):
        urls = [
            'https://www.collusion.com/collection'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.get_cats)

    def get_cats(self, response):
        cat_matches = response.xpath('.//ul[@class="collection"]/li/ul/li/a')
        cat_dicts = []
        for cat_match in cat_matches:
            cat_url = f'https://www.collusion.com{cat_match.xpath(".//@href").extract_first()}'
            cat_name = cat_match.xpath('.//text()').extract_first()
            cat_dicts.append({
                'cat_url': cat_url,
                'cat_name': cat_name
            })

        for cat_dict in cat_dicts:
            yield scrapy.Request(
                url=cat_dict['cat_url'],
                callback=self.get_prod_urls,
                meta={
                    'cat_url': cat_dict['cat_url'],
                    'cat_name': cat_dict['cat_name']
                }
            )

    def get_prod_urls(self, response):
        prod_url_matches = response.xpath('.//div[contains(@class,"teaser--product")]/a/@href').extract()
        prod_urls = [f'https://www.collusion.com{prod_url_match}' for prod_url_match in prod_url_matches]

        for prod_url in prod_urls:
            yield scrapy.Request(
                url=prod_url,
                callback=self.parse,
                meta={
                    'prod_url': prod_url,
                    'cat_url': response.meta['cat_url'],
                    'cat_name': response.meta['cat_name']
                }
            )

        next_cat_page_match = response.xpath('.//nav[contains(@class,"pagination--next")]/a/@href').extract_first()
        if next_cat_page_match is not None:
            next_cat_page = f'{response.meta["cat_url"]}{next_cat_page_match}'
            yield scrapy.Request(
                url=next_cat_page,
                callback=self.get_prod_urls,
                meta={
                    'cat_url': response.meta['cat_url'],
                    'cat_name': response.meta['cat_name']
                }
            )

    def parse(self, response):
        item = CollusionItem()
        item['shop'] = 'Collusion'
        item['name'] = response.xpath('.//h1[@property="name"]/text()').extract_first().title()
        prod_json_string_match = re.search('(?<=\_\_NEXT\_DATA\_\_\ \=\ ).*(?=\;\_\_NEXT\_LOADED\_PAGES\_\_)',
                                           response.text, re.I | re.DOTALL)
        prod_json_string = prod_json_string_match.group(0)
        prod_json = json.loads(prod_json_string)
        price_current = prod_json['props']['pageProps']['product']['price']['current']['value']
        price_previous = prod_json['props']['pageProps']['product']['price']['previous']['value']
        if price_current < price_previous:
            sale = True
            saleprice = price_current
            price = price_previous
        else:
            sale = False
            saleprice = None
            price = price_current

        item['price'] = price
        item['sale'] = sale
        item['saleprice'] = saleprice

        item['prod_url'] = response.meta['prod_url']
        if isinstance(response.meta['prod_url'], str):
            prod_id_hash_object = hashlib.sha1(response.meta['prod_url'].encode('utf8'))
            prod_id_hex_dig = prod_id_hash_object.hexdigest()
            item['prod_id'] = prod_id_hex_dig

        item['image_urls'] = response.xpath('.//ul[@class="product-images"]/li/img/@src').extract()
        item['image_hash'] = []
        for img_string in item['image_urls']:
            # Check if image string is a string, if not then do not pass this item
            if isinstance(img_string, str):
                hash_object = hashlib.sha1(img_string.encode('utf8'))
                hex_dig = hash_object.hexdigest()
                item['image_hash'].append(hex_dig)

        item['sex'] = 'women'
        item['brand'] = 'Collusion'
        item['currency'] = 'GBP'
        item['date'] = int(time.time())
        item['description'] = response.xpath('.//td[@property="description"]/p/text()').extract_first()
        item['color_string'] = None
        item['category'] = response.meta['cat_name']

        size = prod_json['props']['pageProps']['product']['sizing']
        item['size_stock'] = [{
            'size': size,
            'stock': 'In stock'
        }]
        item['in_stock'] = len(item['size_stock']) > 0

        yield item
