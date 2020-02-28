import scrapy
# from scrapy.selector import Selector
from realisation.items import RealisationItem
import hashlib
# import re
import time
# from urllib.parse import urlparse


class RealisationSpider(scrapy.Spider):
    name = "realisation_spider_uk"

    def start_requests(self):
        urls = [
            'https://uk.realisationpar.com/shop/everything/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.get_cats)

    def get_cats(self, response):
        cat_matches = response.xpath('.//li[@class="navPage-subMenu-item"]/a')
        cat_dicts = []
        for cat_match in cat_matches:
            cat_url = cat_match.xpath('.//@href').extract_first()
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
        prod_urls = response.xpath('.//h4[contains(@class,"product-name")]/a/@href').extract()
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

    def parse(self, response):
        item = RealisationItem()
        item['shop'] = 'Realisation Par'

        name_1 = response.xpath('.//h1[@class="productView-title"]/text()').extract_first()
        if name_1 is not None:
            name_1 = name_1.strip()
        name_2 = response.xpath('.//meta[@name="description"]/@content').extract_first()
        if name_2 is not None:
            name_2 = name_2.strip()
        item['name'] = f'{name_1}. {name_2}'

        price_current_match = response.xpath('.//meta[@property="product:price:amount"]/@content').extract_first()
        price_current = float(price_current_match)
        price_was_match = response.xpath('.//meta[@property="og:price:standard_amount"]/@content').extract_first()
        price_was = None
        if price_was_match is not None:
            price_was = float(price_was_match)
        if price_was is not None:
            sale = True
            price = price_was
            saleprice = price_current
        else:
            sale = False
            price = price_current
            saleprice = None
        item['price'] = price
        item['sale'] = sale
        item['saleprice'] = saleprice
        item['prod_url'] = response.meta['prod_url']

        if isinstance(response.meta['prod_url'], str):
            prod_id_hash_object = hashlib.sha1(response.meta['prod_url'].encode('utf8'))
            prod_id_hex_dig = prod_id_hash_object.hexdigest()
            item['prod_id'] = prod_id_hex_dig

        item['image_urls'] = response.xpath('.//img[contains(@class,"productView-image--default")]/@src').extract()
        item['image_hash'] = []
        for img_string in item['image_urls']:
            # Check if image string is a string, if not then do not pass this item
            if isinstance(img_string, str):
                hash_object = hashlib.sha1(img_string.encode('utf8'))
                hex_dig = hash_object.hexdigest()
                item['image_hash'].append(hex_dig)

        item['sex'] = 'women'
        item['brand'] = 'Realisation Par'
        item['currency'] = 'GBP'
        item['date'] = int(time.time())
        description_matches = response.xpath('.//div[@id="tab-description"]//span/text()').extract()
        item['description'] = '\n'.join(description_matches)
        item['color_string'] = None
        item['category'] = response.meta['cat_name']

        size_matches = response.xpath('.//div[contains(@class,"size-options")]/label')
        size_stock = []
        for size_match in size_matches:
            size_stock.append({
                'size': size_match.xpath('.//text()').extract()[1],
                'stock': 'In stock'
            })
        item['size_stock'] = size_stock
        if len(size_stock) > 0:
            in_stock = True
        else:
            in_stock = False
        item['in_stock'] = in_stock

        yield item
