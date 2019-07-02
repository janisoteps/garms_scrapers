import scrapy
from boohoo.items import BoohooItem
import hashlib
import re
import json
import math
import time


class BoohooSpider(scrapy.Spider):
    name = "boohoo_spider_uk"

    # The main start function which initializes the scraping URLs and triggers parse function
    def start_requests(self):
        urls = [
            'https://www.boohoo.com/page/sitemap.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.cat_link_collection)

    # Go through the top menu in initial response to collect links of each category
    def cat_link_collection(self, response):
        cat_links = response.xpath('.//h4[@class="sitemap-subtitle"]/a')
        cat_link_arr = []
        for cat_link in cat_links:
            cat_url = cat_link.xpath('.//@href').extract_first()
            cat_name_dirty = cat_link.xpath('.//text()').extract_first()
            cat_name = re.sub(r'([^\s\w]|_)+', '', cat_name_dirty).strip()
            link_dict = {
                'cat_url': cat_url,
                'cat_name': cat_name
            }
            cat_link_arr.append(link_dict)

        def get_sex(url_string):
            if 'womens' in url_string or 'maternity' in url_string:
                return 'women'
            else:
                return 'men'

        cat_link_sex_arr = [{
            'cat_url': cat_link['cat_url'],
            'cat_name': cat_link['cat_name'],
            'cat_sex': get_sex(cat_link['cat_url'])
        } for cat_link in cat_link_arr]

        for cat_url_name in cat_link_sex_arr:
            yield scrapy.Request(
                url=cat_url_name['cat_url'],
                callback=self.cat_pages,
                meta={
                    'cat_name': cat_url_name['cat_name'],
                    'sex': cat_url_name['cat_sex'],
                    'cat_url': cat_url_name['cat_url']
                }
            )

    def cat_pages(self, response):
        prod_count_match = response.xpath('.//div[contains(@class, "js-product-count")]/text()').extract_first()
        prod_count_string = prod_count_match.strip()
        prod_count = int(re.sub("\D", "", prod_count_string))
        page_count = math.ceil(prod_count / 60)

        for k in range(0, page_count):
            print(k * 60)
            req_url = response.meta['cat_url'] + '?sz=60&start=' + str(k * 60)

            yield scrapy.Request(
                url=req_url,
                callback=self.prod_collect,
                meta={
                    'cat_name': response.meta['cat_name'],
                    'sex': response.meta['sex']
                }
            )

    def prod_collect(self, response):
        product_tiles = response.xpath('.//div[@class="product-tile"]')
        for product_tile in product_tiles:
            prod_url = product_tile.xpath('.//a[contains(@class, "name-link")]/@href').extract_first()
            prod_name = product_tile.xpath('.//a[contains(@class, "name-link")]/text()').extract_first()

            yield scrapy.Request(
                url='https://www.boohoo.com' + prod_url,
                callback=self.parse,
                meta={
                    'cat_name': response.meta['cat_name'],
                    'sex': response.meta['sex'],
                    'name': prod_name.strip(),
                    'prod_url': 'https://www.boohoo.com' + prod_url
                }
            )

    def parse(self, response):
        item = BoohooItem()
        price_match = response.xpath('.//span[contains(@itemprop, "price")]/@content').extract_first()
        current_price = None
        if price_match is not None:
            current_price = float(price_match)

        price_class_match = response.xpath('.//span[contains(@itemprop, "price")]/@class')
        price_class = None
        if price_class_match is not None:
            price_class = price_class_match

        item['sale'] = 'sales' in price_class

        if item['sale']:
            item['saleprice'] = current_price
            price_std_match = response.xpath('.//span[@class="price-standard"]/text()').extract_first()
            item['price'] = float(price_std_match.strip()[1:])
        else:
            item['saleprice'] = None
            item['price'] = current_price

        description_match = response.xpath('.//meta[@property="og:description"]/@content').extract_first()
        if description_match is not None:
            item['description'] = description_match

        img_urls = []
        primary_img_match = response.xpath('.//img[contains(@class, "js-primary-image")]/@src').extract_first()
        if primary_img_match is not None:
            primary_img = 'https:' + primary_img_match
            img_urls.append(primary_img)

        prim_im_split = img_urls[0].split('?')
        for t in range(1, 4):
            sec_img_url = f'{prim_im_split[0]}_{t}?{prim_im_split[1]}'
            img_urls.append(sec_img_url)

        item['image_urls'] = img_urls

        color_match = response.xpath('.//div[contains(text(), "Colour")]/span/text()').extract_first()
        if color_match is not None:
            item['color_string'] = color_match.strip()

        size_matches = response.xpath('.//ul[contains(@class, "swatches size")]/li/span/@data-variation-values').extract()
        size_arr = []
        for size_match in size_matches:
            size_json = json.loads(size_match)
            size_arr.append({
                'stock': 'In stock',
                'size': size_json['attributeValue']
            })
        item['size_stock'] = size_arr

        item['shop'] = 'Boohoo'
        item['name'] = response.meta['name']
        item['category'] = response.meta['cat_name']
        item['sex'] = response.meta['sex']
        item['prod_url'] = response.meta['prod_url']

        if isinstance(response.meta['prod_url'], str):
            prod_id_hash_object = hashlib.sha1(response.meta['prod_url'].encode('utf8'))
            prod_id_hex_dig = prod_id_hash_object.hexdigest()
            item['prod_id'] = prod_id_hex_dig

        img_strings = item['image_urls']
        item['image_hash'] = []
        for img_string in img_strings:
            # Check if image string is a string, if not then do not pass this item
            if isinstance(img_string, str):
                hash_object = hashlib.sha1(img_string.encode('utf8'))
                hex_dig = hash_object.hexdigest()
                item['image_hash'].append(hex_dig)

        item['brand'] = 'Boohoo'
        item['currency'] = '£'
        item['date'] = int(time.time())

        yield item
