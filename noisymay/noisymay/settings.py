# -*- coding: utf-8 -*-

# Scrapy settings for noisymay project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'noisymay'

SPIDER_MODULES = ['noisymay.spiders']
NEWSPIDER_MODULE = 'noisymay.spiders'


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
    'cookie': '__cfduid=d24d068113b31bf517ab1ae9ef96c5dd51577707171; __cq_dnt=0; dw_dnt=0; dwanonymous_4887ae275d2e3149dd6a6534fdd472df=abYE6YkyBPG7yF0FcYS5tiuoTK; dwac_bc082iaaiTywMaaadqlmYUVd5G=VP0qIhrI5ogqrkXLgiZzTeg4eFyTuF7m1xI%3D|dw-only|||EUR|false|Europe%2FAmsterdam|true; dwsecuretoken_4887ae275d2e3149dd6a6534fdd472df=Q-JV78G2bhPgfU_xMYWe2ANzlDcpJMZsHw==; mt.v=2.2099170123.1577707188214; dw_cookies_accepted=1; mt.pc=2.1; _gcl_au=1.1.1332640076.1577707189; mt.g.829f7900=2.2099170123.1577707188214; _ga=GA1.2.2114291612.1577707189; _gid=GA1.2.1727498562.1577707189; __cq_uuid=d81b0bb0-c018-11e9-b6cd-25e4f7339976; customer_club_closed=true; _ga_cookie=VP0qIhrI5ogqrkXLgiZzTeg4eFyTuF7m1xI; dwanonymous_982e1e223e55662daee7d57e25e7fcbe=abkHVe7TmzGw4pIX0yx9xVWeNv; __cq_bc=%7B%22abbt-BSE-South%22%3A%5B%7B%22id%22%3A%2227000430%22%7D%5D%7D; tfc-l=%7B%22a%22%3A%7B%22v%22%3A%22b6a25f19-3715-427f-af0f-6537aae18ce1%22%2C%22e%22%3A1577794171%7D%7D; sid=DdVt9MxTXWhjjaL6ODIfnuq4DCNo5kCVquk; dwsid=msRSJsKqjTogfCt44u3rQH2pM_FmH5DH6RjnjAlgSpXIIEh0hYx0SphckDjDYEw9CkgT_fnGUKw_fGWuI6MIOQ==; dwanonymous_91b08f347cfea20452b0e969603162ea=acl14ydlTWfmy9xaxlGBOLYrcw; dwac_49c0f6ae5a5eb5be1f9fbe29ac=DdVt9MxTXWhjjaL6ODIfnuq4DCNo5kCVquk%3D|dw-only|||EUR|false|Europe%2FAmsterdam|true; dwsecuretoken_91b08f347cfea20452b0e969603162ea=CPQSS9Raga1bApK3S8EUCEi3PMGWqu7gWQ==; dwac_bcJ6oiaaiTPCaaaadq9ngUVd5G=DdVt9MxTXWhjjaL6ODIfnuq4DCNo5kCVquk%3D|dw-only|||EUR|false|Europe%2FAmsterdam|true; dwsecuretoken_982e1e223e55662daee7d57e25e7fcbe=CbM9C01fXJ8a62tSjlqFHJ1oeTz4lkcA7g==; cqcid=abkHVe7TmzGw4pIX0yx9xVWeNv; AMP_TOKEN=%24NOT_FOUND; _dc_gtm_UA-66188758-43=1; _dc_gtm_UA-66188758-20=1; __cq_seg=0~0.47!1~0.07!2~0.05!3~0.23!4~-0.06!5~-0.25!6~0.06!7~-0.54!8~-0.56!9~0.22',
    'pragma': 'no-cache',
    'referer': 'https://www.noisymay.com/gb/en/home',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'noisymay.middlewares.NoisymaySpiderMiddleware': 543,
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

IMAGES_STORE = '/home/janis/dev/garms_data/data_uk/noisymay_uk/images/dec_2019'

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 2
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 20
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 2.0
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
