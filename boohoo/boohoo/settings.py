# -*- coding: utf-8 -*-

# Scrapy settings for boohoo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'boohoo'

SPIDER_MODULES = ['boohoo.spiders']
NEWSPIDER_MODULE = 'boohoo.spiders'


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
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 1
#CONCURRENT_REQUESTS_PER_IP = 16
RETRY_TIMES = 0

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,lv;q=0.8',
    'cache-control': 'no-cache',
    'cookie': '__cfduid=de6bab5f9b68cb380ef4b941545ef25eb1560717279; dwac_901934c2df27fe61a1e3d786c2=P5kOg8ksRdY4FNCsE33SGW63EtPWjruw3Ic%3D|dw-only|||GBP|false|Europe%2FLondon|true; cqcid=ac4G2blima1O28eecvkX8f8Q6R; sid=P5kOg8ksRdY4FNCsE33SGW63EtPWjruw3Ic; dwanonymous_3c96516478c33a12ebf223e921102926=ac4G2blima1O28eecvkX8f8Q6R; __cq_dnt=0; dw_dnt=0; dwsid=OWc0R1QfI8VvEC2-yw3jbWhJKBdLvd2ji4MqFJ7H12Vh4DaFMTg_YkQNp1HbaKM_nvYsNmrjPDCYYVBqNU-PyA==; mt.v=2.668808714.1560717288370; locationProtocol=https%3A; _gcl_au=1.1.1180915791.1560717290; __adal_first_visit=1560717290174; _ga=GA1.2.1094295532.1560717290; _gid=GA1.2.1918252411.1560717290; _scid=e9b4b24f-5cbd-4e52-9e40-a8e2197336b6; cd_user_id=16b61ffebb163f-0a6be026537f59-37647e03-232800-16b61ffebb252e; __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; _cs_c=1; _fbp=fb.1.1560717290889.1104685392; riTrack_WRSID=1560717293029544604; cto_lwid=c2f1d4a0-58d8-4a51-9129-f4539767a8fa; dw_locale=en_GB; __cq_uuid=ccdcf580-d6ce-11e8-af72-ef24856155e0; dwsecuretoken_3c96516478c33a12ebf223e921102926=ggHn-BU4Ko_lGpii1HkrnDP-YiDUfP4psA==; __adal_session_start=1560724388629; __adal_last_visit=1560724388629; C360i=242D6DB82A99425B9532965155D13D12|eyJjcmVhdGVkIjoxNTYwNzE3MjkwNjYwLCJ1cGRhdGVkIjoxNTYwNzI0Mzg4Nzg0LCJ0YWciOiIyLTIuMjQtNiIsImNvdW50Ijo2LCJldGFnIjoiNjk2MDkyNzE3MDY1MTA0NDU5MDAwMDAwMzU5ODNiMWQwN2QxNGVjMDc0YjdlOTdkNDAyMGU0YjhjNDNlIn0=; C360i=242D6DB82A99425B9532965155D13D12|eyJjcmVhdGVkIjoxNTYwNzE3MjkwNjYwLCJ1cGRhdGVkIjoxNTYwNzI0Mzg4Nzg0LCJ0YWciOiIyLTIuMjQtNiIsImNvdW50Ijo2LCJldGFnIjoiNjk2MDkyNzE3MDY1MTA0NDU5MDAwMDAwMzU5ODNiMWQwN2QxNGVjMDc0YjdlOTdkNDAyMGU0YjhjNDNlIn0=; _cs_id=e8c4a580-fe87-a8cb-bf2f-24e89f4f7e98.1560717290.5.1560766227.1560766227.1499948428.1594881290777; _cs_s=1.0; dw=1; dw_cookies_accepted=1',
    'pragma': 'no-cache',
    'referer': 'https://www.boohoo.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'boohoo.middlewares.BoohooSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#     'scrapoxy.downloadmiddlewares.blacklist.BlacklistDownloaderMiddleware': 950,
#     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#     'scrapy_useragents.downloadermiddlewares.useragents.UserAgentsMiddleware': 500,
# }
DOWNLOADER_MIDDLEWARES = {
    'scrapoxy.downloadmiddlewares.blacklist.BlacklistDownloaderMiddleware': None,
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
#    'boohoo.pipelines.BoohooPipeline': 300,
#}

ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}

IMAGES_STORE = '/home/janis/jdev/scrapers/img_uk/boohoo_uk_1'

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 20
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
