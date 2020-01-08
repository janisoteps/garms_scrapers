import scrapy
from noisymay.items import NoisymayItem
import hashlib
import re
import requests
import time


class NoisymaySpider(scrapy.Spider):
    name = "noisymay_spider"

    # The main start function which initializes the scraping URLs and triggers parse function
    def start_requests(self):
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,lv;q=0.8',
            'cache-control': 'no-cache',
            'cookie': '__cfduid=d24d068113b31bf517ab1ae9ef96c5dd51577707171; __cq_dnt=0; dw_dnt=0; dwanonymous_4887ae275d2e3149dd6a6534fdd472df=abYE6YkyBPG7yF0FcYS5tiuoTK; dwac_bc082iaaiTywMaaadqlmYUVd5G=VP0qIhrI5ogqrkXLgiZzTeg4eFyTuF7m1xI%3D|dw-only|||EUR|false|Europe%2FAmsterdam|true; dwsecuretoken_4887ae275d2e3149dd6a6534fdd472df=Q-JV78G2bhPgfU_xMYWe2ANzlDcpJMZsHw==; mt.v=2.2099170123.1577707188214; dw_cookies_accepted=1; mt.pc=2.1; _gcl_au=1.1.1332640076.1577707189; mt.g.829f7900=2.2099170123.1577707188214; _ga=GA1.2.2114291612.1577707189; _gid=GA1.2.1727498562.1577707189; __cq_uuid=d81b0bb0-c018-11e9-b6cd-25e4f7339976; customer_club_closed=true; _ga_cookie=VP0qIhrI5ogqrkXLgiZzTeg4eFyTuF7m1xI; dwanonymous_982e1e223e55662daee7d57e25e7fcbe=abkHVe7TmzGw4pIX0yx9xVWeNv; __cq_bc=%7B%22abbt-BSE-South%22%3A%5B%7B%22id%22%3A%2227000430%22%7D%5D%7D; tfc-l=%7B%22a%22%3A%7B%22v%22%3A%22b6a25f19-3715-427f-af0f-6537aae18ce1%22%2C%22e%22%3A1577794171%7D%7D; sid=DdVt9MxTXWhjjaL6ODIfnuq4DCNo5kCVquk; dwsid=msRSJsKqjTogfCt44u3rQH2pM_FmH5DH6RjnjAlgSpXIIEh0hYx0SphckDjDYEw9CkgT_fnGUKw_fGWuI6MIOQ==; dwanonymous_91b08f347cfea20452b0e969603162ea=acl14ydlTWfmy9xaxlGBOLYrcw; dwac_49c0f6ae5a5eb5be1f9fbe29ac=DdVt9MxTXWhjjaL6ODIfnuq4DCNo5kCVquk%3D|dw-only|||EUR|false|Europe%2FAmsterdam|true; dwsecuretoken_91b08f347cfea20452b0e969603162ea=CPQSS9Raga1bApK3S8EUCEi3PMGWqu7gWQ==; dwac_bcJ6oiaaiTPCaaaadq9ngUVd5G=DdVt9MxTXWhjjaL6ODIfnuq4DCNo5kCVquk%3D|dw-only|||EUR|false|Europe%2FAmsterdam|true; dwsecuretoken_982e1e223e55662daee7d57e25e7fcbe=CbM9C01fXJ8a62tSjlqFHJ1oeTz4lkcA7g==; cqcid=abkHVe7TmzGw4pIX0yx9xVWeNv; AMP_TOKEN=%24NOT_FOUND; _dc_gtm_UA-66188758-43=1; _dc_gtm_UA-66188758-20=1; __cq_seg=0~0.47!1~0.07!2~0.05!3~0.23!4~-0.06!5~-0.25!6~0.06!7~-0.54!8~-0.56!9~0.22',
            'pragma': 'no-cache',
            'referer': 'https://www.noisymay.com/gb/en/home',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }

        cat_page_req = requests.get('https://www.noisymay.com/gb/en/nm/clothing/?sz=60&start=0', headers=headers)
        prod_count_match = re.search('(?<=nm-shop-by-category\",\"items\"\:).*?(?=\})', cat_page_req.text)
        prod_count = int(prod_count_match.group(0))
        page_count = int(prod_count / 60) + 1

        for i in range(0, page_count, 1):

            yield scrapy.Request(
                url=f'https://www.noisymay.com/gb/en/nm/clothing/?sz=60&start={60 * i}',
                callback=self.prod_collection
            )

    def prod_collection(self, response):
        prod_urls = response.xpath('.//a[contains(@class, "plp__products__item__image-container")]/@href').extract()

        for prod_url in prod_urls:
            yield scrapy.Request(
                url=prod_url,
                callback=self.parse
            )

    def parse(self, response):
        color_pattern_cats = [
            'abstract',
            'acid',
            'animal',
            'apricot',
            'beige',
            'black',
            'blue',
            'bright',
            'brown',
            'burgundy',
            'cable',
            'camo',
            'charcoal',
            'check',
            'chevron',
            'circle',
            'clear',
            'contrast',
            'cream',
            'crochet',
            'dark',
            'dot',
            'dye',
            'embellished',
            'embellishment',
            'embroidered',
            'embroidery',
            'floral',
            'flower',
            'gingham',
            'gold',
            'green',
            'grey',
            'heart',
            'indigo',
            'jacquard',
            'khaki',
            'knot',
            'lace',
            'lattice',
            'leopard',
            'lettuce',
            'light',
            'lilac',
            'lime',
            'logo',
            'mango',
            'mesh',
            'monochrome',
            'mustard',
            'navy',
            'neon',
            'nude',
            'ombre',
            'orange',
            'paisley',
            'pale',
            'palm',
            'pattern',
            'peach',
            'pink',
            'pinstripe',
            'polka',
            'print',
            'printed',
            'purple',
            'rainbow',
            'red',
            'rib',
            'rose',
            'rust',
            'silver',
            'snake',
            'spot',
            'square',
            'star',
            'stitch',
            'straw',
            'stripe',
            'striped',
            'stripes',
            'tan',
            'tea',
            'textured',
            'tiger',
            'tortoiseshell',
            'triangle',
            'tropical',
            'vanilla',
            'wash',
            'washed',
            'white',
            'yellow',
            'zebra'
        ]
        item = NoisymayItem()

        item['shop'] = "Noisy May"
        name_match = response.xpath('.//h1[@class="product-name--visible"]/text()').extract_first()
        item['name'] = name_match.lower().title()

        price_match = re.search('(?<=\"price\"\:\").*?(?=\")', response.text)
        price = float(price_match.group(0))
        item['price'] = price
        saleprice_match = re.search('(?<=\"salesPrice\"\:\").*?(?=\")', response.text)
        saleprice = float(saleprice_match.group(0))
        item['saleprice'] = saleprice
        if saleprice == price:
            sale = False
        else:
            sale = True
        item['sale'] = sale

        item['prod_url'] = response.url
        if isinstance(response.url, str):
            prod_id_hash_object = hashlib.sha1(response.url.encode('utf8'))
            prod_id_hex_dig = prod_id_hash_object.hexdigest()
            item['prod_id'] = prod_id_hex_dig

        image_urls = response.xpath('.//img[@data-size="maincarousel"]/@data-src').extract()
        item['image_urls'] = image_urls
        img_strings = item['image_urls']
        item['image_hash'] = []
        for img_string in img_strings:
            # Check if image string is a string, if not then do not pass this item
            if isinstance(img_string, str):
                hash_object = hashlib.sha1(img_string.encode('utf8'))
                hex_dig = hash_object.hexdigest()
                item['image_hash'].append(hex_dig)

        item['sex'] = 'women'

        color_match = response.xpath('.//p[@class="color-combination"]/text()').extract_first()
        color_words = color_match.split(' ')
        color_cats = [word.lower() for word in color_words if word.lower() in color_pattern_cats]
        if len(color_cats) > 0:
            color_string = color_cats[0]
        else:
            color_string = color_match[0].lower()
        item['color_string'] = color_string

        item['brand'] = 'Noisy May'
        item['currency'] = '£'
        item['date'] = int(time.time())

        desc_1 = response.xpath('.//pre[@class="pdp-description__text__short"]/text()').extract()
        desc_2 = response.xpath('.//li[contains(@class, "pdp-description__text__value--fabric")]/text()').extract()
        desc_3 = response.xpath('.//li[@class="pdp-description__list__item"]/text()').extract()
        desc_list = desc_1 + desc_2 + desc_3
        desc_concat = ' '.join(desc_list)
        description = desc_concat.replace('  ', '')
        item['description'] = description

        category_match = re.search('(?<=\"category\"\:\").*?(?=\")', response.text)
        item['category'] = category_match.group(0).lower()

        size_match = response.xpath('.//ul[@data-group-id="size"]/li/a/div/text()').extract()
        size_stock = [{
            'size': size,
            'stock': 'In stock'
        } for size in size_match]
        item['size_stock'] = size_stock

        in_stock = False
        for size in size_stock:
            if size['stock'] == 'In stock':
                in_stock = True
        item['in_stock'] = in_stock

        yield item
