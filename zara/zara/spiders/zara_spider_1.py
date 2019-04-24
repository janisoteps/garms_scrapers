import scrapy
from zara.items import ZaraItem
import hashlib
import re
# import requests
# import json
import datetime
# import random


class ZaraSpider(scrapy.Spider):
    name = "zara_spider_uk_1"

    # The main start function which initializes the scraping URLs and triggers parse function
    def start_requests(self):
        urls = [
            'https://www.zara.com/uk/en/woman-l1000.html?v1=358532'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.get_cat_urls)

    def get_cat_urls(self, response):
        def get_sex_name(string):
            cat_string_arr = string.split('/')[-1].split('.')[0].split('-')
            cat_string_arr_clean = [string for string in cat_string_arr if string.isalpha()]
            sex = 'women' if 'woman' in cat_string_arr_clean or 'trf' in cat_string_arr_clean else 'men' if 'man' in cat_string_arr_clean else None
            cat_string_arr_sexless = [string for string in cat_string_arr_clean if
                                      string not in ['man', 'woman', 'trf']]
            cat_string = ' '.join(cat_string_arr_sexless)
            return {
                'sex': sex,
                'cat_name': cat_string,
                'cat_url': string
            }

        cat_urls_women = response.xpath('.//li[@data-name="WOMAN"]/ul/li[@data-isredirected="false"]/a[contains(@class, "_category-link")]/@href').extract()
        cat_w_names_urls = [get_sex_name(cat_url) for cat_url in cat_urls_women]
        cat_w_names_urls_nokids = [cat_dict for cat_dict in cat_w_names_urls if cat_dict['sex'] is not None]

        cat_urls_trf = response.xpath('.//li[@data-name="TRF"]/ul/li[@data-isredirected="false"]/a[contains(@class, "_category-link")]/@href').extract()
        cat_trf_names_urls = [get_sex_name(cat_url) for cat_url in cat_urls_trf]
        cat_trf_names_urls_nokids = [cat_dict for cat_dict in cat_trf_names_urls if cat_dict['sex'] is not None]

        cat_urls_men = response.xpath('.//li[@data-name="MAN"]/ul/li[@data-isredirected="false"]/a[contains(@class, "_category-link")]/@href').extract()
        cat_men_names_urls = [get_sex_name(cat_url) for cat_url in cat_urls_men]
        cat_men_names_urls_nokids = [cat_dict for cat_dict in cat_men_names_urls if cat_dict['sex'] is not None]

        cat_list = cat_w_names_urls_nokids + cat_trf_names_urls_nokids + cat_men_names_urls_nokids

        for cat_dict in cat_list:
            yield scrapy.Request(
                url=cat_dict['cat_url'],
                callback=self.get_prod_urls,
                meta={
                    'cat_name': cat_dict['cat_name'],
                    'sex': cat_dict['sex'],
                    'cat_url': cat_dict['cat_url']
                }
            )

    def get_prod_urls(self, response):
        prod_urls = response.xpath('.//li[contains(@class, "product")]/a[contains(@class, "item")]/@href').extract()
        print(f'{len(prod_urls)} product URLs found')

        for prod_url in prod_urls:
            yield scrapy.Request(
                url=prod_url,
                callback=self.parse,
                meta={
                    'cat_name': response.meta['cat_name'],
                    'sex': response.meta['sex'],
                    'prod_url': prod_url
                }
            )

    def parse(self, response):
        item = ZaraItem()
        item['shop'] = 'Zara'
        item['sex'] = response.meta['sex']
        item['brand'] = 'Zara'
        item['currency'] = 'GBP'
        item['prod_url'] = response.meta['prod_url']
        item['category'] = response.meta['cat_name']
        name = response.xpath('.//h1[@class="product-name"]/text()').extract_first()
        if name is not None:
            item['name'] = name.title()
            img_urls = response.xpath('.//a[contains(@class, "main-image")]/@href').extract()
            item['image_urls'] = [f'http:{img_url}' for img_url in img_urls]
            item['color_string'] = response.xpath('.//span[@class="_colorName"]/text()').extract_first()
            price_match = re.search('(?<=price\": \").*?(?=\")', response.text)
            if price_match is not None:
                item['price'] = float(price_match.group(0))
                item['saleprice'] = None
                item['sale'] = False
                item['description'] = response.xpath('.//p[@class="description"]/text()').extract_first()

                sizes = response.xpath('.//input[@name="size"]/@value').extract()
                oos_sizes = response.xpath('.//input[@disabled="disabled"]/@value').extract()
                item['size_stock'] = [{
                                   'stock': 'Out of stock',
                                   'size': size
                               } if size in oos_sizes else {
                    'stock': 'In stock',
                    'size': size
                } for size in sizes]

                img_strings = item['image_urls']
                item['image_hash'] = []
                for img_string in img_strings:
                    # Check if image string is a string, if not then do not pass this item
                    if isinstance(img_string, str):
                        # print(img_string)
                        hash_object = hashlib.sha1(img_string.encode('utf8'))
                        hex_dig = hash_object.hexdigest()
                        item['image_hash'].append(hex_dig)

                item['date'] = int(datetime.datetime.now().timestamp())

                yield item
