# -*- coding: utf-8 -*-

# Scrapy settings for zalando project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zalando'

SPIDER_MODULES = ['zalando.spiders']
NEWSPIDER_MODULE = 'zalando.spiders'


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

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zalando.middlewares.ZalandoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zalando.middlewares.ZalandoDownloaderMiddleware': 543,
#}
DOWNLOADER_MIDDLEWARES = {
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
#    'zalando.pipelines.ZalandoPipeline': 300,
#}

ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}

IMAGES_STORE = '/home/janis/dev/garms_data/data_uk/zalando_uk/images/dec_2019'

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
HTTPERROR_ALLOWED_CODES = [404, 403]
