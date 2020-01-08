# -*- coding: utf-8 -*-

# Scrapy settings for neverfullydressed project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'neverfullydressed'

SPIDER_MODULES = ['neverfullydressed.spiders']
NEWSPIDER_MODULE = 'neverfullydressed.spiders'


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
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,lv;q=0.8',
    'cookie': '__cfduid=dfe2ec2b5ef383e262a353e07fc4ddde81576845723; secure_customer_sig=; _landing_page=%2Fcollections%2Fdresses; _shopify_y=d09b0828-fee6-463c-ad0b-a8e84b3263f8; _orig_referrer=; cart=161a0377d792f3c95810c584e0242c15; _shopify_country=Germany; _y=d09b0828-fee6-463c-ad0b-a8e84b3263f8; _s=2354528f-4DED-4398-4FB1-11A11BF79BA7; _shopify_s=2354528f-4DED-4398-4FB1-11A11BF79BA7; _shopify_fs=2019-12-20T12%3A42%3A04.738Z; _shopify_sa_p=; cto_lwid=600edc5e-6502-4bf0-abc1-c69b725b98a2; currency=GBP; __adal_ses=*; __adal_ca=so%3Ddirect%26me%3Dnone%26ca%3Ddirect%26co%3D%28not%2520set%29%26ke%3D%28not%2520set%29; __adal_cw=1576845725453; _ga=GA1.3.1000031196.1576845726; _gid=GA1.3.2061175016.1576845726; _gat=1; lc_sso9825745=1576845726336; __lc.visitor_id.9825745=S1576845725.b9d2d0d67f; lc_window_state=minimized; usb_previous_pathname=/collections/dresses; fsb_previous_pathname=/collections/dresses; fsb_total_price_227344=0; KL_FORMS_MODAL={%22disabledForms%22:{%22QCBhbd%22:{%22lastCloseTime%22:1576845741%2C%22successActionTypes%22:[]}}}; cart_sig=; cart_currency=GBP; cart_ts=1576845749; _shopify_sa_t=2019-12-20T12%3A42%3A30.588Z; __adal_id=ed2cc915-c18b-4df5-a3a1-b16262266eb2.1576845725.1.1576845751.1576845725.92140d2d-648d-46fa-891b-3fd9cbd7e0bf; __kla_id=eyIkcmVmZXJyZXIiOnsidHMiOjE1NzY4NDU3MjYsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3Lm5ldmVyZnVsbHlkcmVzc2VkLmNvLnVrL2NvbGxlY3Rpb25zL2RyZXNzZXMifSwiJGxhc3RfcmVmZXJyZXIiOnsidHMiOjE1NzY4NDU3NTIsInZhbHVlIjoiIiwiZmlyc3RfcGFnZSI6Imh0dHBzOi8vd3d3Lm5ldmVyZnVsbHlkcmVzc2VkLmNvLnVrL2NvbGxlY3Rpb25zL2RyZXNzZXMifX0=',
    'referer': 'https://www.neverfullydressed.co.uk/',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'neverfullydressed.middlewares.NeverfullydressedSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'scrapoxy.downloadmiddlewares.blacklist.BlacklistDownloaderMiddleware': 950,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_useragents.downloadermiddlewares.useragents.UserAgentsMiddleware': 500,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}

IMAGES_STORE = '/home/janis/dev/garms_data/data_uk/neverfullydressed_uk/images/dec_2019'

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 30
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 3.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

HTTPERROR_ALLOWED_CODES = [404, 403]