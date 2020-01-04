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
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,lv;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Cookie': 'adform_qv=1; akainst=EU1; bm_sz=371D238A55056C204874C555E01A6A8B~YAAQlboQAvLYuzJvAQAAGQY8awauq69/pGSHws4wcsKGgsPT6LdyCAjmaZV0GX9uvTihCIvA65KDYhrJqC4qAMtvIZxorc+pakGPK1bJrjqrHD0ZqxIQJ1DXAhwyjgRo+oQqTcbNBzsLQai2KYVvP1nyX/EdY7Lr93lQgrDx+sQP6RHgdcwLZdii7iI=; ab_first_session=true; ab_new_user=true; optimizelyEndUserId=oeu1578052093793r0.7104636023804616; TS013be3eb=01dd555d354971cb206c5bba70bf2e9d04d1a58426f162ab00cd4fc26a21fa3cb65c42bf9f93779068d9851f4cef8aa1b49de293ff4b883a07208aea327f2633fb2a3e81b2; HMX_123=1; agCookie=42072c9b-119c-42ed-89e9-44593ab6965c; JSESSIONID=ACB6A971DFD79F8048A71BB30598A902B94A5121B0B95BC07F7E13732414B6C1C7F35BCDC30EE5D0C1B95CFE6CC8FA88CD3F587BEA5F7B524F8BB8947C24F66D.HYBECMPRDEU1P04; userCookie=##eyJjYXJ0Q291bnQiOjB9##; hm-greatbritain-favourites=""; TS0150476f=01dd555d35a598ad3f045c681e28059232d3555981f162ab00cd4fc26a21fa3cb65c42bf9f5f2238745280e5d31c5a0423cf824cef95b49b72684695a6c5c0658469808db7d9f76b09d804f675e6d09b914e97787bf51720c957e3e859a523fab247a3304ddc07fa1348d93c8e244d9cbadcf553ab; _abck=B470CB0246C637DAA9DA0AD2201507F5~0~YAAQlboQAv7YuzJvAQAAWwo8awMLy/Zk99YwNaI8nRCge8fc/c1cPB0Ff+CX8kNb4fCBNM/jqQfVNsWJRwBRDsn0uaiHJYC+5U4U6KI56MFX71+EC/HIoUcY1k3PY0KR5NmDOu7TvunrDCJtEGjUUO3NsFzaEPfyyypl9YLGuZI7Tt1teu2/wfiOGWDCgOuhvjO9csQnhXzBSL2Cd7arWcJichru5/VSyBcaFljhhzMlnQWZRMExmirLiKMYmBN7OwMgzZRta4X6deI4EAphsB05ZZd7DqqBBK3EkEoah1gbg+JceufVd7rt/AU2WLD8cjdn~-1~-1~-1; ak_bmsc=200CC601CA62B5AED384CA445B0647A10210BA9569290000FD290F5EEF53C94F~plNkbv1Q+bUCEJ6s5avcoQhFfz3EVrc0AEef/9D8Y/tUuNC9kCVnfUOYCauuWxgxQFUtTuTLoVGbCAdoanppR1ZAWLZw8x42q4VVSqrFqUSoMfr9S9O7jut45Vu2vCa6nJWzVswR2M7n6HfKaAzwaISbd/9EJabwhHX0Ohv2gRH/BQQjCZQxQStOn4mSBqlAtcUgb7DFsdqjrnDfxtsvWzNKpvdo9kyJYvTZWOQqkk76Y1Er+RGtcnmxagpo42WIzi; AMCVS_32B2238B555215F50A4C98A4%40AdobeOrg=1; AMCV_32B2238B555215F50A4C98A4%40AdobeOrg=-1891778711%7CMCIDTS%7C18265%7CMCMID%7C32509042840667002613805168883976474988%7CMCAAMLH-1578656894%7C6%7CMCAAMB-1578656894%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1578059294s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C2.4.0; akamref=en_gb; s_cc=true; _ga=GA1.2.1762485173.1578052097; _gid=GA1.2.91507510.1578052097; _gat_GA_GLOBAL=1; _gat_GA_LOCAL=1; aasegs=aal%3D16770768; aamgasegs=segid%3D16770768; aemsegs=aem%3D15496949; AAMAA=AAMSegID%3D6499983; aamoptsegs=aam%3D6499983; aam_uuid=32480940005034741573801223354624019812; rmStore=atm:mop; _scid=55e0609b-c299-4698-9659-7336d7bbb9c5; _gcl_au=1.1.1999456257.1578052098; _derived_epik=dj0yJnU9dHVNb1ZwU1BWLWdTakR1WkI4SXBJRExWTTJscGNheWImbj05YjRzMTJUTkltbHRLOG9NeG1DZ253Jm09NyZ0PUFBQUFBRjRQS2dF; stc114913=tsa:1578052097860.965267166.0997734.22803766749101118.:20200103121817|env:1%7C20200203114817%7C20200103121817%7C1%7C1044345:20210102114817|uid:1578052097860.462183129.81846285.114913.1270117984:20210102114817|srchist:1044345%3A1%3A20200203114817:20210102114817; _CT_RS_=Recording; WRUIDAWS20180923=2588372142063675; __CT_Data=gpv=1&ckp=tld&dm=hm.com&apv_44_www36=1&cpv_44_www36=1&rpv_44_www36=1; dtPC=-; dtLatC=1; akavpau_www2_en_gb=1578052402~id=a2de8376130a19b91e7d6cad1c6f1b7e; bm_sv=1DF3FBF8986D2EB7A0C29B188D1263F7~U+1nPa2Om/ebIZWhib5B/8Dya3ev8adQ827V85zw3aEAcltUGL7gYLgUQbji0wlaE8HZTmA6/KPn+2/K+/hoPFACslUrlnMDlMRVNJx5INL+HfutnoCBxB7+pbQUBnZn9ye0CggRbnf34bCIAQdC2A==; ctm={\'pgv\':8652317113624582|\'vst\':3673420648741103|\'vstr\':3489893303812675|\'intr\':1578052105258|\'v\':1}; utag_main=v_id:016f6b3c0ac2002c3d3c4fb28e6803078002507000c48$_sn:1$_se:5$_ss:0$_st:1578053907148$ses_id:1578052094659%3Bexp-session$_pn:1%3Bexp-session$touchpoint:DESKTOP%3Bexp-session$vc:%7B%7D%3Bexp-session$cart_active:No%3Bexp-session$opt_ga:16836871062_16857820741%3Bexp-session$vapi_domain:hm.com; dtCookie=127A539A60CFA9971BCCF7218A073C8D|SCUyNk0rUHJvZHVjdGlvbitXZWJ8MQ; dtSa=true%7CKD82%7C-1%7CHM.com%20%20LadiesNew%20ArrivalsClothesShoes%20%26%20AccessoriesBeautyShop%20by%20ProductView%20AllDressesShirts%20%26%20Blo...%7C-%7C1578052107710%7C52093668_530%7Chttps%3A%2F%2Fwww2.hm.com%2Fen_5Fgb%2Fladies.html%7CWomen%27s%20Clothing%20%26%20Fashion%20-%20shop%20the%20latest%20trends%20%5Ep%20H%26M%20GB%7C1578052101992%7C; RT="sl=1&ss=1578052093291&tt=3673&obo=0&bcn=%2F%2F0211c844.akstat.io%2F&sh=1578052096970%3D1%3A0%3A3673&dm=hm.com&si=b2ea6600-abba-4323-9fee-d836e61c05a9&ld=1578052096970&r=https%3A%2F%2Fwww2.hm.com%2Fen_gb%2Fladies.html&ul=1578052107734"',
            'Host': 'www2.hm.com',
            'Pragma': 'no-cache',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }

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

            count_check_response = requests.get(count_check_url, headers=headers)
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
                        get_prod_response = requests.get(get_prod_url, headers=headers)
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
                                if len(current_swatch) > 0:
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
        item['shop'] = 'H&M'
        item['name'] = response.meta['name']
        item['price'] = response.meta['price']
        item['sale'] = response.meta['sale']
        item['saleprice'] = response.meta['sale_price']
        item['prod_url'] = response.meta['prod_url']
        item['sex'] = response.meta['sex']
        item['category'] = response.meta['cat_name']
        item['color_string'] = response.meta['color_string']

        if isinstance(response.meta['prod_url'], str):
            prod_id_hash_object = hashlib.sha1(response.meta['prod_url'].encode('utf8'))
            prod_id_hex_dig = prod_id_hash_object.hexdigest()
            item['prod_id'] = prod_id_hex_dig

        # main_img_re = './/div[@class="product-detail-main-image-container"]/img/@src'
        formatted_text = response.text.replace('"', '\'')
        js_match = re.search('(?<=productArticleDetails\ =\ )[\s\S]*(?=\;)', formatted_text)
        prod_match = re.search(f'(?<=\'{response.meta["prod_id"]}\'\:\ )[\s\S]*(?=\,\n)', js_match.group(0))
        images_string_match = re.search('(?<=\'images\'\:\[).*?(?=\]\,\r\n)', prod_match.group(0), re.I | re.DOTALL)
        if images_string_match is not None:
            img_slug_match = re.findall('(?<=fullscreen\'\:\ isDesktop\ \?\ \').*?(?=\'\ \:)', images_string_match.group(0))
            item['image_urls'] = [f'https:{img_slug}' for img_slug in img_slug_match]
        else:
            MAIN_IMG_SELECTOR = './/div[@class="product-detail-main-image-container"]/img/@src'
            main_img_arr = response.xpath(MAIN_IMG_SELECTOR).extract()
            item['image_urls'] = [f'https:{img_url}' for img_url in main_img_arr]

        sizes_match = re.search('(?<=\'sizes\'\:\[)[\s\S]*?(?=\]\,)', prod_match.group(0))
        size_name_match = re.findall('(?<=\'name\'\:\ \')[\S]*?(?=\')', sizes_match.group(0))
        sizes_stock = [{
            'stock': 'In stock',
            'size': size
        } for size in size_name_match]
        item['size_stock'] = sizes_stock

        if len(item['size_stock']) > 0:
            item['in_stock'] = True
        else:
            item['in_stock'] = False

        item['image_hash'] = []
        for img_string in item['image_urls']:
            # Check if image string is a string, if not then do not pass this item
            if isinstance(img_string, str):
                hash_object = hashlib.sha1(img_string.encode('utf8'))
                hex_dig = hash_object.hexdigest()
                item['image_hash'].append(hex_dig)

        item['date'] = int(datetime.datetime.now().timestamp())
        item['currency'] = '£'
        item['brand'] = 'H&M'

        DESCRIPTION_SELECTOR = './/p[contains(@class, "pdp-description-tex")]/text()'
        item['description'] = response.xpath(DESCRIPTION_SELECTOR).extract_first()

        yield item
