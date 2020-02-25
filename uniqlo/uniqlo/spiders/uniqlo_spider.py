import scrapy
from scrapy.selector import Selector
from uniqlo.items import UniqloItem
import hashlib
import re
import time
from urllib.parse import urlparse


class UniqloSpider(scrapy.Spider):
    name = "uniqlo_spider_uk"

    def start_requests(self):
        urls = [
            'https://www.uniqlo.com/uk/en/women'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.get_cats)

    def get_cats(self, response):
        cats = response.xpath('.//div[@class="category-content"]/div/div/div/div/ul/li/a')

        cat_dicts = []
        for cat in cats:
            cat_url = cat.xpath('.//@href').extract_first()
            cat_name = cat.xpath('.//text()').extract_first().strip()
            if '/women' in cat_url:
                cat_dicts.append({
                    'cat_name': cat_name,
                    'cat_url': cat_url,
                    'sex': 'women'
                })
            if '/men' in cat_url:
                cat_dicts.append({
                    'cat_name': cat_name,
                    'cat_url': cat_url,
                    'sex': 'men'
                })

        for cat_dict in cat_dicts:
            yield scrapy.Request(
                url=cat_dict['cat_url'],
                callback=self.get_prod_urls,
                meta={
                    'cat_url': cat_dict['cat_url'],
                    'cat_name': cat_dict['cat_name'],
                    'sex': cat_dict['sex']
                }
            )

    def get_prod_urls(self, response):
        prod_urls = response.xpath('.//div[contains(@class, "productTile__imageContainer")]/a/@data-seoproducturl').extract()

        for prod_url in prod_urls:
            yield scrapy.Request(
                url=prod_url,
                callback=self.parse,
                meta={
                    'prod_url': prod_url,
                    'cat_url': response.meta['cat_url'],
                    'cat_name': response.meta['cat_name'],
                    'sex': response.meta['sex']
                }
            )

    def parse(self, response):
        item = UniqloItem()
        item['shop'] = 'Uniqlo'
        item['name'] = response.xpath('.//h1[contains(@class,"pdp__title")]/text()').extract_first()
        price_original = response.xpath('.//span[@class="price-standard"]/text()').extract_first()
        item['price'] = float(price_original.strip('£'))
        price_sale = response.xpath('.//span[contains(@class,"price-sales")]/text()').extract_first()
        price_sale = float(price_sale.strip('£'))
        item['sale'] = item['price'] != price_sale
        if item['sale'] == True:
            item['saleprice'] = price_sale
        else:
            item['saleprice'] = None

        item['prod_url'] = response.meta['prod_url']

        if isinstance(response.meta['prod_url'], str):
            prod_id_hash_object = hashlib.sha1(response.meta['prod_url'].encode('utf8'))
            prod_id_hex_dig = prod_id_hash_object.hexdigest()
            item['prod_id'] = prod_id_hex_dig

        img_url_matches = response.xpath('.//img[contains(@class,"pdp__mainImg")]/@src').extract()
        item['image_urls'] = [img_url_match.split('?')[0] for img_url_match in img_url_matches]

        item['image_hash'] = []
        for img_string in item['image_urls']:
            # Check if image string is a string, if not then do not pass this item
            if isinstance(img_string, str):
                hash_object = hashlib.sha1(img_string.encode('utf8'))
                hex_dig = hash_object.hexdigest()
                item['image_hash'].append(hex_dig)

        item['sex'] = response.meta['sex']
        item['brand'] = 'Uniqlo'
        item['currency'] = 'GBP'
        item['date'] = int(time.time())

        description = response.xpath('.//div[contains(@class,"js-pdpDescription__container")]/text()').extract_first()
        item['description'] = '\n'.join(description)
        item['color_string'] = None
        item['category'] = response.meta['cat_name']

        size_matches = response.xpath('.//div[contains(@class,"pdp__swatchBox--size")]/button')

        size_stock = []
        for size_match in size_matches:
            size = size_match.xpath('.//@data-size-value').extract_first()
            stock_class = size_match.xpath('.//@class').extract_first()
            if 'pdp__swatch--available' in stock_class:
                stock = 'In stock'
            else:
                stock = 'Out of stock'
            size_stock.append({
                'stock': stock,
                'size': size
            })
        item['size_stock'] = size_stock

        in_stock_sizes = [size for size in size_stock if size['stock'] == 'In stock']
        item['in_stock'] = len(in_stock_sizes) > 0

        yield item
