# -*- coding: utf-8 -*-

# Scrapy settings for topshop project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'topshop'

SPIDER_MODULES = ['topshop.spiders']
NEWSPIDER_MODULE = 'topshop.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'

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
    'cache-control': 'no-cache',
    'cookie': 'bm_sz=787EAD0F7C4B225BF89B711F99FC89C5~YAAQHbsQAh5ii6BuAQAA0v+cfwZh/2+rK6QYlP5kHEdEBDM8UM/DUOjum4mQWBA/BbeklrnTB/86xdMY4PSRCNZBBF7C9NKvwlZ3fHyG/J42OJQoOPeUdJfadY9SOX6ILzVD92mZodCcYAhGwe+QVUg3vJPYk0G956NRlrEJtF31Ms23jyR58D66NUAr35aCDQ==; _blka_uab=45; deviceType=desktop; _gcl_au=1.1.1244171170.1578394001; new_returning_customer=N1578394001429; userId=unspecified; _abck=6AC9134EEEDD2D7AE5099E9C22EE768E~0~YAAQHbsQAihji6BuAQAANiCdfwNHUmtwplCnsbjbaz5zPKusBrSHXgcivEk6/g9QpGdPbpqsAF4qjSIPmokYJM0ypiY2k4O3vdUZeJ/ewBXJ9/IaT/Q8+T7Sz1H4gvyMAauecWKMhRPVH6jmbVBk2209eNkh7sx+ilveRDDHLWTVuSrBcTBzaiLwhhW9JN0T69xf96ASo/5MZRsFIsWDN/knK5T2TWHn3YEkPR8QR0/e1Nd/Jq8m36m7yxVwLkz7qdMizv4CBZnX7KhvGeJrDO09JP+t14CQUWNMSESYPoIJmc/4mMSStxDoldOXczsDBImAMnjFkNw=~-1~-1~-1; peerius_sess=119866084813|942GKDdVZ6xjEW4J4bhAZ2mU8Rb4It0apWMlFz2AyDw; peerius_user=cuid:75168310513|XrYjIeIX2j24alXNkcRSl13Lx16NrZBwJjjCC1Hy1oc; _ga=GA1.2.1493720660.1578394002; _gid=GA1.2.641844300.1578394002; _scid=3ea60883-2f67-41d9-974a-332e2c6b8117; ak_bmsc=8ECA00B9D479C686BA6CE77EB26630FA0210BB1D2A4900008961145ECB7F1234~plxjHWaSPdS0Sgu4BO2BGI4xzERD5EP1Za8vRcYtnM0KUmDcEfVJAjGjmlFBy9GKo+4aVF4ByZ0KDfypjhlJzL2snM8EiE95wmU1H6ImcXcN//yP/YVplYUrXSF8LgvTbIxVsZqAOXYr7wqiX6FEWpCa5IkNUkalt5TLe4g8T4+4Acw+jmtcCJlFdBnyyw6bTr0mJJ6qibFIZLof26FCvgqPRKmzn+gU9ddWOiVY9bT+IMqk8aa+vrl/hOeiwqqJOF; _derived_epik=dj0yJnU9UXA0XzZndG9sSDJRMXpNbFpOWmprY2IteDRtQTI3N1Embj1VWFB6NHdBMnFLVjVRS0FQVmx6UnZBJm09MSZ0PUFBQUFBRjRVWVpJJnJtPTEmcnQ9QUFBQUFGNFVZWkk; _hjid=e3aa1902-572f-4ea2-862e-a7d1830aebc3; TLTSID=58864215198174902923825843741217; GEOIP=GB; source=CoreAPI; tempsession=true; notice_preferences=3:; notice_gdpr_prefs=0,1,2,3::implied,eu; cmapi_gtm_bl=; cmapi_cookie_privacy=permit 1,2,3,4; traceId2=1578394027951R595981; __exponea_etc__=0d2ecee1-313b-11ea-b2a8-8ab630c69043; __exponea_time2__=0.015987873077392578; jsessionid=eyJhbGciOiJIUzI1NiJ9.MTUzZDBlZjQtZGZhMS00Y2Y5LWJjNjItNmI2NWFhODJjZDc5.K3x5SjKL3abM92smNYMnUkKNBYhhAq2b4Q7LJPdKnNc; akavpau_VP_TS=1578394465~id=5fac10c37cd36703cbb2000288f6f8d0; bm_sv=B6C97F78E03F9A83BF7464E129AD5F46~0HJ1r15DcLZnrMxbNou2xo+OjsG/B0QkvQiRwUM3uhyOgQa0j/dfkEkNPPX5mr9hvOiimXwvdZRcNj6FQCR52dUsd6lIwFV0Q+C63WkGUK+9psK3UzES9TlWTnjQEs33bkKqPsQh6FnWMW03nPOHq8O1j1SMQJ/ePXxl6gUF87M=; _dc_gtm_UA-99206402-1=1',
    'pragma': 'no-cache',
    'referer': 'https://www.topshop.com/',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'brand-code': 'tsuk'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'topshop.middlewares.TopshopSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
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

IMAGES_STORE = '/home/janis/dev/garms_data/data_uk/topshop_uk/images/dec_2019'

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
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
