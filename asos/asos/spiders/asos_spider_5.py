import scrapy
from asos.items import AsosItem
import hashlib
import re
import requests
import json
import time
import random


class AsosSpider(scrapy.Spider):
    name = "asos_spider_uk_1"

    # The main start function which initializes the scraping URLs and triggers parse function
    def start_requests(self):
        urls = [
            'https://www.asos.com/women/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.get_cat_urls)

    def get_cat_urls(self, response):
        def get_sex(url_string):
            women_check = len(url_string.split('women')) == 2
            if women_check == True:
                return 'women'
            else:
                men_check = len(url_string.split('men')) == 2
                if men_check == True:
                    return 'men'
                else:
                    return None

        cat_urls = response.xpath('.//nav[@data-testid="primarynav-large"]/div/div//div[@data-testid="secondarynav-flyout"]/section/div/ul/li/a/@href').extract()
        cat_names = response.xpath('.//nav[@data-testid="primarynav-large"]/div/div//div[@data-testid="secondarynav-flyout"]/section/div/ul/li/a/text()').extract()
        cat_urls_names_sex = [{
            'url': cat_url,
            'sex': get_sex(cat_url),
            'cat_name': cat_names[cat_urls.index(cat_url)]
        } for cat_url in cat_urls]
        cat_urls_sex_filtered = list(filter(lambda x: x['sex'] is not None, cat_urls_names_sex))

        for cat_url_dict in cat_urls_sex_filtered:
            yield scrapy.Request(
                url=cat_url_dict['url'],
                callback=self.get_prod_urls,
                meta={
                    'cat_name': cat_url_dict['cat_name'],
                    'sex': cat_url_dict['sex'],
                    'cat_url': cat_url_dict['url']
                }
            )

    def get_prod_urls(self, response):
        store_version_match = response.xpath('.//div[@id="myaccount-dropdown"]/div/div/div/div/span/a/@href').extract()
        store_version = store_version_match[0].split('keyStoreDataversion=')[1]
        referer = response.meta['cat_url'].replace('+', '%20')
        cat_id_match = re.search('(?<=cid\=).*?(?=&)', response.meta['cat_url'])
        cat_id = cat_id_match.group(0)
        user_agents = [
            ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 '
             'Safari/537.36'),  # chrome Win10
            ('Mozilla/5.0 (X11; Linux x86_64) '
             'AppleWebKit/537.36 (KHTML, like Gecko) '
             'Chrome/61.0.3163.79 '
             'Safari/537.36'),  # chrome
            ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) '
             'Gecko/20100101 '
             'Firefox/55.0'),  # firefox
            ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
             '(KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'),
            ('Mozilla/5.0 (X11; Linux x86_64) '  # Chrome 72.0 Win10
             'AppleWebKit/537.36 (KHTML, like Gecko) '
             'Chrome/61.0.3163.91 '
             'Safari/537.36'),  # chrome
            ('Mozilla/5.0 (X11; Linux x86_64) '
             'AppleWebKit/537.36 (KHTML, like Gecko) '
             'Chrome/62.0.3202.89 '
             'Safari/537.36'),  # chrome
            ('Mozilla/5.0 (X11; Linux x86_64) '
             'AppleWebKit/537.36 (KHTML, like Gecko) '
             'Chrome/63.0.3239.108 '
             'Safari/537.36'),  # chrome
            ('Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0)'
             ' Gecko/20100101 Firefox/65.0'),
            ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
             'Chrome/72.0.3626.119 Safari/537.36'),
            ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
             'Chrome/72.0.3626.96 Safari/537.36'),
            ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 '
             '(KHTML, like Gecko) Version/12.0.3 Safari/605.1.15'),
            ('Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) '
             'Gecko/20100101 Firefox/65.0'),
            ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) '
             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'),
            ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) '
             'Gecko/20100101 Firefox/65.0'),
            ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) '
             'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.2 Safari/605.1.15'),
            ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 '
             '(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')
        ]
        api_headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Cache-Control': 'no-cache',
            'pragma': 'no-cache',
            'Host': 'api.asos.com',
            'Origin': 'https://www.asos.com/',
            'Referer': referer,
            'upgrade-insecure-requests': '1',
            'user-agent': random.choice(user_agents)
        }

        api_req_count = requests.get(
            f'https://api.asos.com/product/search/v1/categories/{cat_id}?channel=desktop-web&country=GB&currency=GBP&keyStoreDataversion={store_version}&lang=en&limit=72&offset=0&rowlength=4&store=1',
            headers=api_headers
        )
        api_count_json = json.loads(api_req_count.text)
        item_count = api_count_json['itemCount']
        page_count = int(item_count / 72)

        for page_nr in range(1, page_count):
            api_req = requests.get(
                f'https://api.asos.com/product/search/v1/categories/{cat_id}?channel=desktop-web&country=GB&currency=GBP&keyStoreDataversion={store_version}&lang=en&limit=72&offset={page_nr * 72}&rowlength=4&store=1',
                headers=api_headers
            )
            api_json = json.loads(api_req.text)
            api_products = api_json['products']

            for product in api_products:
                name = product['name']
                price_dict = product['price']
                sale_check = 'isMarkedDown' in price_dict
                if sale_check == True:
                    sale = price_dict['isMarkedDown']
                    if sale == True:
                        saleprice = price_dict['current']['value']
                        price = price_dict['previous']['value']
                    else:
                        saleprice = None
                        price = price_dict['current']['value']
                else:
                    sale = False
                    saleprice = None
                    price = price_dict['current']['value']

                brand = product['brandName']
                color_string = product['colour']
                prod_url = f'https://www.asos.com/{product["url"]}'

                yield scrapy.Request(
                    url=prod_url,
                    callback=self.parse,
                    meta={
                        'cat_name': response.meta['cat_name'],
                        'sex': response.meta['sex'],
                        'name': name,
                        'sale': sale,
                        'saleprice': saleprice,
                        'price': price,
                        'brand': brand,
                        'color_string': color_string,
                        'prod_url': prod_url
                    }
                )

    def parse(self, response):
        item = AsosItem()
        item['shop'] = 'Asos'
        item['name'] = response.meta['name']
        item['price'] = response.meta['price']
        item['saleprice'] = response.meta['saleprice']
        item['sale'] = response.meta['sale']
        item['prod_url'] = response.meta['prod_url']
        item['sex'] = response.meta['sex']
        item['brand'] = response.meta['brand']
        item['date'] = int(time.time())
        item['currency'] = '£'
        item['color_string'] = response.meta['color_string']
        item['category'] = response.meta['cat_name']

        description_match = response.xpath('.//div[@class="product-description"]//ul/li/text()').extract()
        item['description'] = '\n'.join(description_match)

        if isinstance(response.meta['prod_url'], str):
            prod_id_hash_object = hashlib.sha1(response.meta['prod_url'].encode('utf8'))
            prod_id_hex_dig = prod_id_hash_object.hexdigest()
            item['prod_id'] = prod_id_hex_dig

        img_urls_match = re.search('(?<=\"images\"\:\[).*?(?=\])', response.text)
        img_urls_json = json.loads(f'[{img_urls_match.group(0)}]')
        img_urls = [img_dict['url'] for img_dict in img_urls_json]
        item['image_urls'] = [f'{img_url}?$XXL$&wid=800&fit=constrain' for img_url in img_urls]

        # Calculate SHA1 hash of image URL to make it easy to find the image based on hash entry and vice versa
        img_strings = item['image_urls']
        item['image_hash'] = []
        for img_string in img_strings:
            # Check if image string is a string, if not then do not pass this item
            if isinstance(img_string, str):
                # print(img_string)
                hash_object = hashlib.sha1(img_string.encode('utf8'))
                hex_dig = hash_object.hexdigest()
                item['image_hash'].append(hex_dig)

        info_json_match = re.search(
            '(?<=window.asos.pdp.config.product = ).*?(?=window.asos.pdp.config.translations)',
            response.text, re.I | re.DOTALL)
        info_json = json.loads(info_json_match.group(0).strip()[:-1])
        item['size_stock'] = [{
            'size': size_dict['size'],
            'stock': 'In stock'
        } for size_dict in info_json['variants']]
        if len(item['size_stock']) > 0:
            item['in_stock'] = True
        else:
            item['in_stock'] = False

        yield item
