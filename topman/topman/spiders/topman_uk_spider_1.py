import scrapy
from topman.items import TopmanItem
import hashlib
import time
import re
import json
import requests


class TopmanSpider(scrapy.Spider):
    name = "topman_spider"

    # Main start function
    def start_requests(self):
        url = 'https://www.topman.com/en/tsuk/'

        yield scrapy.Request(url=url, callback=self.category_collection)

    def category_collection(self, response):
        cat_urls_matches = response.xpath(
            './/div[@class="HeaderTopman-navigation"]//a[contains(@href, "/tmuk/category/")]'
        )
        for cat_urls_match in cat_urls_matches:
            cat_url = cat_urls_match.xpath('@href')
            cat_name = cat_urls_match.xpath('text()')

            yield scrapy.Request(
                url=f'https://www.topman.com{cat_url.extract_first()}',
                callback=self.product_collection,
                meta={
                    'cat_name': cat_name.extract_first(),
                    'cat_url': f'https://www.topman.com{cat_url.extract_first()}'
                }
            )

    def product_collection(self, response):
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,lv;q=0.8',
            'cache-control': 'no-cache',
            'cookie': 'bm_sz=787EAD0F7C4B225BF89B711F99FC89C5~YAAQHbsQAh5ii6BuAQAA0v+cfwZh/2+rK6QYlP5kHEdEBDM8UM/DUOjum4mQWBA/BbeklrnTB/86xdMY4PSRCNZBBF7C9NKvwlZ3fHyG/J42OJQoOPeUdJfadY9SOX6ILzVD92mZodCcYAhGwe+QVUg3vJPYk0G956NRlrEJtF31Ms23jyR58D66NUAr35aCDQ==; _blka_uab=45; deviceType=desktop; _gcl_au=1.1.1244171170.1578394001; new_returning_customer=N1578394001429; userId=unspecified; _abck=6AC9134EEEDD2D7AE5099E9C22EE768E~0~YAAQHbsQAihji6BuAQAANiCdfwNHUmtwplCnsbjbaz5zPKusBrSHXgcivEk6/g9QpGdPbpqsAF4qjSIPmokYJM0ypiY2k4O3vdUZeJ/ewBXJ9/IaT/Q8+T7Sz1H4gvyMAauecWKMhRPVH6jmbVBk2209eNkh7sx+ilveRDDHLWTVuSrBcTBzaiLwhhW9JN0T69xf96ASo/5MZRsFIsWDN/knK5T2TWHn3YEkPR8QR0/e1Nd/Jq8m36m7yxVwLkz7qdMizv4CBZnX7KhvGeJrDO09JP+t14CQUWNMSESYPoIJmc/4mMSStxDoldOXczsDBImAMnjFkNw=~-1~-1~-1; peerius_sess=119866084813|942GKDdVZ6xjEW4J4bhAZ2mU8Rb4It0apWMlFz2AyDw; peerius_user=cuid:75168310513|XrYjIeIX2j24alXNkcRSl13Lx16NrZBwJjjCC1Hy1oc; _ga=GA1.2.1493720660.1578394002; _gid=GA1.2.641844300.1578394002; _scid=3ea60883-2f67-41d9-974a-332e2c6b8117; ak_bmsc=8ECA00B9D479C686BA6CE77EB26630FA0210BB1D2A4900008961145ECB7F1234~plxjHWaSPdS0Sgu4BO2BGI4xzERD5EP1Za8vRcYtnM0KUmDcEfVJAjGjmlFBy9GKo+4aVF4ByZ0KDfypjhlJzL2snM8EiE95wmU1H6ImcXcN//yP/YVplYUrXSF8LgvTbIxVsZqAOXYr7wqiX6FEWpCa5IkNUkalt5TLe4g8T4+4Acw+jmtcCJlFdBnyyw6bTr0mJJ6qibFIZLof26FCvgqPRKmzn+gU9ddWOiVY9bT+IMqk8aa+vrl/hOeiwqqJOF; _derived_epik=dj0yJnU9UXA0XzZndG9sSDJRMXpNbFpOWmprY2IteDRtQTI3N1Embj1VWFB6NHdBMnFLVjVRS0FQVmx6UnZBJm09MSZ0PUFBQUFBRjRVWVpJJnJtPTEmcnQ9QUFBQUFGNFVZWkk; _hjid=e3aa1902-572f-4ea2-862e-a7d1830aebc3; TLTSID=58864215198174902923825843741217; GEOIP=GB; source=CoreAPI; tempsession=true; notice_preferences=3:; notice_gdpr_prefs=0,1,2,3::implied,eu; cmapi_gtm_bl=; cmapi_cookie_privacy=permit 1,2,3,4; traceId2=1578394027951R595981; __exponea_etc__=0d2ecee1-313b-11ea-b2a8-8ab630c69043; __exponea_time2__=0.015987873077392578; jsessionid=eyJhbGciOiJIUzI1NiJ9.MTUzZDBlZjQtZGZhMS00Y2Y5LWJjNjItNmI2NWFhODJjZDc5.K3x5SjKL3abM92smNYMnUkKNBYhhAq2b4Q7LJPdKnNc; akavpau_VP_TS=1578394465~id=5fac10c37cd36703cbb2000288f6f8d0; bm_sv=B6C97F78E03F9A83BF7464E129AD5F46~0HJ1r15DcLZnrMxbNou2xo+OjsG/B0QkvQiRwUM3uhyOgQa0j/dfkEkNPPX5mr9hvOiimXwvdZRcNj6FQCR52dUsd6lIwFV0Q+C63WkGUK+9psK3UzES9TlWTnjQEs33bkKqPsQh6FnWMW03nPOHq8O1j1SMQJ/ePXxl6gUF87M=; _dc_gtm_UA-99206402-1=1',
            'pragma': 'no-cache',
            'referer': 'https://www.topman.com/',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
            'brand-code': 'tmuk'
        }

        breadcrumbs_string = re.search('(?<=\"breadcrumbs\"\:\[).*?(?=\])', response.text)
        cat_id_match = re.findall('(?<=category\"\:\").*?(?=\")', breadcrumbs_string.group(0))
        cat_id = cat_id_match[1]

        first_api_request_url = f'https://www.topman.com/api/products?currentPage=1&pageSize=24&category={cat_id}'
        first_api_request = requests.get(first_api_request_url, headers=headers)
        first_api_req_json = json.loads(first_api_request.text)
        prod_count = first_api_req_json['totalProducts']
        page_count = int(prod_count / 24)

        for i in range(0, page_count):
            print(f'page: {i + 1}')
            req_url = f'https://www.topman.com/api/products?currentPage={i + 1}&pageSize=24&category={cat_id}'
            api_request = requests.get(req_url, headers=headers)
            response_json = json.loads(api_request.text)
            response_prods = response_json['products']
            for response_prod in response_prods:
                prod_name = response_prod['name']
                current_price = float(response_prod['unitPrice'])
                try:
                    was_price = float(response_prod['wasPrice'])
                except:
                    was_price = None
                sale = was_price is not None
                if sale:
                    price = was_price
                    saleprice = current_price
                else:
                    price = current_price
                    saleprice = None

                prod_url = f'https://www.topman.com{response_prod["productUrl"]}'

                yield scrapy.Request(
                    url=prod_url,
                    callback=self.parse,
                    meta={
                        'cat_name': response.meta['cat_name'],
                        'cat_url': response.meta['cat_url'],
                        'prod_name': prod_name,
                        'prod_url': prod_url,
                        'price': price,
                        'saleprice': saleprice,
                        'sale': sale
                    }
                )

    def parse(self, response):
        item = TopmanItem()

        item['shop'] = 'Top Man'
        item['name'] = response.meta['prod_name']
        item['price'] = response.meta['price']
        item['saleprice'] = response.meta['saleprice']
        item['sale'] = response.meta['sale']
        item['prod_url'] = response.meta['prod_url']

        if isinstance(response.meta['prod_url'], str):
            prod_id_hash_object = hashlib.sha1(response.meta['prod_url'].encode('utf8'))
            prod_id_hex_dig = prod_id_hash_object.hexdigest()
            item['prod_id'] = prod_id_hex_dig

        prod_info_string_match = re.search('(?<=window\.__INITIAL_STATE__\=).*?(?=window\.version\=\{)', response.text,
                                           re.I | re.DOTALL)
        prod_info_string = prod_info_string_match.group(0).strip()[:-1]
        prod_info_json = json.loads(prod_info_string)

        item['color_string'] = prod_info_json['currentProduct']['colour'].lower()
        item['description'] = prod_info_json['currentProduct']['description']

        image_list = prod_info_json['currentProduct']['assets']
        img_index_list = []
        img_urls = []
        for img_slug_dict in image_list:
            img_index = img_slug_dict['index']
            if img_index not in img_index_list:
                img_index_list.append(img_index)
                img_slug = img_slug_dict['url']
                img_slug_split = img_slug.split('?$')
                img_url = f'{img_slug_split[0]}?$w1000$&fmt=jpg&qlt=80'
                img_urls.append(img_url)
        item['image_urls'] = img_urls

        img_strings = item['image_urls']
        item['image_hash'] = []
        for img_string in img_strings:
            # Check if image string is a string, if not then do not pass this item
            if isinstance(img_string, str):
                hash_object = hashlib.sha1(img_string.encode('utf8'))
                hex_dig = hash_object.hexdigest()
                item['image_hash'].append(hex_dig)

        size_list = prod_info_json['currentProduct']['items']
        size_stock = [{
            'size': size_dict['size'],
            'stock': size_dict['stockText']
        } for size_dict in size_list]
        item['size_stock'] = size_stock
        in_stock_sizes = [size_dict for size_dict in size_stock if size_dict['stock'] == 'In stock']
        if len(in_stock_sizes) > 0:
            item['in_stock'] = True
        else:
            item['in_stock'] = False

        item['sex'] = 'men'
        item['brand'] = 'Top Man'
        item['currency'] = 'GBP'
        item['date'] = int(time.time())
        item['category'] = response.meta['cat_name']

        yield item
