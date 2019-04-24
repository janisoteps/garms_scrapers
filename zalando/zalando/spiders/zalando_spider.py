import scrapy
# from scrapy.selector import Selector
from zalando.items import ZalandoItem
import hashlib
# import re
import requests
import json
import datetime


class ZalandoSpider(scrapy.Spider):
    name = "zalando_spider"

    # The main start function which initializes the scraping URLs and triggers parse function
    def start_requests(self):
        init_req_url = 'https://en.zalando.de/api/catalog/articles?limit=84&offset=84&sort=popularity'
        init_ajax_req = requests.get(init_req_url)
        init_json_dict = json.loads(init_ajax_req.text)
        page_count = init_json_dict['pagination']['page_count']

        for i in range(0, page_count, 1):
            inner_api_url = f'https://en.zalando.de/api/catalog/articles?limit=84&offset={i * 84}&sort=popularity'
            inner_ajax_req = requests.get(inner_api_url)
            inner_json_dict = json.loads(inner_ajax_req.text)
            item_array = inner_json_dict['articles']

            for item in item_array:
                name = item['name']
                price = item['price']['original']
                saleprice = item['price']['promotional']
                sale = item['price']['has_different_prices']
                sizes = item['sizes']
                prod_url = f'https://en.zalando.de/{item["url_key"]}.html'
                size_stock = [{"stock": "In stock", "size": size} for size in sizes]
                brand = item['brand_name']

                yield scrapy.Request(
                        url=prod_url,
                        callback=self.parse,
                        meta={
                            'name': name,
                            'price': price,
                            'saleprice': saleprice,
                            'sale': sale,
                            'size_stock': size_stock,
                            'brand': brand,
                            'prod_url': prod_url,
                            # 'category': cat_name,
                            # 'sex': sex
                        }
                    )

    #     urls = [
    #         'https://en.zalando.de/women-home/',
    #         'https://en.zalando.de/men-home/'
    #     ]
    #     for url in urls:
    #         sex = 'women' if url == 'https://en.zalando.de/women-home/' else 'men'
    #         yield scrapy.Request(
    #             url=url,
    #             callback=self.cat_collection,
    #             meta={
    #                 'sex': sex
    #             }
    #         )
    #
    # def cat_collection(self, response):
    #     links = Selector(response).xpath('.//a[contains(@class, "z-navicat-header_categoryListLink")]')
    #     sex = response.meta['sex']
    #
    #     for link in links:
    #         top_cat_url = f'https://en.zalando.de{link.xpath("./@href").extract_first()}'
    #         print(f'Cat URL: {top_cat_url}')
    #
    #         yield scrapy.Request(
    #             url=top_cat_url,
    #             callback=self.sub_cat_collection,
    #             meta={
    #                 'sex': sex
    #             }
    #         )
    #
    # def sub_cat_collection(self, response):
    #     sub_links = Selector(response).xpath('.//div[contains(@class, "cat_child")]//a[contains(@class, "cat_link")]')
    #     sex = response.meta['sex']
    #     print('SUB CAT COLLECTION')
    #     print(sub_links)
    #
    #     for sub_link in sub_links:
    #         sub_cat_path = sub_link.xpath('./@pathname').extract_first().replace('/', '')
    #
    #         print(f'Sub cat URL: {sub_cat_path}')
    #         cat_name = sub_link.xpath('./text()').extract_first()
    #         print(f'Cat name: {cat_name}')
    #
    #         api_url = f'https://en.zalando.de/api/catalog/articles?categories=' \
    #                   + f'{sub_cat_path}&limit=84&offset=0&sort=popularity '
    #
    #         ajax_req = requests.get(api_url)
    #         json_dict = json.loads(ajax_req.text)
    #
    #         page_count = json_dict['pagination']['page_count']
    #
    #         for i in range(0, page_count, 1):
    #             inner_api_url = f'https://en.zalando.de/api/catalog/articles?categories=' \
    #                       + f'{sub_cat_path}&limit=84&offset=0&sort=popularity '
    #
    #             inner_ajax_req = requests.get(inner_api_url)
    #             innder_json_dict = json.loads(inner_ajax_req.text)
    #
    #             item_array = innder_json_dict['articles']
    #
    #             for item in item_array:
    #                 name = item['name']
    #                 price = item['price']['original']
    #                 saleprice = item['price']['promotional']
    #                 sale = item['price']['has_different_prices']
    #                 sizes = item['sizes']
    #                 prod_url = item['url_key']
    #                 size_stock = [{"stock": "In stock", "size": size} for size in sizes]
    #                 brand = item['brand_name']
    #
    #                 # {"stock": "Out of stock", "size": "32"}
    #
    #                 yield scrapy.Request(
    #                         url=prod_url,
    #                         callback=self.parse,
    #                         meta={
    #                             'name': name,
    #                             'price': price,
    #                             'saleprice': saleprice,
    #                             'sale': sale,
    #                             'size_stock': size_stock,
    #                             'brand': brand,
    #                             'prod_url': prod_url,
    #                             'category': cat_name,
    #                             'sex': sex
    #                         }
    #                     )

    def parse(self, response):
        item = ZalandoItem()
        item['name'] = response.meta['name']
        item['price'] = response.meta['price']
        item['saleprice'] = response.meta['saleprice']
        item['sale'] = response.meta['sale']
        item['size_stock'] = response.meta['size_stock']
        item['prod_url'] = response.meta['prod_url']
        item['size_stock'] = response.meta['size_stock']
        item['brand'] = response.meta['brand']
        item['category'] = response.xpath('.//script[contains(@id, "pdp-props")]').re(r'category_tag\":\"(.*?)\"')[0]
        print(f'CATEGORY: {item["category"]}')
        image_matches = response.xpath('.//script[contains(@id, "pdp-props")]').re(r'reco2x\"\:\"(.*?)\"')
        image_urls = [image_match for image_match in image_matches]
        item['image_urls'] = image_urls
        item['image_hash'] = []
        for img_string in image_urls:
            # Check if image string is a string, if not then do not pass this item
            if isinstance(img_string, str):
                hash_object = hashlib.sha1(img_string.encode('utf8'))
                hex_dig = hash_object.hexdigest()
                item['image_hash'].append(hex_dig)

        item['date'] = int(datetime.datetime.now().timestamp())
        item['currency'] = 'EUR'
        item['colour_string'] = response.xpath('.//script[contains(@id, "pdp-props")]')\
            .re(r'\"color\":\"(.{2,70}?)\"')[0]
        item['description'] = response.meta['name']

        categories = response.xpath('.//script[contains(@id, "pdp-props")]').re(r'\"categories\":(.*?),\"brand')[0]
        item['sex'] = 'women' if 'women' in list(categories) else 'men'

        yield item
