# -*- coding: utf-8 -*-

# Scrapy settings for uniqlo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'uniqlo'

SPIDER_MODULES = ['uniqlo.spiders']
NEWSPIDER_MODULE = 'uniqlo.spiders'


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
    'cookie': 'OptanonAlertBoxClosed=2020-02-24T05:47:24.678Z; OptanonConsent=isIABGlobal=false&datestamp=Mon+Feb+24+2020+06%3A47%3A24+GMT%2B0100+(Central+European+Standard+Time)&version=5.6.0&landingPath=NotLandingPage&groups=0_50971%3A1%2C1%3A1%2C0_50972%3A1%2C2%3A1%2C0_50975%3A1%2C3%3A1%2C4%3A1%2C0_50969%3A1%2C0_50968%3A1%2C0_50967%3A1%2C0_50966%3A1%2C0_50965%3A1%2C0_53717%3A1%2C0_50963%3A1%2C0_50962%3A1%2C0_50973%3A1%2C0_50970%3A1; __cfduid=dbdc4fb7e465ec62c4cc5cb65897ba7881582523233; dwac_3201ce5c4e7bf5630633c3e425=mAOs8MV1zXgTvUL4mWBTMlK6-Cu0zr0V6nE%3D|dw-only|||GBP|false|Europe%2FBerlin|true; cqcid=adu6ws6VTAd1bqSMGA4dauIK8O; sid=mAOs8MV1zXgTvUL4mWBTMlK6-Cu0zr0V6nE; geoSite=IT; dwpersonalization_8af1144abc5a7219343b18330f0adea9=11065e4207b1629861b0bd7dff20200226000000000; dwanonymous_8af1144abc5a7219343b18330f0adea9=adu6ws6VTAd1bqSMGA4dauIK8O; __cq_dnt=0; dw_dnt=0; dwsid=CkXq21MY6QmZT-_-6gtfxMD8vgAio5lkYIPOQh0osyynOopFDAh_BzlsJbMWdBoMZHiRB-4ycXuFN8xFnq_dYg==; bm_sz=FC01FC103869196B4016E7C37CC14BA9~YAAQBfAWAm5SHWpwAQAAFTi8dQa61wVUJeYjvJMS4hoCCNrEQZqMT0BENJITw7XkYSCvDQFUkSvbi1G4TVDXIT6nBr4D/4gwD3kFPQmi/9ljpQo2Qft0F8ijwMbqn9Q/dkpcKk7/6FKRQxd2KU8l3pFgZ7HaideP5TMG/YjFaWj768niBME5LTMf/IZAZnXX; _ga=GA1.2.906641138.1582523235; _gid=GA1.2.1945931590.1582523235; _gcl_au=1.1.1591417003.1582523235; _mibhv=anon-1582523235884-8456175242_8273; _micpn=esp:-1::1582523235884; _ALGOLIA=anonymous-b8da3a88-45f4-4875-8bd5-edbacb1f516a; dw=1; dw_cookies_accepted=1; ak_bmsc=439CD5A118119D634FE29D9E549348370216F0059B7000006263535EE07A2557~plp9aGyk+EMA/095hrxiMS2yKx5jnDJ0b65W66lHan+JYVuGhyad9orlyCxIQTdCNuUYe8rRiYE5i95vwEzdPpl+KIxpiZeX+YHdtFolZxEIkqU3ECOFNlga51pVKP3bXBqNhwAAP1x7PZtUFzH/nziSOnvwkemGP3jy41X+TymiiawUDSTTFRiBHOXY6rLEdXqXEY8wUEpURHJSOMYaUCk9hIIRvZx2tkUeox//1y/Bj9dDVj1klcL/YdwcqYfQoq; _abck=D6F3887E65647CD64034118E5ED67414~0~YAAQBfAWAnFSHWpwAQAAZ0u8dQN2UrYqudlXWrJhRs+rhLBGxya1ipEXthtjwAcZHSs8OuQCipx/2Z7R7OTsUKr1S4wt4gTUh8rSC/tAHSRKExTBSJRtNZCZMZ4tiQmFkjRyQbP7hK8XJWqry2ZdIhvwsu1j0cCMbHufiteMhp7s+y0RzBfhnu3h+z1pC8vnmD/hkZ7VYFGomWo0HkYAg4PQkrvOrhY6moms2s9dANjhf/w7GRKdDuG4dU3XkGcXM5nfNHFFifs7gHbYUkX+e+XcK5AdHU+sTI8LkJ6nLG2YUYssGsOvT8cLW/MSilslYI7yvnhmuw==~-1~-1~-1; __cq_uuid=d81b0bb0-c018-11e9-b6cd-25e4f7339976; __cq_seg=0~0.00!1~0.00!2~0.00!3~0.00!4~0.00!5~0.00!6~0.00!7~0.00!8~0.00!9~0.00; sc.InTg=a; sc.ASP.NET_SESSIONID=v0exfq0b3qhrvxu0p5xmnykw; bounceClientVisit3083v=N4IgNgDiBcIBYBcEQM4FIDMBBNAmAYnvgO6kB0ArgHYCWAjmAPZkDGjAtkRQNZECmVInA58QAGhAAnGCFLEyAc0aMFYPq2Y8QAXyA; bm_sv=459FAF2108CBD2FB5F94CC7B41CC572E~13YlTf7pbHjZZoJpFFijY2CK3BUBVxOMshF8EsCGdBddKWLfCZLZCAdY9Mm17AulZme/i/PQIcGGDa5O8aL81D2TgxZ3R04Y48FE2oMOemzYW17ZvkxDZHWc8MarzJUfrc46Ry5zoNx/w4qeLNNM/jNXZfWlveFcPwCnoms6j2g=; _gat_UA-1566247-1=1',
    'pragma': 'no-cache',
    'referer': 'https://www.uniqlo.com/uk/en/home',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'uniqlo.middlewares.UniqloSpiderMiddleware': 543,
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

IMAGES_STORE = '/Users/janis/dev/garms_data/data_uk/uniqlo_uk/images/2020_feb'

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
