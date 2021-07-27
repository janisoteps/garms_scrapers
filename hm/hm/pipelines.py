# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from scrapy.exceptions import DropItem
import random
import os
import shutil
import requests


class HmPipeline(object):
    def process_item(self, item, spider):
        return item


class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        proxies = [
            'http://35.177.0.176:8888',
            'http://52.56.151.179:8888',
            'http://35.178.95.179:8888'
        ]
        proxie_dicts = [{
            'http': proxy,
            'https': proxy
        } for proxy in proxies]

        for index, image_url in enumerate(item['image_urls']):
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9,lv;q=0.8',
                'cache-control': 'no-cache',
                'cookie': 'optimizelyEndUserId=87851502006c0000c0a3ae5eaa02000018e20000; bm_sz=B09907DA76056612E679B137FA36F89C~YAAQh4UVAr/Wu9ZxAQAAqqgv2geyKuyFICyWKbnpUtfN27OKiUhLjzs/H2fjeLLox4Ugmka9BYLY0m7eDZzhvyOg7MRkkOAS8Dh5Tr+EZTNeU++YTrzpgYtM9nLz6n9fS8lRgjrX2JLnWXubAXKL9iiU2nv7+JlbYSdbgR0qPINF4naEALjy+V0EGXU=; dtCookie=80B131FF847291D3979A6205B951F3DF|SCUyNk0rUHJvZHVjdGlvbitXZWJ8MQ; TS013be3eb=01dd555d35b1b453ea28bac6a33603a938abe6dbdd57f2d18390588134c0533a9cb4acf252b888604bcf55009c2f819179ba9771945da653a71dca55081f68cf743e67de0c; ak_bmsc=7B3A36A6E1F2D3F739C95052F82FB9B902158587006C0000C0A3AE5EA9CD6869~plrMXrTQsg+/2ApyTUuol1r9+0M94nUuHGh2+WDkf2iUee6058kJt71A8KGUaluybtNAdy6Yw9mlPc+XYmNQXh5KpJ0udNzUhuwXZXto8U4JdVPJsIlWitsS1oaHICRtwdwx5lQ1gfrskjCUUsdmxjj5RThHKUjJBsE6Nk6ZhQg2+OOYt1lTE4f+qprYDVIySVVer2Zj3dPXeQAXgkenvgVC0LNoNhiab+9Fa+AtFTx9vX8J6xWqceudW98XYfzXQj; _abck=21D722E9065A88B928AA7140EE0D2411~0~YAAQh4UVAt3Wu9ZxAQAApa8v2gNbABw7f0Ur+nv0CQwMdkWdtKVIvhKvfpjmaQ7Bkn+Ld3SL95Z697sAZr0lTc3Lx0j1I69KwSJdJ90JcmgOue/1diVwRGpBfuYuWEhBMxKAYfG6OZyoPX/GnHjCQiuLNGuLWR15262AGpLW/77FpaDRkaw/PHb8vLvu7XITZocMX9NJxaAfug5tWZzjuOJ/2Rr6hNN4Vr3LdlphwdYiOAVJMyLmF1AhXAyCZJJ2pgMZUMoqHYfTpK1VByKNbryq1XrJvu7NhFSb2VPvIjkzZE5jnb+zp1kwVz+ORXwAqaCr~-1~-1~-1; _ga=GA1.2.23667329.1588503492; _gid=GA1.2.405601047.1588503492; s_fid=7EA0798BEC65AAEA-1B3080A1ED5A66B4; rmStore=atm:mop; _scid=aee280d1-2dc8-41ca-8fc8-224c82b2af2c; _gcl_au=1.1.1854431299.1588503492; _cs_c=1; _cs_cvars=%7B%221%22%3A%5B%22page%20id%22%2C%22Ladies%20Department%22%5D%2C%222%22%3A%5B%22category%20id%22%2C%22LADIES_DEPARTMENT_VIEW_ALL%22%5D%2C%223%22%3A%5B%22category%20path%22%2C%22LADIES_DEPARTMENT_VIEW_ALL%22%5D%2C%224%22%3A%5B%22selected%20market%22%2C%22GB%22%5D%2C%228%22%3A%5B%22customer%20status%22%2C%22FALSE%22%5D%7D; bm_sv=C16E7439BFA646C247A3115D6C0E1BB0~k+NYSlnLy+D6VDcFos8HZkh6+JLe49m1suTTFeXTtOY+v96e3NHO5xFuwxdUnfGuksFmquF8tqwtdCCIarYXomer/xHae2Rbx4F01ORIDYKwCF8uqGW474BzHsHkHa82ExfLc8Q6WCP1+VujZ+Tirw==; AMCVS_32B2238B555215F50A4C98A4%40AdobeOrg=1; s_ecid=MCMID%7C32509042840667002613805168883976474988; AMCV_32B2238B555215F50A4C98A4%40AdobeOrg=-1891778711%7CMCIDTS%7C18386%7CMCMID%7C32509042840667002613805168883976474988%7CMCAAMLH-1589108316%7C6%7CMCAAMB-1589108316%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1588510716s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C2.4.0; utag_main=v_id:0171da2fae1a00125ccf89b3614d03079002507100c48$_sn:1$_se:5$_ss:0$_st:1588505316811$ses_id:1588503490075%3Bexp-session$_pn:2%3Bexp-session$accept_cookies:1$touchpoint:DESKTOP%3Bexp-session$vc:%7B%7D%3Bexp-session$cart_active:No%3Bexp-session$opt_ga:16836871062_16857820741%3Bexp-session$vapi_domain:hm.com; _uetsid=_uet19ac9f29-4bf8-d2aa-11bf-d5d01f126f19; ctm={\'pgv\':780893172792761|\'vst\':99064286683716|\'vstr\':8824529793755444|\'intr\':1588503517702|\'v\':1}; _cs_id=f630f36c-b4c1-af4e-9428-cc59e8ffae27.1588503492.1.1588503517.1588503492.1.1622667492645.Lax.0; _cs_s=2.1; __CT_Data=gpv=2&ckp=tld&dm=hm.com&apv_44_www36=2&cpv_44_www36=2; RT="sl=2&ss=1588503488535&tt=5176&obo=0&sh=1588503516702%3D2%3A0%3A5176%2C1588503491607%3D1%3A0%3A3067&dm=hm.com&si=9dc8f852-5576-4b1f-a29e-a600fd9d853e&bcn=%2F%2F0211c814.akstat.io%2F"',
                'pragma': 'no-cache',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
            }

            print('SCRAPING IMAGE')
            print(f'IMG URL {image_url}')
            img_hash = item['image_hash'][index]
            out_file_path = f'images/full/{img_hash}.jpeg'

            img_response = requests.get(image_url, headers=headers, stream=True, proxies=random.choice(proxie_dicts))

            with open(out_file_path, 'wb') as out_file:
                shutil.copyfileobj(img_response.raw, out_file)

    def item_completed(self, results, item, info):
        # image_urls = [x['path'] for ok, x in results if ok]
        # if not image_urls:
        #     raise DropItem("Item contains no images")
        # item['image_urls'] = image_urls
        return item
