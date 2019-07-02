import scrapy
from farfetch.items import FarfetchItem
import hashlib
import time
import re
import json


class FarfetchSpider(scrapy.Spider):
    name = "farfetch_spider"

    # Main start function
    def start_requests(self):
        url = 'https://www.farfetch.com/uk/sitemap/'

        yield scrapy.Request(url=url, callback=self.category_collection)

    # Go through category links
    def category_collection(self, response):
        cat_url_anchors_top = response.xpath('.//h4/a')
        cat_url_anchors_lower = response.xpath('.//h5/a')

        cat_url_elems = [cat_url_anchors_top, cat_url_anchors_lower]

        cat_url_list = []
        for cat_url_elem_list in cat_url_elems:
            for cat_url_anchor in cat_url_elem_list:
                cat_url = 'https://www.farfetch.com' + cat_url_anchor.xpath('.//@href')[0]
                cat_name = cat_url_anchor.xpath('.//text()')[0]
                cat_url_list.append({
                    'cat_url': cat_url,
                    'cat_name': cat_name
                })

        def get_sex(url_string):
            if 'women' in url_string:
                return 'women'
            elif 'men' in url_string:
                return 'men'
            else:
                return None

        adult_cat_url_list = [{
            'cat_url': cat_dict['cat_url'],
            'cat_name': cat_dict['cat_name'],
            'sex': get_sex(cat_dict['cat_url'])
        } for cat_dict in cat_url_list if get_sex(cat_dict['cat_url']) is not None]

        for cat_url_name in adult_cat_url_list:
            yield scrapy.Request(
                url=cat_url_name['cat_url'],
                callback=self.product_collection,
                meta={
                    'cat_name': cat_url_name['cat_name'],
                    'sex': cat_url_name['sex']
                }
            )

    # Collect product URLs in each category
    def product_collection(self, response):
        cat_name = response.meta['cat_name']
        sex = response.meta['sex']

        prod_tiles = response.xpath('.//li[@data-test="productCard"]')
        prod_list = []
        for prod_tile in prod_tiles:
            prod_url = prod_tile.xpath('.//a[@itemprop="itemListElement"]/@href')
            prod_name = prod_tile.xpath('.//p[@data-test="productDescription"]/text()')
            price_match = prod_tile.xpath('.//span[@data-test="price"]/text()')
            initial_price = prod_tile.xpath('.//span[@data-test="initialPrice"]/text()')
            sale = False
            # price = None
            saleprice = None
            if len(initial_price) > 0:
                sale = True
                price = initial_price[0]
                saleprice = price_match[0]
            else:
                price = price_match[0]
            brand = prod_tile.xpath('.//h3[@data-test="productDesignerName"]/text()')

            prod_list.append({
                'name': prod_name[0].title(),
                'prod_url': 'https://www.farfetch.com' + prod_url[0],
                'price': price,
                'sale': sale,
                'saleprice': saleprice,
                'brand': brand[0]
            })

        for prod_dict in prod_list:
            print('Product URL scraped: ', str(prod_dict['prod_url']))
            yield scrapy.Request(
                url=prod_dict['prod_url'],
                callback=self.parse,
                meta={
                    'cat_name': cat_name,
                    'sex': sex,
                    'name': prod_dict['name'],
                    'prod_url': prod_dict['prod_url'],
                    'price': prod_dict['price'],
                    'sale': prod_dict['sale'],
                    'saleprice': prod_dict['saleprice'],
                    'brand': prod_dict['brand']
                }
            )

        next_page_match = response.xpath('.//link[@rel = "next"]/@href')
        if len(next_page_match) > 0:
            next_page = next_page_match[0]
            yield scrapy.Request(
                url=next_page,
                callback=self.product_collection,
                meta={
                    'cat_name': cat_name,
                    'sex': sex
                }
            )

    # Scrape the product page
    def parse(self, response):
        item = FarfetchItem()

        item['category'] = response.meta['cat_name']
        item['shop'] = 'Farfetch'
        item['currency'] = '£'
        item['sex'] = response.meta['sex']
        item['name'] = response.meta['name']
        item['prod_url'] = response.meta['prod_url']
        item['price'] = response.meta['price']
        item['saleprice'] = response.meta['saleprice']
        item['sale'] = response.meta['sale']
        item['brand'] = response.meta['brand']

        item['date'] = int(time.time())

        prod_json_string = re.search('(?<=__initialState_slice-pdp__\'\]\ \=\ ).*?(?=\<\/script)', response.text)
        prod_json = json.loads(prod_json_string.group(0))
        item['color_string'] = prod_json['productViewModel']['designerDetails']['designerColour'].split(' ')[-1].lower()

        img_list = prod_json['productViewModel']['images']['main']
        item['image_urls'] = [img_dict['600'] for img_dict in img_list]
        img_strings = item['image_urls']
        item['image_hash'] = []
        for img_string in img_strings:
            # Check if image string is a string, if not then do not pass this item
            if isinstance(img_string, str):
                # print(img_string)
                hash_object = hashlib.sha1(img_string.encode('utf8'))
                hex_dig = hash_object.hexdigest()
                item['image_hash'].append(hex_dig)

        item['description'] = prod_json['productViewModel']['details']['description']
        item['size_stock'] = [{
            'size': value['description'],
            'stock': 'In stock'
        } for key, value in prod_json['productViewModel']['sizes']['available'].items()]

        if isinstance(response.meta['prod_url'], str):
            prod_id_hash_object = hashlib.sha1(response.meta['prod_url'].encode('utf8'))
            prod_id_hex_dig = prod_id_hash_object.hexdigest()
            item['prod_id'] = prod_id_hex_dig

        yield item
