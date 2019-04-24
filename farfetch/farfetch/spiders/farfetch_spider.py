import scrapy
from farfetch.items import FarfetchItem
import hashlib
import time
import re


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

        for cat_url_elem_list in cat_url_elems:
            for cat_url_anchor in cat_url_elem_list:
                cat_url = 'https://www.farfetch.com' + cat_url_anchor.xpath('.//@href').extract_first()
                cat_name = cat_url_anchor.xpath('.//text()').extract_first()

                print('Category URL: ', str(cat_url))
                print('Category name: ', str(cat_name))

                yield scrapy.Request(
                    url=cat_url,
                    callback=self.product_collection,
                    meta={
                        'cat_name': cat_name
                    }
                )

    # Collect product URLs in each category
    def product_collection(self, response):
        cat_name = response.meta['cat_name']

        prod_urls = response.xpath('.//div[@class = "listing-item-image"]/a/@href').extract()

        for prod_url in prod_urls:
            print('Product URL scraped: ', str(prod_url))
            prod_req_url = 'https://www.farfetch.com' + prod_url
            yield scrapy.Request(
                url=prod_req_url,
                callback=self.parse,
                meta={
                    'cat_name': cat_name
                }
            )

        current_page = response.xpath('.//span[@data-tstid = "paginationCurrent"]/text()').extract_first()
        if current_page is not None:
            current_page = int(current_page)

            total_pages = response.xpath('.//span[@data-tstid = "paginationTotal"]/text()').extract_first()
            if total_pages is not None:
                total_pages = int(total_pages)

                if total_pages > current_page:
                    if response.url[-6:-1] == 'page=':
                        next_page_url = str(response.url)[0:-1] + str(current_page + 1)
                    else:
                        next_page_url = str(response.url) + '?page=' + str(current_page + 1)

                    print('Next page scraped: ', str(next_page_url))
                    yield scrapy.Request(
                        url=next_page_url,
                        callback=self.product_collection,
                        meta={
                            'cat_name': cat_name
                        }
                    )

    # Scrape the product page
    def parse(self, response):
        item = FarfetchItem()

        item['category'] = response.meta['cat_name']
        item['shop'] = 'Farfetch'
        item['currency'] = '£'
        item['sex'] = response.url.partition('shopping/')[2].partition('/')[0]
        item['prod_url'] = response.url

        item['name'] = response.xpath('.//title/text()').extract_first()

        try:
            item['price'] = re.findall(r'(?<=unit_price\"\:).*?(?=\,)', str(response.body))[0]
        except:
            item['price'] = None

        if item['price'] is not None:
            try:
                item['saleprice'] = re.findall(r'(?<=unit_sale_price\"\:).*?(?=\,)', str(response.body))[0]
            except:
                item['saleprice'] = ''

            if float(item['saleprice']) == float(item['price']):
                item['sale'] = False
                item['saleprice'] = ''
            else:
                item['sale'] = True

            item['image_urls'] = response.xpath('.//img[@itemprop = "image"]/@data-zoom-image').extract()

            # Calculate SHA1 hash of image URL to make it easy to find the image based on hash entry and vice versa
            # Add the hash to item
            img_strings = item['image_urls']

            item['image_hash'] = []

            for img_string in img_strings:
                # Check if image string is a string, if not then do not pass this item
                if isinstance(img_string, str):
                    # print(img_string)
                    hash_object = hashlib.sha1(img_string.encode('utf8'))
                    hex_dig = hash_object.hexdigest()
                    item['image_hash'].append(hex_dig)

            color = response.xpath('.//span[@itemprop = "color"]/text()').extract_first()
            color = ''.join(filter(str.isalpha, color))
            item['color'] = color.lower()

            item['brand'] = response.xpath('.//a[@itemprop = "brand"]/text()').extract_first()

            item['date'] = int(time.time())

            item['description'] = response.xpath('.//p[@itemprop = "description"]/text()').extract_first()

            yield item
