# -*- coding: utf-8 -*-

# Scrapy settings for farfetch project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'farfetch'

SPIDER_MODULES = ['farfetch.spiders']
NEWSPIDER_MODULE = 'farfetch.spiders'


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
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,lv;q=0.8',
    'cookie': 'ckm-ctx-sf=/uk; FF.Session=uunraxuupaocz1wlof0ej4zv; ub=; BIcookieID=e860665f-ab76-4a76-b17b-bb1ae0ac5a22; checkoutType2=4; FF.ApplicationCookie=_1T6cQ4vyM8hLahPDj0u-TMpuQSqeemF4T4T_zu5Soeqm4B6T055f4u7yDG9FN5bfk8InodRIyLO96u3ATpA4j6UE-8n6vILVgwX6SlDY44DrzLZ1z4deaU4fSgEzjM-I0l-F04HQp8mEPm4FtiM_EF0RlaH8D3CIBYLTLpvQ0REoMD9klN1MgFnZe5Z7BQmUuSO40JfKEcrvLkrWoNXr27SNiuYv-OVy6FQIcON4Rj0lKCr; ABProduct=; ABListing=122:1#35:2; ABLanding=139:0; ABCheckout=; ABReturns=; optimizelyEndUserId=a1e11602e2490000ec58165d4f02000008780000; session#1=uunraxuupaocz1wlof0ej4zv; usr-gender=0; grtng-mssg={"isToDisplay":false,"type":2}; ABGeneral=135:1#145:0#155:0#156:1#301:0#302:0#322:1#472:1#473:0#952:1; _gcl_au=1.1.394411917.1561745647; _ga=GA1.2.85874619.1561745647; _gid=GA1.2.188663186.1561745647; lastRskxRun=1561745647693; rskxRunCookie=0; rCookie=tphoffnbxemimabdpy3xi; RES_TRACKINGID=10566330774654716; ResonanceSegment=; RES_SESSIONID=33929490774654716; _gat_UA-3819811-6=1; af_load=1561745647755; _scid=87a748f1-06b3-4c84-8338-f8d6f69e49df; cto_lwid=6adc7ef5-3bf2-4ee8-b5b9-ae214a743483; _derived_epik=dj0yJnU9dG9YODdHNkM5NzNOb2Y1eTBxMFEtcXNMZ2xOdFpWZHgmbj1VZTFuTVp4bE9WV3FwTXF3WktweE1nJm09NyZ0PUFBQUFBRjBXV084; _fbp=fb.1.1561745647952.1665486557; af_id=b670f330-7b4b-4c48-a392-e90c3b85044a; ORA_FPC=id=90ed76a2-adcb-4afe-988b-cba757f91e3b; WTPERSIST=; _qst_s=1; _qsst_s=1561745648341; _qubitTracker=1561745648401.837804; _qubitTracker_s=1561745648401.837804; _qst=%5B1%2C0%5D; _qPageNum_farfetch=0; _qsst=1561745648411; qb_session=1:1:12::0:WufS25U:0:0:0:0:.farfetch.com; qb_permanent=1561745648401.837804:1:1:1:1:0::0:1:0:BdFljx:BdFljx:::::82.21.239.54:southwark:2788:united%20kingdom:GB:51.4825:-0.095375:itv%20london:826044:southwark:25527:migrated|1561745649791::B:WufS3B/:WufS25U:0:0:0::0:0:.farfetch.com:0; __cid=6dc710c3-0847-4635-8b51-b54438e47a06-1765b2f965ec6a6157652a28; af_unload=1561745658269',
    'pragma': 'no-cache',
    'referer': 'https://www.farfetch.com/',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'farfetch.middlewares.FarfetchSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'scrapoxy.downloadmiddlewares.blacklist.BlacklistDownloaderMiddleware': 950,
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
ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}

IMAGES_STORE = '/home/janis/dev/garms_data/data_uk/farfetch_uk/images/dec_2019'

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


HTTPERROR_ALLOWED_CODES = [404, 403]
