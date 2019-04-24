import scrapy
from scrapy.selector import Selector
from hm.items import HmItem
import hashlib
import re
import requests
import json
import datetime
# from urllib.parse import urlparse
import math


class HmSpider(scrapy.Spider):
    name = "hm_spider_uk"

    # The main start function which initializes the scraping URLs and triggers parse function
    def start_requests(self):
        urls = [
            {
                'url': 'https://www2.hm.com/en_gb/ladies.html',
                'sex': 'women',
                'api_prefix': 'ladies'
            },
            {
                'url': 'https://www2.hm.com/en_gb/men.html',
                'sex': 'men',
                'api_prefix': 'men'
            }
        ]
        for url in urls:
            yield scrapy.Request(
                url=url['url'],
                callback=self.get_cat_urls,
                meta={
                    'sex': url['sex'],
                    'api_prefix': url['api_prefix']
                }
            )

    def get_cat_urls(self, response):
        links = Selector(response).xpath('.//a[@role="menuitem"]')
        print(f'links: {links}')

        for link in links:
            cat_url = link.xpath("./@href").extract_first()
            if len(cat_url.split('hm.com')) != 2:
                cat_url = f'https://www2.hm.com{cat_url}'
            print(f'Cat URL: {cat_url}')
            cat_name = link.xpath('./text()').extract_first()
            cat_name = ''.join(ch for ch in cat_name if ch.isalnum())
            print(f'Cat name: {cat_name}')
            cat_api_regex = re.search('\/(?:.(?!\/))+$', cat_url)
            api_regex = re.search(r'(?<=\/).*?(?=\.html?)', cat_api_regex.group(0))
            print(f'API slug: {api_regex.group(0)}')
            api_slug = api_regex.group(0)

            yield scrapy.Request(
                url=cat_url,
                callback=self.infinite_requests,
                meta={
                    'cat_name': cat_name,
                    'sex': response.meta['sex'],
                    'api_prefix': response.meta['api_prefix'],
                    'api_slug': api_slug,
                    'cat_url': cat_url
                }
            )

    def infinite_requests(self, response):
        count_slug_array = response.meta['api_slug'].split('-')
        count_slug_array = [word for word in count_slug_array if word not in ['and']]
        count_slug = ''.join(count_slug_array)
        count_check_slug = f'{response.meta["api_prefix"]}_{count_slug}'

        long_api_slug = re.search(r'(?<=data\-filtered\-products\-url\=\").*?(?=\")', response.text)
        if long_api_slug is not None:
            print('---------------------------------------------------------')
            print(f'infinite_requests API slug: {response.meta["api_slug"]}')
            print(f'infinite_requests API check slug: {count_check_slug}')
            print(f'infinite_requests CAT URL: {response.meta["cat_url"]}')
            if len(response.meta["cat_url"].split('new-arrivals')) == 2:
                count_check_url = f'https://www2.hm.com{long_api_slug.group(0)}?sort=stock&image-size=large&image=model&offset=0&page-size=36'
            elif len(response.meta["cat_url"].split('shop-by-occasion')) == 2:
                count_check_url = f'https://www2.hm.com{long_api_slug.group(0)}?sort=stock&image-size=large&image=model&offset=0&page-size=36'
            else:
                count_check_url = f'https://www2.hm.com{long_api_slug.group(0)}?product-type={count_check_slug}&sort=stock&image-size=large&image=model&offset=0&page-size=36'
            print(count_check_url)

            count_check_response = requests.get(count_check_url)
            if count_check_response.status_code == 200:
                count_check_dict = json.loads(count_check_response.text)
                if len(count_check_dict) > 0:
                    prod_count = count_check_dict['total']
                    page_count = int(math.ceil(prod_count / 36))

                    for i in range(0, page_count):
                        print(f'offset = {i * 36}')
                        if len(response.meta["cat_url"].split('new-arrivals')) == 2:
                            get_prod_url = f'https://www2.hm.com{long_api_slug.group(0)}?sort=stock&image-size=large&image=model&offset={i * 36}&page-size=36'
                        elif len(response.meta["cat_url"].split('shop-by-occasion')) == 2:
                            get_prod_url = f'https://www2.hm.com{long_api_slug.group(0)}?sort=stock&image-size=large&image=model&offset={i * 36}&page-size=36'
                        else:
                            get_prod_url = f'https://www2.hm.com{long_api_slug.group(0)}?product-type={count_check_slug}&sort=stock&image-size=large&image=model&offset={i * 36}&page-size=36'

                        print(get_prod_url)
                        get_prod_response = requests.get(get_prod_url)
                        if get_prod_response.status_code == 200:
                            get_prod_dict = json.loads(get_prod_response.text)

                            prod_array = get_prod_dict['products']
                            for prod in prod_array:
                                prod_url = prod['link']
                                prod_id = prod['articleCode']
                                sale_price = prod['redPrice']
                                if len(sale_price) == 0:
                                    sale_price = prod['yellowPrice']
                                swatches = prod['swatches']
                                current_swatch = [swatch for swatch in swatches if swatch['articleLink'] == prod_url]
                                color_string = current_swatch[0]['colorName']
                                color_hex = current_swatch[0]['colorCode']

                                yield scrapy.Request(
                                    url=f'https://www2.hm.com{prod_url}',
                                    callback=self.prod_parse,
                                    meta={
                                        'cat_name': response.meta['cat_name'],
                                        'sex': response.meta['sex'],
                                        'name': prod['title'],
                                        'price': prod['price'],
                                        'sale': prod['showPriceMarker'],
                                        'sale_price': sale_price,
                                        'prod_url': f'https://www2.hm.com{prod_url}',
                                        'prod_id': prod_id,
                                        'color_string': color_string,
                                        'color_hex': color_hex
                                    }
                                )

    def prod_parse(self, response):
        item = HmItem()
        item['name'] = response.meta['name']
        item['price'] = response.meta['price']
        item['prod_url'] = response.meta['prod_url']
        item['sale'] = response.meta['sale']
        item['saleprice'] = response.meta['sale_price']
        item['sex'] = response.meta['sex']
        item['category'] = response.meta['cat_name']
        item['shop'] = 'H&M'
        item['color_string'] = response.meta['color_string']
        item['color_hex'] = response.meta['color_hex']
        
        # main_img_re = './/div[@class="product-detail-main-image-container"]/img/@src'
        formatted_text = response.text.replace('"', '\'')
        js_match = re.search('(?<=productArticleDetails\ =\ )[\s\S]*(?=\;)', formatted_text)
        prod_match = re.search(f'(?<=\'{response.meta["prod_id"]}\'\:\ )[\s\S]*(?=\,\n)', js_match.group(0))
        images_string_match = re.search('(?<=\'images\'\:\[)[\s\S]*?(?=\]\,\n)', prod_match.group(0))
        if images_string_match is not None:
            img_slug_match = re.findall('(?<=fullscreen\'\:\ isDesktop\ \?\ \').*?(?=\'\ \:)', images_string_match.group(0))
            item['image_urls'] = [f'https:{img_slug}' for img_slug in img_slug_match]
        else:
            MAIN_IMG_SELECTOR = './/div[@class="product-detail-main-image-container"]/img/@src'
            main_img_arr = response.xpath(MAIN_IMG_SELECTOR).extract()
            item['image_urls'] = [f'https:{img_url}' for img_url in main_img_arr]

        sizes_match = re.search('(?<=\'sizes\'\:\[)[\s\S]*?(?=\]\,)', prod_match.group(0))
        size_name_match = re.findall('(?<=\"name\"\:\ \")[\S]*?(?=\")', sizes_match.group(0))
        sizes_stock = [{
            'stock': 'In stock',
            'size': size
        } for size in size_name_match]
        item['size_stock'] = sizes_stock

        item['image_hash'] = []
        for img_string in item['image_urls']:
            # Check if image string is a string, if not then do not pass this item
            if isinstance(img_string, str):
                hash_object = hashlib.sha1(img_string.encode('utf8'))
                hex_dig = hash_object.hexdigest()
                item['image_hash'].append(hex_dig)

        item['date'] = int(datetime.datetime.now().timestamp())
        item['currency'] = 'GBP'
        item['brand'] = 'H&M'

        DESCRIPTION_SELECTOR = './/p[contains(@class, "pdp-description-tex")]/text()'
        item['description'] = response.xpath(DESCRIPTION_SELECTOR).extract_first()

        yield item
