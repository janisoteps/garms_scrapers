import scrapy
from scrapy.selector import Selector
from freeppl.items import FreepplItem
import hashlib
import re
# import requests
# import json
import datetime
from urllib.parse import urlparse


class FreepplSpider(scrapy.Spider):
    name = "freeppl_spider_uk"

    # The main start function which initializes the scraping URLs and triggers parse function
    def start_requests(self):
        urls = [
            'https://www.freepeople.com/uk/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.get_cat_urls)

    def get_cat_urls(self, response):
        links = Selector(response).xpath('.//a[contains(@class, "main-navigation")]')
        print(f'links: {links}')

        for link in links:
            cat_url = link.xpath("./@href").extract_first()
            if len(cat_url.split('freepeople.com')) != 2:
                cat_url = f'https://www.freepeople.com{cat_url}'
            print(f'Cat URL: {cat_url}')
            cat_name = link.xpath('./span/text()').extract_first()
            cat_name = ''.join(ch for ch in cat_name if ch.isalnum())
            print(f'Cat name: {cat_name}')
            yield scrapy.Request(
                url=cat_url,
                callback=self.get_prod_urls,
                meta={
                    'cat_name': cat_name
                }
            )

    def get_prod_urls(self, response):
        current_page = None
        page_count = None
        page_count_regex = re.search(r'page_total_count:\ \"(.*?)\"', response.text)
        if page_count_regex is not None:
            page_count = page_count_regex.group(1)
        current_page_regex = re.search(r'page_number:\ \"(.*?)\"', response.text)
        if current_page_regex is not None:
            current_page = int(current_page_regex.group(1))
        print(f'page count: {page_count}')
        prod_links = Selector(response).xpath('.//a[contains(@class, "product-tile__image-link")]')

        for prod_link in prod_links:
            prod_url = prod_link.xpath('./@href').extract_first()
            if len(prod_url.split('freepeople.com')) != 2:
                prod_url = f'https://www.freepeople.com{prod_url}'
            print(f'Prod URL: {prod_url}')

            yield scrapy.Request(
                url=prod_url,
                callback=self.parse,
                meta={
                    'cat_name': response.meta['cat_name']
                }
            )

        if current_page != page_count:
            parsed_url = urlparse(response.url)
            next_page_url = f'{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}?page={current_page + 1}'
            yield scrapy.Request(
                url=next_page_url,
                callback=self.get_prod_urls,
                meta={
                    'cat_name': response.meta['cat_name']
                }
            )

    def parse(self, response):
        # Write out xpath and css selectors for all fields to be retrieved
        item = FreepplItem()
        NAME_SELECTOR = './/h1[contains(@class, "product-meta__h1")]/span/text()'
        CURRENT_PRICE_SELECTOR = './/span[contains(@class, "current-price")]/text()'
        ORIG_PRICE_SELECTOR = './/span[contains(@class, "original-price")]/text()'
        IMAGE_SELECTOR = './/img[contains(@class, "zoom-product-image")]/@src'
        COLOR_SELECTOR = './/span[contains(@class, "product-colors__name")]/text()'
        # SALE_PRICE_SELECTOR = './/div[@class = "product_prices"]/span[3]/text()'
        SIZES_SELECTOR = './/input[contains(@class, "js-size-select")]/@value'
        OOS_SELECTOR = './/li[contains(@class, "is-back-in-stock")]/input/@value'

        # Assemble the item object which will be passed then to pipeline
        item['shop'] = 'Free People'
        name = response.xpath(NAME_SELECTOR).extract_first()
        item['name'] = ''.join(ch for ch in name if ch.isalnum())

        item['price'] = None
        item['saleprice'] = None
        current_price = response.xpath(CURRENT_PRICE_SELECTOR).extract_first()
        current_price = int(''.join(ch for ch in current_price if ch.isalnum()))
        orig_price = response.xpath(ORIG_PRICE_SELECTOR).extract_first()
        if orig_price is not None:
            item['price'] = int(''.join(ch for ch in orig_price if ch.isalnum()))
            item['saleprice'] = current_price
            item['sale'] = True
        else:
            item['price'] = current_price
            item['saleprice'] = None
            item['sale'] = False

        item['prod_url'] = response.url

        img_url_paths = response.xpath(IMAGE_SELECTOR).extract()
        item['image_urls'] = [f'https:{img_url_path}' for img_url_path in img_url_paths]
        brand_regex = re.search(r'brand\":\ \{\"\@type\":\ \"Thing\"\,\ \"name\"\:\ \"(.*?)\"', response.text)
        if brand_regex is not None:
            item['brand'] = brand_regex.group(1)
        else:
            item['brand'] = 'Free People'
        item['currency'] = 'GBP'

        # Free People has only women fashion
        item['sex'] = 'women'
        item['date'] = int(datetime.datetime.now().timestamp())
        desc_regex = re.search(r'\"description\":\ \"(.*?)\"', response.text)
        if desc_regex is not None:
            item['description'] = desc_regex.group(1)

        color_string = response.xpath(COLOR_SELECTOR).extract_first()
        item['color_string'] = ''.join(ch for ch in color_string if ch.isalnum())
        item['category'] = response.meta['cat_name']

        sizes_match = response.xpath(SIZES_SELECTOR).extract()
        print('sizes match')
        print(sizes_match)
        sizes = [{'size': x} for x in sizes_match]
        print(f'sizes:')
        print(sizes)
        sizes_oos_match = response.xpath(OOS_SELECTOR).extract()
        print(f'sizes stock match')
        print(sizes_oos_match)
        sizes_stock = [
            {
                'stock': 'Out of stock',
                'size': size['size']
            } if size['size'] in sizes_oos_match else {
                'stock': 'In stock',
                'size': size['size']
            } for size in sizes
        ]
        print('SIZES STOCK:')
        print(sizes_stock)
        item['size_stock'] = sizes_stock
        if len(item['size_stock']) > 0:
            item['in_stock'] = True
        else:
            item['in_stock'] = False

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
