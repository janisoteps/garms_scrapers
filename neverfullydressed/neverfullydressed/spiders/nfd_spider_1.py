import scrapy
from neverfullydressed.items import NeverfullydressedItem
import hashlib
import time
import re
import json
import unicodedata


class NeverFullyDressedSpider(scrapy.Spider):
    name = "nfd_spider"

    def __init__(self, name=None, **kwargs):
        super().__init__(name=None, **kwargs)
        self.visited_urls = set()

    # Main start function
    def start_requests(self):
        base_url = 'https://www.neverfullydressed.co.uk'
        cat_urls = [
            '/collections/newness',
             '/collections/bestsellers',
             '/collections/dresses',
             '/collections/skirts',
             '/collections/co-ords',
             '/collections/tops',
             '/collections/knitwear',
             '/collections/jackets-coats',
             '/collections/trousers-shorts',
             '/collections/made-designed-in-london',
             '/collections/charitees',
             '/collections/back-in-stock',
             '/collections/accessories',
             '/collections/bags',
             '/collections/hats',
             '/collections/hair',
             '/collections/scarves',
             '/collections/earrings',
             '/collections/rings',
             '/collections/necklaces',
             '/collections/belts',
             '/collections/phone-cases',
             '/collections/gift-vouchers',
             '/collections/brow-kits',
             '/collections/party-wear',
             '/collections/party-dresses',
             '/collections/finishing-touches',
             '/collections/gifting',
             '/collections/gift-box',
             '/collections/gifts-under-20',
             '/collections/gifts-50-under',
             '/collections/gifts-100-under'
        ]

        for cat_url in cat_urls:
            req_url = f'{base_url}{cat_url}'

            yield scrapy.Request(url=req_url, callback=self.prod_collection)

    def prod_collection(self, response):
        next_page = response.xpath('.//link[@rel="next"]/@href').extract_first()

        prod_urls = response.xpath('.//div[@class="prod-image"]/a/@href').extract()
        for prod_url in prod_urls:
            req_url = f'https://www.neverfullydressed.co.uk{prod_url}'
            yield scrapy.Request(url=req_url, callback=self.parse)

        if next_page is not None:
            next_page_url = f'https://www.neverfullydressed.co.uk{next_page}'
            yield scrapy.Request(url=next_page_url, callback=self.prod_collection)

    def parse(self, response):
        color_pattern_cats = [
            'abstract',
            'acid',
            'animal',
            'apricot',
            'beige',
            'black',
            'blue',
            'bright',
            'brown',
            'burgundy',
            'charcoal',
            'check',
            'chevron',
            'circle',
            'clear',
            'cream',
            'crochet',
            'dark',
            'dot',
            'dye',
            'floral',
            'flower',
            'gingham',
            'gold',
            'green',
            'grey',
            'heart',
            'indigo',
            'jacquard',
            'khaki',
            'leopard',
            'lettuce',
            'light',
            'lilac',
            'lime',
            'mango',
            'mesh',
            'monochrome',
            'mustard',
            'navy',
            'neon',
            'nude',
            'ombre',
            'orange',
            'paisley',
            'pale',
            'palm',
            'pattern',
            'peach',
            'pink',
            'pinstripe',
            'polka',
            'purple',
            'rainbow',
            'red',
            'rib',
            'rose',
            'rust',
            'silver',
            'snake',
            'spot',
            'square',
            'star',
            'stitch',
            'straw',
            'stripe',
            'striped',
            'stripes',
            'tan',
            'tea',
            'tiger',
            'tortoiseshell',
            'triangle',
            'tropical',
            'vanilla',
            'wash',
            'washed',
            'white',
            'yellow',
            'zebra'
        ]
        item = NeverfullydressedItem()

        item['shop'] = 'Never Fully Dressed'
        name = response.xpath('.//h1[@itemprop="name"]/text()').extract_first()
        if name is not None:
            item['name'] = name.strip()

        prod_price = response.xpath('.//div[@id="product-price"]/span[@class="product-price"]/span/text()').extract_first()
        prod_price_number = float(re.sub('[^\d\.]', '', prod_price))
        was_price = response.xpath('.//div[@id="product-price"]/span[@class="was"]/span/text()').extract_first()
        was_price_number = None
        if was_price is not None:
            was_price_number = float(re.sub('[^\d\.]', '', was_price))

        sale = False
        saleprice = None
        if was_price is not None:
            sale = True
            price = was_price_number
            saleprice = round(prod_price_number / 1.2068965, 0)
        else:
            price = prod_price_number

        item['price'] = round(price / 1.2068965, 0)
        item['sale'] = sale
        item['saleprice'] = saleprice
        item['prod_url'] = response.url
        if isinstance(response.url, str):
            prod_id_hash_object = hashlib.sha1(response.url.encode('utf8'))
            prod_id_hex_dig = prod_id_hash_object.hexdigest()
            item['prod_id'] = prod_id_hex_dig

        prod_images = response.xpath('.//a[@class="product-fancybox"]/img/@data-src').extract()
        item['image_urls'] = ['https:' + prod_url.replace('{width}', '1000') for prod_url in prod_images]

        img_strings = item['image_urls']
        item['image_hash'] = []
        for img_string in img_strings:
            # Check if image string is a string, if not then do not pass this item
            if isinstance(img_string, str):
                hash_object = hashlib.sha1(img_string.encode('utf8'))
                hex_dig = hash_object.hexdigest()
                item['image_hash'].append(hex_dig)

        item['sex'] = 'women'

        prod_name_arr = [word.lower() for word in item['name'].split(' ')]
        color_arr = [word for word in prod_name_arr if word in color_pattern_cats]
        color_string = None
        if len(color_arr) > 0:
            color_string = color_arr[0]
        item['color_string'] = color_string

        item['brand'] = 'Never Fully Dressed'
        item['currency'] = '£'
        item['date'] = int(time.time())

        description_match = response.xpath('.//meta[@property="og:description"]/@content').extract_first()
        description = None
        if description_match is not None:
            description_decoded = unicodedata.normalize('NFKD', description_match)
            description = description_decoded.replace('\n', '')
        item['description'] = description

        prod_json = response.xpath('.//script[@class="product-json"]/text()').extract_first()
        prod_json_loaded = json.loads(prod_json)
        size_variants = prod_json_loaded['variants']
        size_stock = []
        for size_variant in size_variants:
            size = size_variant['title']
            available = size_variant['available']
            size_stock.append({
                'size': size,
                'stock': 'In stock' if available else 'Out of stock'
            })
        item['size_stock'] = size_stock

        item['category'] = prod_json_loaded['type'].lower()

        yield item
