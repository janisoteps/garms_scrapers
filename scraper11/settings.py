# -*- coding: utf-8 -*-

# Scrapy settings for scraper11 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scraper11'

SPIDER_MODULES = ['scraper11.spiders']
NEWSPIDER_MODULE = 'scraper11.spiders'


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
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 1
RETRY_TIMES = 0
# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cookie': 'browseMVT=nam-block-group90; geocountry=DE; check=true; browseCountry=GB; browseCurrency=GBP; browseLanguage=en-GB; browseSizeSchema=UK; storeCode=COM; currency=1; asos-b-sdv629=p1swt7e-15; test_cookie=test; AMCVS_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=1; asos-gdpr22=true; asos-perx=cfb54f88a3e54745a915315ce82ab8a3||1bcfd40dcc93452e9e1ab9dc849be26c; s_cc=true; bt_recUser=0; btpdb.ydg7T9K.dGZjLjcxMzA0Nzc=U0VTU0lPTg; btpdb.ydg7T9K.dGZjLjU3Njg1MjA=U0VTU0lPTg; btpdb.ydg7T9K.dGZjLjcwNTk5ODM=U0VTU0lPTg; bt_stdstatus=NOTSTUDENT; browseMVT=nam-block-group90; _fbp=fb.1.1554637584789.601635272; cto_lwid=db4c3047-4f3a-4b31-af32-66eb2bff8f64; _abck=6222325EDE65634C3951A2B675E02DCD58DDDD054868000086E2A95C2B0EB928~0~XgZ2+ATe5YWre0LfcYvq7XzExAWTsiod5T8iGwHXjgE=~-1~-1; floor=1000; asos=PreferredSite=&currencyid=1&currencylabel=GBP&customerguid=cfb54f88a3e54745a915315ce82ab8a3&topcatid=1000; __gads=ID=5c129af916d8dbe6:T=1554639141:S=ALNI_MY1Hz0xGAWmx9jg_rDTb4xuKjoltA; s_sq=%5B%5BB%5D%5D; bm_sz=11CD6689EABC4E8653C2AD44CBF7A9E5~YAAQBd3dWK/AzuFpAQAAisd/+AOoPawp0PeZb1HGcDkuH3+c34O2HQPkqeR7Tu9XMAL6IojWRClJjt6o5lYp10DiY5bES9pftHAyh2vVk8u1Op/sBTtfQCFKNCAFeOYo05ml7a6hxNjnNT4hW0Ssu8pfTFpPjtzXlorrVIZMVHylqU8iOpDPu+iug0Di4w==; siteChromeVersion=au=10&com=10&de=10&es=10&fr=10&it=10&nl=10&roe=10&row=10&ru=10&se=10&us=10; keyStoreDataversion=p1swt7e-15; plp_columsCount=fourColumns; AMCV_C0137F6A52DEAFCC0A490D4C%40AdobeOrg=-1303530583%7CMCIDTS%7C17994%7CMCMID%7C06640552785408282730272795733520164425%7CMCAAMLH-1555257119%7C6%7CMCAAMB-1555257119%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1554659519s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.3.0%7CMCCIDH%7C0; _s_fpv=true; ak_bmsc=2B4E90CF717CCC6F1959934952EDAA6858DDDD05486800009D1CAA5CAEAF3F6D~plqdwGQ5cC4/JlwTrodwWAhINTKsPSU56P98Y96ZJMPLQygoBAEGEFAOy2s5PaYEXvDzr9O2nCUd28gK8nPJj6QA4nSE2CWyCQpHewT2qDD6eBbSmsHBFYOL57eGCm3Px4JuSoxiK87Vhd4zmwAQzpKOe7STmLy+Ltixy2IxFt/d9sHDQK7ABul53whwUKKhWw/MCUtNVdgI3gMWBDo0WIIoI44a+s4FTDtiDqDbXSfxOJFT/rWmnfz2H4ZAbDGGdq; mbox=PC#eacea3cad37841428b83b849d76c9274.26_19#1617897118|session#474ae7385906432b8af5e54b18dcc90a#1554654499; bm_sv=7683BF03395A22AED04415880C76599D~zbsnHh9G7aQ7Mk0aFXBbjTsE28On/K5B8I3XvbUNlZAqMXYTJ+FSH/3b1FITiJTCFSN8rjG5Q2bDXSGHDISLjcc2AvaTxgJL9nIA3f/E6a7neXv+1b5kY98h4/RqnBh8tAW5kExHSGGfUVoJThfGoQ==; s_pers=%20s_vnum%3D1556665200342%2526vn%253D2%7C1556665200342%3B%20s_invisit%3Dtrue%7C1554654439466%3B%20s_nr%3D1554652639475-Repeat%7C1586188639475%3B%20gpv_p10%3Ddesktop%2520com%257Cfloor%2520page%257Cwomen%7C1554654439476%3B%20gpv_p6%3D%2520%7C1554654439478%3B%20gpv_e47%3Dwomen%257Chome%7C1554654439479%3B',
    'pragma': 'no-cache',
    'referer': 'https://www.asos.com/',
    'upgrade-insecure-requests': '1'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scraper11.middlewares.Scraper11SpiderMiddleware': 543,
#}

# PROXY
PROXY = 'http://127.0.0.1:8888/?noconnect'

# SCRAPOXY
API_SCRAPOXY = 'http://127.0.0.1:8889/api'
API_SCRAPOXY_PASSWORD = 'Kurlasmaskas3345'

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

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'scraper11.pipelines.Scraper11Pipeline': 300,
#}

ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}

IMAGES_STORE = '/home/jdo/jdev/scrapers/img_uk/asos_uk_1'

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 0
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 5
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# HTTPERROR_ALLOWED_CODES = [403]
