
# -*- coding: utf-8 -*-

# Scrapy settings for asos project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'asos'

SPIDER_MODULES = ['asos.spiders']
NEWSPIDER_MODULE = 'asos.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/72.0.3626.119 Safari/537.36 '

USER_AGENTS = [
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
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 8

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 1
#CONCURRENT_REQUESTS_PER_IP = 16
# RETRY_TIMES = 0

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cookie': 'browseMVT=nam-block-group90; browseCountry=GB; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=COM; currency=1; gig_hasGmid=ver2; cto_lwid=133f4beb-229b-4d0e-a0fb-ccc9c88c5761; _gcl_au=1.1.956884994.1556384015; _fbp=fb.1.1556384015375.952917663; _ga=GA1.2.1410495741.1556384015; welcomeMessageClosed=true; plp_columsCount=fourColumns; fita.sid.asos=vN-3PNSjdvI18kyaugnOmnhRYZAl00Uj; floor=1000; asos=PreferredSite=&currencyid=1&currencylabel=GBP&customerguid=adf51689030e4b0e9bcefafd964f09b7&topcatid=1000; _abck=EA800BBB9649B6419ED6A700C356A466~0~YAAQVW3UF3sfIA5rAQAAjKzZGAFB8osDT/93aPQ6cFtQ2GqegvWxbw4J74hZzAJvfITl3cQkMMLXdsc2MyiJPaIIFQTy6TnEuQNwsWRbjdP+sm3Mtcyo0fsdWhQUwuZN+R1olE+Exbbbcdd2VUB3EGEG0/YJAzljpa1uAZpFHE+0pbFhKxtnuwLEmJ9nTvPqT2enSsW6Pmtrf3UxlnH10/vZrcGPJirSSv/USd+yFjveLE/UdMH/BKyud8TNTyS0sbFdJPPpjKhfiKKJSNKlW1ZKF/A8Y6NVTX67RgixDtaocINZ2aQf~-1~-1~-1; geocountry=DE; bm_sz=2A234C595B5025042980A28E27BBD33E~YAAQjrUQAvscEmhvAQAAsDiWiQYl+UUcXNl9VsOPfVVt16J5IBECJgmY8egmEC0/TxcQ0aQlMBlKTdQcf2HjmxwLGIrb5P1k4kZwZRknc6QEZh2OZH3jiGvCorixEV1a02jzM48jMJaEmS0A5x9r9LkNoi4Nr4MtZoJc5M5PSX1dwpNU/jsNWr1YcaMm/w==; ak_bmsc=51FFC5E0E5237EFD5DE00F98CD14ECEB0210B58EB91F000029EF165E3287713B~plo7vt+Cqf7TAwalPA6bJ994ojy0nlSt2R3lhU24HsejuwFGA0oJKnATQ6McIOwD/5sVha98Ie21aTy8OYDQz4J6uQzC/k8UryvD1uXfQWmUCtav6m/hqVqcvWUUdjrx6xXfFWQX4Y6QeTf7KEAaTEuo55kz/aeaqNY6zKfMeYULEYie5uq2Zmx36tVeWM4IHRR272wXY69hJmv8dp2CA8kvCI69K4kTPG4WWp/u+HyHlAZTnaAauFC7YYzugLqDIllXXAOwFifi15bN1BLX91H67wmwZpvE+UESOVA0C51t2hsmHNzK7KKSgcZw9DXIVs1uaDVpZ9dj+6BSLXjQ3Ybg==; check=true; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCIDTS%7C18271%7CMCMID%7C48129871169395856320527775713080436586%7CMCAAMLH-1579166123%7C6%7CMCAAMB-1579166123%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1578568523s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.3.0%7CMCCIDH%7C0; siteChromeVersion=au=11&com=11&de=11&dk=11&es=11&fr=11&it=11&nl=11&pl=11&roe=11&row=11&ru=11&se=11&us=11; keyStoreDataversion=jqvkhhb-21; asosAffiliate=affiliateId=17295; asos-gdpr22=true; asos-b-sdv629=jqvkhhb-21; test_cookie=test; mbox=PC#38676d7982a441599efab39e14c52361.26_55#1641806124|session#5b16e1f461f24bfdbd8d91217e63b1e6#1578563185; asos-perx=9e30deef028247c58ed58be93d9cf2a6||6e7719dd71e44a84a9c35436f25fe706; s_pers=%20s_vnum%3D1580511600911%2526vn%253D1%7C1580511600911%3B%20s_invisit%3Dtrue%7C1578563124911%3B%20s_nr%3D1578561324917-Repeat%7C1610097324917%3B%20gpv_p10%3Ddesktop%2520com%257Cfloor%2520page%257Cwomen%7C1578563124921%3B%20gpv_p6%3D%2520%7C1578563124925%3B%20gpv_e47%3Dwomen%257Chome%7C1578563124928%3B; _s_fpv=true; s_cc=true; bt_recUser=0; btpdb.ydg7T9K.dGZjLjcxMzA0Nzc=U0VTU0lPTg; btpdb.ydg7T9K.dGZjLjU3Njg1MjA=U0VTU0lPTg; bt_stdstatus=NOTSTUDENT; btpdb.ydg7T9K.dGZjLjcyMzUwNjA=U0VTU0lPTg; btpdb.ydg7T9K.dGZjLjcwNTk5ODM=U0VTU0lPTg; _gid=GA1.2.1450734469.1578561325; _gat=1; _derived_epik=dj0yJnU9X1pUd0dQY2VHTThhUU9CQldieXpsUVB6TkVfRHdJdEwmbj1FWW43NGRMNE1xQkpRUkVGeEpCMU13Jm09NyZ0PUFBQUFBRjRXN3kw; s_sq=asoscomprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Ddesktop%252520com%25257Cfloor%252520page%25257Cwomen%2526link%253DShoes%2526region%253D1020946c-8949-4e9c-9719-43435002bcd4%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c',
    'pragma': 'no-cache',
    'referer': 'https://www.asos.com/',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'asos.middlewares.AsosSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'asos.middlewares.AsosDownloaderMiddleware': 543,
#}

# PROXY
PROXY = 'http://127.0.0.1:8888/?noconnect'

# SCRAPOXY
API_SCRAPOXY = 'http://127.0.0.1:8889/api'
API_SCRAPOXY_PASSWORD = 'Kurlasmaskas9921'

# BLACKLISTING
BLACKLIST_HTTP_STATUS_CODES = [503, 403]

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'scrapoxy.downloadmiddlewares.proxy.ProxyMiddleware': 100,
    'scrapoxy.downloadmiddlewares.wait.WaitMiddleware': 101,
    'scrapoxy.downloadmiddlewares.scale.ScaleMiddleware': 102,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
    'scrapoxy.downloadmiddlewares.blacklist.BlacklistDownloaderMiddleware': 950,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_useragents.downloadermiddlewares.useragents.UserAgentsMiddleware': 500,
}

# DOWNLOADER_MIDDLEWARES = {
#     'scrapoxy.downloadmiddlewares.blacklist.BlacklistDownloaderMiddleware': 950,
#     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#     'scrapy_useragents.downloadermiddlewares.useragents.UserAgentsMiddleware': 500,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'asos.pipelines.AsosPipeline': 300,
#}

ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}

IMAGES_STORE = '/Users/jdo/dev/garms_data/data_uk/asos_uk/images/2019_dec'

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 0
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 5
# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
