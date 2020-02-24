import scrapy
from scrapy.selector import Selector
from uniqlo.items import UniqloItem
import hashlib
import re
import datetime
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
        