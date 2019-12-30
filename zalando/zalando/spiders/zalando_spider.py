import scrapy
from lxml import etree
from zalando.items import ZalandoItem
import hashlib
import re
import requests
import json
import datetime


class ZalandoSpider(scrapy.Spider):
    name = "zalando_spider"

    # The main start function which initializes the scraping URLs and triggers parse function
    def start_requests(self):
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,lv;q=0.8',
            'cache-control': 'no-cache',
            'cookie': 'fvgs_ml=mosaic; frsx=AAAAALZhWsZk02ljiSRiMe4HQv-HOE5K3fuNuHRSNeNxUIhZg808YlKMyq5B5fs6ATXMJDtkDwA1QQuhnSFhHDdqURXke9qv23n7tQ7e3rNAZGmx-Kw42LlxlrKiOI5z5ZwwidZpCEoKBDRNOkcqM_E=; Zalando-Client-Id=e05d7de4-47d5-4c92-9c94-fb4d8366f543; bm_sz=45E0CF7E5A3DEC84F8D257A26300950E~YAAQFd3dWF9YoT5vAQAA3629VgaNYlQGi2FegrE/TPqD1XWm5JRbm5rhUwbR3sV5xT+zKa709NGSfE4Tr5PA43woKv0h/i5Opo2ZL07zg3k7TMfC0BVXOZ+WtLvwdrAcJ8LTS1Rn81vCAOp7c2yuRhXcta9fZyhkqsF+7EDXIVXMbHy1ICQcOtBiWBR0CiylSyTi; ak_bmsc=02E54EE860C684EB5D0AAEF20DA8C7FB58DDDD15164D0000EDEA095E05F0B210~pl9i/AYVaFnH5skV7Flekf5p+YeDahaTDp0cf8K8IUQXaY5Y6aP3sVJ/ReRfZlD+qdyKteQOWIPQgbRQfGeSPTN0S8uKVTNhvHNIFqmxUo5Ot3VENV1tL79c9/KZPooe6cd0sTFCFAM49wNNpto9YNd5GcPCjVcIFil6dZwnqzD6Ust4zX3Ljm3HHTLP83lijh5pX5qAoXipAWd1OQvmSbuHfXwb3hAWU2EncZ6BocuaYMzDsZmTOXtWQVC4lHBhDNJGI7i3MbX0XUm9m/Xm9N8zRwScJAAG4VL2tC76W3gXd5Z/yRvpufqJ1sUJ4HaoRNxvAIo9XPwE6Qz154LFrtXw==; _ga=GA1.3.333545424.1577708271; _ga=GA1.3.333545424.1577708271; _gid=GA1.3.599663451.1577708272; _gcl_au=1.1.1619036198.1577708272; sqt_cap=1577708271496; _gat_zalga=1; ncx=f; _derived_epik=dj0yJnU9UjdPajdyS3dvX0EzMktSV0Q4M0FKWWVIQnhqaDYtOEkmbj1yZnpGSTFBdVVsNWpWbUdDcGM5OGF3Jm09NyZ0PUFBQUFBRjRKNng0; _abck=AF74E2D14D67F222EA4ACBF9C403D4E4~-1~YAAQFd3dWCJfoT5vAQAAZ6C+VgP526gARPkzGyU9VHleRm7BuA50h/WPFM0bafIXfrf6z6fk+QBSNj9Yjvxx16ecDFZj2sOovzNGY2RlDZx5ZxNZO21fO+K32vXvCP3YH4Q1cdP/ADvunjkpemHgn4Q9hjek8asRQfR+6BAdpAimptXiEsdrFp2mOWVMF5NmM0mzcxKMroucCjoEbwj8ftqH6htZ16p8NJKYVYm3qcoYb3JGC5+UDb0SluUeM9fklzOBjR9AHFKcUhCITwxw/MJS77f180LZbEB/AvgYjP88U1uwTwSOIY7D852cSWZ20qlQFEi6SdyK+T1K6PjG9i+uEoRvGkE=~-1~-1~-1',
            'pragma': 'no-cache',
            'referer': 'https://www.zalando.co.uk/',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }

        init_req_url = 'https://www.zalando.co.uk/api/catalog/articles?limit=84&offset=84&sort=popularity'
        init_ajax_req = requests.get(init_req_url, headers=headers)
        init_json_dict = json.loads(init_ajax_req.text)
        page_count = init_json_dict['pagination']['page_count']

        for i in range(0, page_count, 1):
            inner_api_url = f'https://www.zalando.co.uk/api/catalog/articles?limit=84&offset={i * 84}&sort=popularity'
            inner_ajax_req = requests.get(inner_api_url, headers=headers)
            inner_json_dict = json.loads(inner_ajax_req.text)
            item_array = inner_json_dict['articles']

            for item in item_array:
                name = item['name']
                price_match = item['price']['original']
                price = float(re.sub(r'£', '', price_match))
                saleprice_match = item['price']['promotional']
                saleprice = float(re.sub(r'£', '', saleprice_match))
                if saleprice == price:
                    saleprice = None
                    sale = False
                else:
                    sale = True
                sizes = item['sizes']
                prod_url = f'https://www.zalando.co.uk/{item["url_key"]}.html'
                size_stock = [{"stock": "In stock", "size": size} for size in sizes]
                in_stock = False
                for size in size_stock:
                    if size['stock'] == 'In stock':
                        in_stock = True
                brand = item['brand_name']

                if in_stock:
                    yield scrapy.Request(
                            url=prod_url,
                            callback=self.parse,
                            meta={
                                'name': name,
                                'price': price,
                                'saleprice': saleprice,
                                'sale': sale,
                                'size_stock': size_stock,
                                'in_stock': in_stock,
                                'brand': brand,
                                'prod_url': prod_url
                            }
                        )

    def parse(self, response):
        kind_cats = [
            'accessories',
            'activewear',
            'backpack',
            'bag',
            'bags',
            'beachwear',
            'beauty',
            'belt',
            'bikini',
            'blazer',
            'blazers',
            'blouse',
            'blouses',
            'bodycon',
            'bodysuit',
            'boot',
            'boots',
            'bottom',
            'bottoms',
            'bra',
            'bracelet',
            'bralet',
            'bralette',
            'bras',
            'brief',
            'briefs',
            'brogues',
            'cami',
            'camis',
            'cardigan',
            'cardigans',
            'chinos',
            'clutch',
            'coat',
            'coats',
            'corset',
            'dress',
            'dresses',
            'dungaree',
            'dungarees',
            'earrings',
            'espadrille',
            'espadrilles',
            'hat',
            'heel',
            'heels',
            'hoodie',
            'hoodies',
            'jacket',
            'jackets',
            'jean',
            'jeans',
            'jeggings',
            'jersey',
            'jewellery',
            'jogger',
            'joggers',
            'jumper',
            'jumpers',
            'jumpsuit',
            'jumpsuits',
            'kimono',
            'knickers',
            'legging',
            'leggings',
            'lingerie',
            'lipstick',
            'loafers',
            'makeup',
            'mules',
            'necklace',
            'nightwear',
            'pant',
            'pants',
            'parka',
            'playsuit',
            'playsuits',
            'polo',
            'pullover',
            'pyjama',
            'ring',
            'sandal',
            'sandals',
            'scarf',
            'shirt',
            'shirts',
            'shoes',
            'shorts',
            'skirt',
            'skirts',
            'sneakers',
            'sock',
            'socks',
            'suit',
            'suits',
            'sundress',
            'sunglasses',
            'sweater',
            'sweatpant',
            'sweatpants',
            'sweatshirt',
            'sweatshirts',
            'swim',
            'swimming',
            'swimsuit',
            'swimwear',
            't-shirt',
            't-shirts',
            'tee',
            'thong',
            'tie',
            'tights',
            'top',
            'tops',
            'tote',
            'tracksuit',
            'tracksuits',
            'trainer',
            'trainers',
            'trouser',
            'trousers',
            'trunks',
            'tuxedo',
            'underwear',
            'vest',
            'vests',
            'waistcoat',
            'watch',
            'watches',
            'windbreaker',
            'workwear'
        ]
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
        style_cats = [
            'asymmetric',
            'bandeau',
            'bardot',
            'basic',
            'beach',
            'biker',
            'body',
            'bomber',
            'boxy',
            'boyfriend',
            'bridal',
            'broderie',
            'cargo',
            'casual',
            'chelsea',
            'chunky',
            'classic',
            'club',
            'cord',
            'crop',
            'cropped',
            'cross',
            'curve',
            'curved',
            'curves',
            'ditsy',
            'festival',
            'flare',
            'flared',
            'flat',
            'fluffy',
            'formal',
            'french',
            'fringe',
            'glamorous',
            'gym',
            'high',
            'homme',
            'large',
            'long',
            'longline',
            'loose',
            'lounge',
            'low',
            'mamalicious',
            'maternity',
            'maxi',
            'mela',
            'midi',
            'mini',
            'mom',
            'muscle',
            'oversized',
            'oxford',
            'pencil',
            'peplum',
            'petite',
            'pinafore',
            'platform',
            'pleated',
            'plunge',
            'plus',
            'push-up',
            'quilted',
            'raw',
            'regular',
            'relaxed',
            'retro',
            'ribbed',
            'ripped',
            'ruched',
            'running',
            'shirred',
            'short',
            'skater',
            'skinny',
            'sleeveless',
            'slim',
            'slinky',
            'slip',
            'smart',
            'south',
            'sports',
            'sporty',
            'stiletto',
            'straight',
            'strappy',
            'tailored',
            'tall',
            'tank',
            'tapered',
            'track',
            'training',
            'trench',
            'unisex',
            'vintage',
            'wedding',
            'western',
            'wide',
            'wrap'
        ]
        material_cats = [
            'beaded',
            'chiffon',
            'chino',
            'cotton',
            'denim',
            'down',
            'faux',
            'fishnet',
            'flannel',
            'glitter',
            'knit',
            'knitted',
            'leather',
            'linen',
            'merino',
            'metal',
            'metallic',
            'nylon',
            'paper',
            'pearl',
            'poplin',
            'puffer',
            'satin',
            'sequin',
            'studded',
            'suede',
            'suedette',
            'twill',
            'velour',
            'velvet',
            'viscose',
            'wool',
            'woven'
        ]
        attribute_cats = [
            'ankle',
            'back',
            'backless',
            'belted',
            'block',
            'bow',
            'buckle',
            'bust',
            'button',
            'buttons',
            'cameo',
            'cap',
            'chain',
            'collar',
            'crinkle',
            'cup',
            'double',
            'frill',
            'heeled',
            'hem',
            'hood',
            'hooded',
            'insert',
            'knee',
            'leg',
            'mid',
            'neck',
            'open',
            'pack',
            'padded',
            'panel',
            'panelled',
            'pocket',
            'pockets',
            'ruffle',
            'shoulder',
            'sleeve',
            'sleeves',
            'soft',
            'strap',
            'straps',
            'stretch',
            'sweat',
            'tassel',
            'trim',
            'turtle',
            'turtleneck',
            'twist',
            'underwire',
            'underwired',
            'up',
            'v-neck',
            'waist',
            'waistband',
            'waisted',
            'zip'
        ]
        filter_cats = [
            'curve',
            'curved',
            'curves',
            'tall',
            'plus',
            'petite',
            'mom',
            'mamalicious',
            'maternity',
            'bridal',
        ]
        all_cats = kind_cats + color_pattern_cats + style_cats + material_cats + attribute_cats + filter_cats

        item = ZalandoItem()
        item['name'] = response.meta['name']
        item['price'] = response.meta['price']
        item['saleprice'] = response.meta['saleprice']
        item['sale'] = response.meta['sale']
        item['size_stock'] = response.meta['size_stock']
        item['prod_url'] = response.meta['prod_url']
        item['in_stock'] = response.meta['in_stock']
        item['date'] = int(datetime.datetime.now().timestamp())
        item['currency'] = '£'

        if isinstance(response.meta['prod_url'], str):
            prod_id_hash_object = hashlib.sha1(response.meta['prod_url'].encode('utf8'))
            prod_id_hex_dig = prod_id_hash_object.hexdigest()
            item['prod_id'] = prod_id_hex_dig

        item['size_stock'] = response.meta['size_stock']
        item['brand'] = response.meta['brand']

        prod_json_string = response.xpath('.//script[contains(@id, "pdp-props")]/text()').extract_first()
        prod_json_string_clean_1 = re.sub('\<\!\[CDATA', '', prod_json_string)
        prod_json_string_clean_2 = re.sub('\]\>', '', prod_json_string_clean_1)
        prod_json = json.loads(prod_json_string_clean_2)

        category_match = prod_json[0]['model']['articleInfo']['category_tag']
        kind_cat_list = [word.lower() for word in category_match.split(' ') if word.lower() in kind_cats]
        cat_list = kind_cat_list
        if len(cat_list) == 0:
            all_cat_list = [word.lower() for word in category_match.split(' ') if word.lower() in all_cats]
            cat_list = all_cat_list
        item['category'] = cat_list[0]

        image_urls = [img_dict['sources']['gallery'] for img_dict in
                      prod_json[0]['model']['articleInfo']['media']['images'] if
                      img_dict['type'] == 'PREMIUM' or img_dict['type'] == 'DETAILED']

        item['image_urls'] = image_urls
        item['image_hash'] = []
        for img_string in image_urls:
            # Check if image string is a string, if not then do not pass this item
            if isinstance(img_string, str):
                hash_object = hashlib.sha1(img_string.encode('utf8'))
                hex_dig = hash_object.hexdigest()
                item['image_hash'].append(hex_dig)

        item['color_string'] = prod_json[0]['model']['articleInfo']['color']

        descr_match = response.xpath('.//div[@id="z-pdp-detailsSection"]/div/div/div/div/div/div/div/div/div').extract()
        descr_els = []
        for el in descr_match:
            # node = etree.tostring(el)
            # node_str = str(node, 'utf-8')
            node_clean_1 = re.sub('class=\".*?\"', '', el)
            node_clean_1_1 = re.sub('as=\".*?\"', '', node_clean_1)
            node_clean_2 = re.sub('\<\!--', '', node_clean_1_1)
            node_clean_3 = re.sub('--\>', '', node_clean_2)
            descr_els.append(node_clean_3)
        item['description'] = ' '.join(descr_els)

        categories = prod_json[0]['model']['articleInfo']['categories']
        categories_sex = [cat for cat in categories if cat == 'women' or cat == 'men']
        if len(categories_sex) > 0:
            item['sex'] = categories_sex[0]

            yield item
