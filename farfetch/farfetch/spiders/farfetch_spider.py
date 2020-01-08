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
        url = 'https://www.farfetch.com/uk/'

        yield scrapy.Request(url=url, callback=self.category_collection)

    # Go through category links
    def category_collection(self, response):
        def get_sex(url_string):
            if 'women' in url_string:
                return 'women'
            elif 'men' in url_string:
                return 'men'
            else:
                return None

        cat_url_els = response.xpath('.//ul[contains(@class, "ff-primary-nav")]//a[contains(@class, "ff-nav-a")]')

        cat_urls = []
        for cat_url_el in cat_url_els:
            cat_url_match = cat_url_el.xpath('@href').extract_first()
            if len(cat_url_match.split('?')) > 1:
                cat_url = f'https://www.farfetch.com{cat_url_match.split("?")[0]}'
            else:
                cat_url = f'https://www.farfetch.com{cat_url_match}'
            cat_name = cat_url_el.xpath('text()').extract_first().strip()
            cat_sex = get_sex(cat_url)
            if len(cat_name) > 0 and cat_sex is not None:
                print(f'CAT URL: {cat_url}')
                cat_urls.append({
                    'url': cat_url,
                    'name': cat_name,
                    'sex': cat_sex
                })

        for cat_url_dict in cat_urls:
            yield scrapy.Request(
                url=cat_url_dict['url'],
                callback=self.product_collection,
                meta={
                    'cat_name': cat_url_dict['name'],
                    'sex': cat_url_dict['sex']
                }
            )

    # Collect product URLs in each category
    def product_collection(self, response):
        cat_name = response.meta['cat_name']
        sex = response.meta['sex']

        prod_tiles = response.xpath('.//li[@data-test="productCard"]')
        prod_list = []
        for prod_tile in prod_tiles:
            prod_url = prod_tile.xpath('.//a[@itemprop="itemListElement"]/@href').extract_first()
            prod_name = prod_tile.xpath('.//p[@data-test="productDescription"]/text()').extract_first()
            price_match = prod_tile.xpath('.//span[@data-test="price"]/text()').extract_first()
            initial_price = prod_tile.xpath('.//span[@data-test="initialPrice"]/text()').extract_first()
            sale = False
            # price = None
            saleprice = None
            if initial_price is not None:
                sale = True
                price = initial_price
                saleprice = price_match.replace('£', '')
                saleprice = float(saleprice.replace(',', ''))
            else:
                price = price_match
            brand = prod_tile.xpath('.//h3[@data-test="productDesignerName"]/text()').extract_first()

            price = price.replace(',', '')

            prod_list.append({
                'name': prod_name.title(),
                'prod_url': 'https://www.farfetch.com' + prod_url,
                'price': float(price.replace('£', '')),
                'sale': sale,
                'saleprice': saleprice,
                'brand': brand
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

        next_page_match = response.xpath('.//link[@rel = "next"]/@href').extract_first()
        if next_page_match is not None:
            next_page = next_page_match
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
        image_urls_list = [img_dict['600'] for img_dict in img_list]
        if len(image_urls_list) > 4:
            item['image_urls'] = image_urls_list[:4]
        else:
            item['image_urls'] = image_urls_list

        img_strings = item['image_urls']
        item['image_hash'] = []
        for img_string in img_strings:
            # Check if image string is a string, if not then do not pass this item
            if isinstance(img_string, str):
                hash_object = hashlib.sha1(img_string.encode('utf8'))
                hex_dig = hash_object.hexdigest()
                item['image_hash'].append(hex_dig)

        item['description'] = prod_json['productViewModel']['details']['description']
        item['size_stock'] = [{
            'size': value['description'],
            'stock': 'In stock'
        } for key, value in prod_json['productViewModel']['sizes']['available'].items()]
        if len(item['size_stock']) > 0:
            item['in_stock'] = True
        else:
            item['in_stock'] = False

        if isinstance(response.meta['prod_url'], str):
            prod_id_hash_object = hashlib.sha1(response.meta['prod_url'].encode('utf8'))
            prod_id_hex_dig = prod_id_hash_object.hexdigest()
            item['prod_id'] = prod_id_hex_dig

        yield item
