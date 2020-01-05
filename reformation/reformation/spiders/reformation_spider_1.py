import scrapy
from reformation.items import ReformationItem
import hashlib
import time
import re
import json


class ReformationSpider(scrapy.Spider):
    name = "reformation_spider"

    def __init__(self, name=None, **kwargs):
        super().__init__(name=None, **kwargs)
        self.visited_urls = set()

    # Main start function
    def start_requests(self):
        url = 'https://www.thereformation.com/sitemap'

        yield scrapy.Request(url=url, callback=self.category_collection)

    def category_collection(self, response):
        sitemap_links = response.xpath('.//li[@class="sitemap__item"]')
        cat_urls = []
        for sitemap_link in sitemap_links:
            sitemap_url = sitemap_link.xpath('.//a/@href').extract_first()
            if 'http' not in sitemap_url and 'categories' in sitemap_url:
                cat_name_slug = sitemap_url.split('categories/')[1]
                cat_name_arr = [cat_string for cat_string in cat_name_slug.split('-') if cat_string.isalpha()]
                cat_name = ' '.join(cat_name_arr).title()
                cat_urls.append({
                    'cat_url': 'https://www.thereformation.com' + sitemap_url,
                    'cat_name': cat_name
                })

        for cat_url in cat_urls:
            yield scrapy.Request(
                url=cat_url['cat_url'],
                callback=self.product_collection,
                meta={
                    'cat_name': cat_url['cat_name']
                }
            )

    def product_collection(self, response):
        next_page = response.xpath('.//link[@rel = "next"]/@href').extract_first()

        prod_tiles = response.xpath('.//div[@class="product-summary"]')
        prod_list = []
        for prod_tile in prod_tiles:
            prod_url = 'https://www.thereformation.com' + \
                       prod_tile.xpath('.//a[@class="product-summary__media-link"]/@href').extract_first()
            prod_name = prod_tile.xpath('.//h2[@class="product-summary__name"]/a/text()').extract_first()
            prod_list.append({
                'prod_url': prod_url,
                'prod_name': prod_name
            })

        for prod_dict in prod_list:
            print('Product URL scraped: ', str(prod_dict['prod_url']))
            self.visited_urls.add(prod_dict['prod_url'])
            yield scrapy.Request(
                url=prod_dict['prod_url'],
                callback=self.parse,
                meta={
                    'cat_name': response.meta['cat_name'],
                    'name': prod_dict['prod_name'],
                    'prod_url': prod_dict['prod_url']
                }
            )

        if next_page is not None:
            yield scrapy.Request(
                url=next_page,
                callback=self.product_collection,
                meta={
                    'cat_name': response.meta['cat_name']
                }
            )

    def parse(self, response):
        item = ReformationItem()

        item['name'] = response.meta['name']
        item['description'] = response.xpath('.//div[@itemprop="description"]/text()').extract_first()
        item['image_urls'] = response.xpath('.//img[contains(@class, "pdp__primary-image-link-image")]/@data-src').extract()

        img_strings = item['image_urls']
        item['image_hash'] = []
        for img_string in img_strings:
            # Check if image string is a string, if not then do not pass this item
            if isinstance(img_string, str):
                hash_object = hashlib.sha1(img_string.encode('utf8'))
                hex_dig = hash_object.hexdigest()
                item['image_hash'].append(hex_dig)

        item['shop'] = 'Reformation'
        item['currency'] = '£'

        product_prices_string = response.xpath('.//p[@class="product-prices__price"]/span/@data-fp').extract_first()
        prod_prices_json = json.loads(product_prices_string)
        item['price'] = prod_prices_json['defaults']['GBP']
        item['prod_url'] = response.meta['prod_url']

        if isinstance(response.meta['prod_url'], str):
            prod_id_hash_object = hashlib.sha1(response.meta['prod_url'].encode('utf8'))
            prod_id_hex_dig = prod_id_hash_object.hexdigest()
            item['prod_id'] = prod_id_hex_dig

        item['sex'] = 'women'
        item['sale'] = False
        item['saleprice'] = None

        orig_url = response.meta['prod_url']
        alt_color_opts = response.xpath('.//li[@class="pdp-color-options__color"]/a/div/text()').extract()
        orig_color = orig_url.split('?color=')[1].split('&')[0]

        item['color_string'] = orig_color
        item['brand'] = 'Reformation'
        item['date'] = int(time.time())
        item['category'] = response.meta['cat_name']

        size_opts = response.xpath('.//div[@class="pdp-size-options__size-button"]')
        size_stock = []
        for size_opt in size_opts:
            size_json_string = size_opt.xpath('.//input/@data-pdp-size-button').extract_first()
            size_json = json.loads(size_json_string)
            size = size_json['size']

            disabled_match = size_opt.xpath('.//input/@disabled')
            disabled = False
            if len(disabled_match) > 0:
                disabled = True

            size_stock.append({
                'size': size,
                'stock': 'In stock' if disabled is False else 'Out of stock'
            })

        item['size_stock'] = size_stock
        if len(item['size_stock']) > 0:
            item['in_stock'] = True
        else:
            item['in_stock'] = False

        alt_color_urls = [orig_url.split(orig_color)[0] + alt_color + orig_url.split(orig_color)[1] for alt_color in alt_color_opts]
        for alt_color_url in alt_color_urls:
            if alt_color_url in self.visited_urls:
                print('ALREADY SCRAPED')
            else:
                self.visited_urls.add(alt_color_url)
                yield scrapy.Request(
                    url=alt_color_url,
                    callback=self.parse,
                    meta={
                        'cat_name': response.meta['cat_name'],
                        'name': response.meta['name'],
                        'prod_url': alt_color_url
                    }
                )

        yield item
