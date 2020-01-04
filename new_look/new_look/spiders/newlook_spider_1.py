import scrapy
from new_look.items import NewLookItem
import hashlib
import re
import requests
# import json
import datetime
# import random
import time


class ZaraSpider(scrapy.Spider):
    name = "zara_spider_uk_1"

    # The main start function which initializes the scraping URLs and triggers parse function
    def start_requests(self):
        urls = [
            'https://www.newlook.com/uk/sitemap'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.get_prod_urls)

    def get_prod_urls(self, response):
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,lv;q=0.8',
            'cookie': 'JSESSIONID=CB3AFFEB6ECE9AC7852730644608A8ED.app53-se; NL_LOCALE2=en_GB_NewLook; ens_lastClick=seo; AMCVS_208B22CE52784ABC0A490D4D%40AdobeOrg=1; 54190=; AMCV_208B22CE52784ABC0A490D4D%40AdobeOrg=1406116232%7CMCIDTS%7C18009%7CMCMID%7C56529088119221786800858791027136777586%7CMCAAMLH-1556564406%7C6%7CMCAAMB-1556564406%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1555966806s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C2.5.0; ensNLVisitorID=56529088119221786800858791027136777586; s_cc=true; newlookCookieConsent=true; 55767=; 51935=; 51854=not-found; _ga=GA1.2.462363415.1555959616; _gid=GA1.2.2027162352.1555959616; nGroup=B; _fbp=fb.1.1555959639579.340522315; _caid=e9b86c3b-c4e7-4bf8-9a2a-1f7f818ab311; _cavisit=16a466bf038|; _scid=7ff4b70c-560b-458d-bdcf-e1f76a55a1ed; _hjIncludedInSample=1; __zlcmid=rwiBLxtz0jdovE; newlookSessionData="YpL7BCcU4xeIhzx0RprTOCuZZOMcLSbNOWhGJXMCjBUmW430idRInNwXMDRYcY2L3VB8LfN4GsNQQitWF3BgE0C7Y0HiMnbnSc9KCA57DG//1APizMn7NTlzMFsvePiEyoapS2WI7CkOUkUm3TRsrRYEYVOoDHbX2xvQdv9NuBEmcu2MyNdA7rd7LmcwornoDEJqqTUZ7PzeE0VmSpWiLi8Ly9SIMaRmh6h+LbTVVx/HkhFXu0DPgvMjRO8j7y2hsakks7i/gN2Zw/s2sHGR8/kDikQCOXfqBL5OEwpUKCrk0Aq3AMGsA6XDlwVqHN71RYjRNcx1HPaERMv06TJr/06XFPd/mz1mpJyClN9j8zjDFK2k6E1ThQgqzU1ZuTh/GqzdvY4F94noFIgv3OAiM3+so8pUmN4G9TOxX5JrUB82io5jo4Ej2qh4lszQocGM9wmlWOEjM8MENFyIFya9w7UyuQjgIa7VPoCe4AfqL8dg+Vn+1l5eUkX9n73OvjVUIK0poI/q+nSFIy5cPuUDPA=="; sc_pp_path_15=%2Fuk%2Fwomens%2Fclothing%2Fc%2Fuk-womens-clothing; sc_pp_v15=no%20value; sc_pp_path_16=%2Fuk%2Fwomens%2Fclothing%2Fc%2Fuk-womens-clothing; sc_pp_c16=uk%3Ac%3Auk-womens-clothing; s_sq=%5B%5BB%5D%5D; BVImplmain_site=14268; Current_unit_Amount=product0%3A626808579-style_code_units%3Dundefined%2Cproduct1%3A619000670-style_code_units%3Dundefined%2Cproduct2%3A628400049-style_code_units%3Dundefined%2Cproduct3%3A627355713-style_code_units%3Dundefined%2Cproduct4%3A620597539-style_code_units%3Dundefined%2Cproduct5%3A628130601-style_code_units%3Dundefined%2Cproduct6%3A620914029-style_code_units%3Dundefined%2Cproduct7%3A617368045-style_code_units%3Dundefined%2Cproduct8%3A623697572-style_code_units%3Dundefined%2Cproduct9%3A628264301-style_code_units%3Dundefined; sc_pp_v15a=ProductGridPageTemplate; mmapi.store.p.0=%7B%22mmparams.d%22%3A%7B%7D%2C%22mmparams.p%22%3A%7B%22pd%22%3A%221587495718764%7C%5C%22422912341%7CFwAAAApVAwBcXCC7jhF5lgABEQABQkDoRIsBAGyIPP9Ux9ZIFjyGvVTH1kgAAAAAAQAAAP%2F%2F%2F%2F8ADnd3dy5nb29nbGUuY29tBI4RAQAAAAAAAAAAAItVAgD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwUARvwAABBaT4xKjhEA%2F%2F%2F%2F%2FwGOEY4R%2F%2F8GAAABAAAAAAEwegIAPCMDAAB9DgEAUpR4sdWOEQD%2F%2F%2F%2F%2FAY4RjhH%2F%2FwMAAAEAAAAAAQGoAgBCXQMAACgQAQCCsdgnSI4RAP%2F%2F%2F%2F8BjhGOEf%2F%2FAwAAAQAAAAABe6wCADtjAwAAC%2FwAABD%2B0S%2FhjhEA%2F%2F%2F%2F%2FwGOEY4R%2F%2F8DAAABAAAAAAHHeQIARiQDAAGLVQIAAQAAAM0MAQBgSO%2F2044RAP%2F%2F%2F%2F8BjhGOEf%2F%2FAQAAAQAAAAABeKMCALdXAwAAAAAAAAABRQ%3D%3D%5C%22%22%2C%22srv%22%3A%221587495718770%7C%5C%22ldnvwcgeu02%5C%22%22%7D%2C%22mmengine%22%3A%7B%22Integrations%22%3A%221555961517975%7C%7B%5C%22adobe%20analytics%5C%22%3A%7B%5C%22PER%20-%20WK%201%202019%20VM%20Going%20out%20vs%20occasion%5C%22%3A%7B%5C%22sessionDate%5C%22%3A1555959717760%7D%2C%5C%22PER%20-%20WK%203%202019%20Spend%20Stretch%20Countdown%5C%22%3A%7B%5C%22sessionDate%5C%22%3A1555959717971%7D%2C%5C%22PER%20-%20WK%2052%20New%20Customer%20POPUP%5C%22%3A%7B%5C%22sessionDate%5C%22%3A1555959717701%7D%7D%7D%22%7D%2C%22T_FootwearMenu%20QA%22%3A%7B%7D%2C%22T_FootwearMenu%20Mobile%22%3A%7B%7D%7D; mmapi.store.s.0=%7B%22mmparams.d%22%3A%7B%7D%2C%22mmparams.p%22%3A%7B%7D%2C%22mmengine%22%3A%7B%7D%2C%22T_FootwearMenu%20QA%22%3A%7B%22adobe-integration%22%3A%220%7C%5C%22footwear%3Aa0_newdefault%5C%22%22%7D%2C%22T_FootwearMenu%20Mobile%22%3A%7B%22adobe-integration%22%3A%220%7C%5C%22%5C%22%22%7D%7D; BVBRANDID=1c4b2b20-8566-46d5-856c-1cb49e41bc22; BVBRANDSID=13e9c8d0-4708-4081-8b6e-469b53bf6bee; sc_pp_path=home%20%3A%20women%27s%20clothes%20%3A%20womens%20clothing; ADRUM=s=1555960641738&r=https%3A%2F%2Fwww.newlook.com%2Fuk%2Fwomens%2Fclothing%2Fc%2Fuk-womens-clothing%3F1456608918; ecos.dt=1555960643324; XSRF-TOKEN=f8da0a62-f054-4b70-865d-70aea76e6b94; ADRUM_BTa="R:0|g:deaad903-e5be-48c1-924d-2803fa090e88|n:saasnewlookhybris_27749e59-4644-4fed-acb4-213f46a0a1f9"; akavpau_vpbc=1555961268~id=d031b01cf6b5bd66a32f4c951cf1c982',
            'pragma': 'no-cache',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
        }
        def get_sex(url_string):
            sex = None
            if len(url_string.split('/womens')) > 1:
                sex = 'women'
            if len(url_string.split('/mens')) > 1:
                sex = 'men'
            if len(url_string.split('/girls')) > 1:
                sex = 'women'

            return sex

        all_links = response.xpath('.//ul/li/a')
        all_link_dicts = []
        for link in all_links:
            link_url = link.xpath('@href').extract()
            link_name = link.xpath('text()').extract()
            all_link_dicts.append({
                'cat_name': link_name,
                'cat_url': link_url
            })
        valid_link_dicts = [url_dict for url_dict in all_link_dicts if
                            len(url_dict['cat_url']) > 0 and len(url_dict['cat_name']) > 0]
        valid_format_link_dicts = [{
            'cat_name': url_dict['cat_name'][0],
            'cat_url': url_dict['cat_url'][0]
        } for url_dict in valid_link_dicts]
        full_link_dicts = [url_dict for url_dict in valid_format_link_dicts if
                           len(url_dict['cat_url'].split('https')) == 2]
        cat_link_dicts = [url_dict for url_dict in full_link_dicts if
                          len(url_dict['cat_url'].split('/womens')) > 1 or len(
                              url_dict['cat_url'].split('/mens')) > 1 or len(url_dict['cat_url'].split('/girls')) > 1]
        cat_link_dicts_sex = [{
            'cat_name': cat_dict['cat_name'],
            'cat_url': cat_dict['cat_url'],
            'sex': get_sex(cat_dict['cat_url'])
        } for cat_dict in cat_link_dicts]

        cat_dicts_nohome = [cat_dict for cat_dict in cat_link_dicts_sex if
                            cat_dict['cat_url'] not in ['https://www.newlook.com/uk/mens',
                                                        'https://www.newlook.com/uk/womens']]
        for cat_link_dict in cat_dicts_nohome:
            timestamp = int(time.time() * 1000)
            initial_r = requests.get(
                f'{cat_link_dict["cat_url"]}/data-48.json?currency=GBP&language=en&lastIndexTime={timestamp}&page=0&q'
                f'=:relevance&sort=relevance&text=', headers=headers)
            if initial_r.status_code == 200:
                json_response = initial_r.json()
                page_count = json_response['data']['pagination']['numberOfPages']

                for i in range(0, page_count):
                    prod_r = requests.get(
                        f'{cat_link_dict["cat_url"]}/data-48.json?currency=GBP&language=en&lastIndexTime={timestamp}&'
                        f'page={i}&q=:relevance&sort=relevance&text=', headers=headers)
                    if prod_r.status_code == 200:
                        prod_json = prod_r.json()
                        prod_list = prod_json['data']['results']

                        for prod_dict in prod_list:
                            price = prod_dict['price']['value']
                            img_list = prod_dict['gallery']
                            img_urls = [f'http:{img_dict["url"]}?strip=true&qlt=80&w=1200' for img_dict in img_list]
                            name = prod_dict['name']
                            description = prod_dict['description']
                            size_options = prod_dict['sizeOptions']
                            # print(size_options)
                            size_stock = [{
                                'stock': 'In stock' if size_dict['stockStatus'] == 'AVAILABLE' else 'Out of stock',
                                'size': size_dict['value']
                            } for size_dict in size_options if 'value' in size_dict]
                            prod_id = prod_dict['code']
                            color_string = prod_dict['colourOptions'][prod_id]['displayName']
                            prod_url = f'https://www.newlook.com/uk{prod_dict["url"]}'
                            color_hex = prod_dict['colourOptions'][prod_id]['swatchColour']

                            yield scrapy.Request(
                                url=prod_url,
                                callback=self.parse,
                                meta={
                                    'cat_name': cat_link_dict['cat_name'],
                                    'sex': cat_link_dict['sex'],
                                    'cat_url': cat_link_dict['cat_url'],
                                    'price': price,
                                    'img_urls': img_urls,
                                    'name': name,
                                    'description': description,
                                    'size_stock': size_stock,
                                    'prod_id': prod_id,
                                    'color_string': color_string,
                                    'prod_url': prod_url,
                                    'color_hex': color_hex
                                }
                            )

    def parse(self, response):
        item = NewLookItem()
        item['shop'] = 'New Look'
        item['name'] = response.meta['name']
        # item['price'] = response.meta['price']
        item['prod_url'] = response.meta['prod_url']
        item['image_urls'] = response.meta['img_urls']
        item['sex'] = response.meta['sex']

        img_strings = item['image_urls']
        item['image_hash'] = []
        for img_string in img_strings:
            # Check if image string is a string, if not then do not pass this item
            if isinstance(img_string, str):
                # print(img_string)
                hash_object = hashlib.sha1(img_string.encode('utf8'))
                hex_dig = hash_object.hexdigest()
                item['image_hash'].append(hex_dig)

        item['date'] = int(datetime.datetime.now().timestamp())

        prev_price = response.xpath('.//strike[contains(@class, "price--previous-price")]/text()').extract_first()
        non_decimal = re.compile(r'[^\d.]+')
        if prev_price is not None and len(prev_price) > 0:
            print(f'PREV PRICE: {prev_price}')
            item['price'] = non_decimal.sub('', prev_price)
            sale_price = response.xpath('.//span[contains(@class, "price--marked-down")]/text()').extract_first()
            item['saleprice'] = non_decimal.sub('', sale_price)
            item['sale'] = True
        else:
            curr_price = response.xpath('.//span[contains(@class, "product-description__price")]/text()').extract_first()
            item['price'] = non_decimal.sub('', curr_price)
            item['sale'] = False
            item['saleprice'] = None

        item['brand'] = 'New Look'
        item['currency'] = 'GBP'
        item['description'] = response.meta['description']
        item['color_string'] = response.meta['color_string']
        item['color_hex'] = response.meta['color_hex']
        item['category'] = response.meta['cat_name']
        item['size_stock'] = response.meta['size_stock']

        yield item
