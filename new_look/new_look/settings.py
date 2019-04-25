# # -*- coding: utf-8 -*-
#
# # Scrapy settings for zara project
# #
# # For simplicity, this file contains only settings considered important or
# # commonly used. You can find more settings consulting the documentation:
# #
# #     https://doc.scrapy.org/en/latest/topics/settings.html
# #     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# #     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#
# BOT_NAME = 'zara'
#
# SPIDER_MODULES = ['zara.spiders']
# NEWSPIDER_MODULE = 'zara.spiders'
#
#
# # Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) ' \
#              'Chrome/72.0.3626.119 Safari/537.36 '
#
# USER_AGENTS = [
#     ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 '
#      'Safari/537.36'),  # chrome Win10
#     ('Mozilla/5.0 (X11; Linux x86_64) '
#      'AppleWebKit/537.36 (KHTML, like Gecko) '
#      'Chrome/61.0.3163.79 '
#      'Safari/537.36'),  # chrome
#     ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) '
#      'Gecko/20100101 '
#      'Firefox/55.0'),  # firefox
#     ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
#      '(KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'),
#     ('Mozilla/5.0 (X11; Linux x86_64) '  # Chrome 72.0 Win10
#      'AppleWebKit/537.36 (KHTML, like Gecko) '
#      'Chrome/61.0.3163.91 '
#      'Safari/537.36'),  # chrome
#     ('Mozilla/5.0 (X11; Linux x86_64) '
#      'AppleWebKit/537.36 (KHTML, like Gecko) '
#      'Chrome/62.0.3202.89 '
#      'Safari/537.36'),  # chrome
#     ('Mozilla/5.0 (X11; Linux x86_64) '
#      'AppleWebKit/537.36 (KHTML, like Gecko) '
#      'Chrome/63.0.3239.108 '
#      'Safari/537.36'),  # chrome
#     ('Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0)'
#      ' Gecko/20100101 Firefox/65.0'),
#     ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#      'Chrome/72.0.3626.119 Safari/537.36'),
#     ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#      'Chrome/72.0.3626.96 Safari/537.36'),
#     ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 '
#      '(KHTML, like Gecko) Version/12.0.3 Safari/605.1.15'),
#     ('Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) '
#      'Gecko/20100101 Firefox/65.0'),
#     ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) '
#      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'),
#     ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) '
#      'Gecko/20100101 Firefox/65.0'),
#     ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) '
#      'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.2 Safari/605.1.15'),
#     ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 '
#      '(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')
# ]
#
# # Obey robots.txt rules
# ROBOTSTXT_OBEY = False
#
# # Configure maximum concurrent requests performed by Scrapy (default: 16)
# #CONCURRENT_REQUESTS = 32
#
# # Configure a delay for requests for the same website (default: 0)
# # See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# # See also autothrottle settings and docs
# #DOWNLOAD_DELAY = 3
# # The download delay setting will honor only one of:
# #CONCURRENT_REQUESTS_PER_DOMAIN = 16
# #CONCURRENT_REQUESTS_PER_IP = 16
# CONCURRENT_REQUESTS_PER_DOMAIN = 1
# RETRY_TIMES = 0
#
# # Disable cookies (enabled by default)
# #COOKIES_ENABLED = False
#
# # Disable Telnet Console (enabled by default)
# #TELNETCONSOLE_ENABLED = False
#
# # Override the default request headers:
# #DEFAULT_REQUEST_HEADERS = {
# #   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
# #   'Accept-Language': 'en',
# #}
#
# DEFAULT_REQUEST_HEADERS = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
#     'accept-encoding': 'gzip, deflate, br',
#     'accept-language': 'en-US,en;q=0.9,lv;q=0.8',
#     'cookie': 'web_version=STANDARD; bm_sz=A6377E9B4171247ED4E1787937A304D1~YAAQF93dWO/2MMBpAQAA7vNMMAObY9jO/G6+AjrcVvrfpDjr9uYQGH3kPkwpKQKy3kyae9sCyFmgQLo2dUFmq69M9VXt/yAT5jHLkEdLN7RgR2M6u/B/g34ViKpnhP90I6Yvo23/qBNyGO5Ik1IZxrKgq6T8ZukmrjpmIaOW2/GudloC2BHm3+eIEsCzdw==; optimizelyEndUserId=oeu1555588511147r0.5341322124115195; socControl=https%3A%2F%2Fwww.zara.com; _abck=E9C4AE997C8F1ED3F10F7328D035A03858DDDD173E0F00009E65B85CBD3B7502~0~e21KbjrABjJtj4rAlkSB0G21/uDfFjsrH9CU9yogvD4=~-1~-1; _ga=GA1.2.1482112061.1555588512; _gid=GA1.2.216663099.1555588512; rid=b08b1b8d-c1f3-40d4-a6a5-db0dabd6ae1c; _fbp=fb.1.1555588512026.1537971650; chin={"status":"chat-status:not_connected","uid":"","crid":"","email":"","userJid":"","uiCurrentView":"view:hidden","areMessagesNotRead":false,"privacyAccepted":false,"isChatAttended":false,"timeShowInteractiveChat":0}; ak_bmsc=F8427E1BC141972B5CEEBC4898ABD18758DDDD173E0F00009E65B85CE8F3532F~plJIMSl8F7pfGFJPBB8upKLhvRwOsAwyAbAavYDwGMvK+UT8K8sbuq+QN604qpUvFcJQMSxmsSNax4nyJMp+UVKF0Y/zY1VMUqlBZ2jcVKRn/gZL1zs43ynKQno+s3ZNqzUq7qaPqIMz7BVMoMVZZ/Aq0gX/fOBJ0vRcO/HU5Xhvi44qTSPNc3doJd5aneJT+ctfYbdSf9zJRfD4J+H9zKfDOVBhCw4zWYI+mJYBzMHwVVlO5K4gZhb/OVp2ac3XRGHFxAtB0qFXN8yjpRnLA4AQ==; rskxRunCookie=0; rCookie=euevs798yyqxd1kbkns1; WC_cookiesMsg=1; policyVersion=1527202800000; storepath=uk%2Fen; lastRskxRun=1555588530255; bm_sv=BA7896552C453713F32D8ACFE3EDA08F~MyvGdegTYulYazCn2iIk5WeZ/Sgdzyh6ZUJfRIlqX1AL367Mbi2Fo6lUvRAn0nErpA4KANkUp10yXQ34qtHFe83PzviphUNs7m8tc+ZeCo4JnctA/SA+KkBI5/8gheL8rioL8MmxJiMRT7Lia4gbEg==; RT="sl=2&ss=1555588510395&tt=4293&obo=0&bcn=%2F%2F0211c844.akstat.io%2F&sh=1555588531314%3D2%3A0%3A4293%2C1555588516293%3D1%3A0%3A4034&dm=zara.com&si=f2efe0ce-4114-45de-9ac2-68f8cfccffaf&nu=https%3A%2F%2Fwww.zara.com%2Fuk%2Fen%2Fwoman-editorial-11-l1523.html%3Fv1%3D1180552&cl=1555588871021&r=https%3A%2F%2Fwww.zara.com%2Fuk%2Fen%2Fwoman-l1000.html%3Fv1%3D358532&ul=1555588880604"',
#     'pragma': 'no-cache',
#     'referer': 'https://www.zara.com',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
# }
#
# # Enable or disable spider middlewares
# # See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# #SPIDER_MIDDLEWARES = {
# #    'zara.middlewares.ZaraSpiderMiddleware': 543,
# #}
#
# # PROXY
# PROXY = 'http://127.0.0.1:8888/?noconnect'
#
# # SCRAPOXY
# API_SCRAPOXY = 'http://127.0.0.1:8889/api'
# API_SCRAPOXY_PASSWORD = 'Kurlasmaskas3345'
#
# # BLACKLISTING
# BLACKLIST_HTTP_STATUS_CODES = [503, 403]
#
# # Enable or disable downloader middlewares
# # See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# # DOWNLOADER_MIDDLEWARES = {
# #     'scrapoxy.downloadmiddlewares.proxy.ProxyMiddleware': 100,
# #     'scrapoxy.downloadmiddlewares.wait.WaitMiddleware': 101,
# #     'scrapoxy.downloadmiddlewares.scale.ScaleMiddleware': 102,
# #     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
# #     'scrapoxy.downloadmiddlewares.blacklist.BlacklistDownloaderMiddleware': 950,
# #     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
# #     'scrapy_useragents.downloadermiddlewares.useragents.UserAgentsMiddleware': 500,
# # }
#
# DOWNLOADER_MIDDLEWARES = {
#     'scrapoxy.downloadmiddlewares.blacklist.BlacklistDownloaderMiddleware': 950,
#     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#     'scrapy_useragents.downloadermiddlewares.useragents.UserAgentsMiddleware': 500,
# }
#
# # Enable or disable extensions
# # See https://doc.scrapy.org/en/latest/topics/extensions.html
# #EXTENSIONS = {
# #    'scrapy.extensions.telnet.TelnetConsole': None,
# #}
#
# # Configure item pipelines
# # See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# #ITEM_PIPELINES = {
# #    'zara.pipelines.ZaraPipeline': 300,
# #}
#
# ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}
#
# IMAGES_STORE = '/home/janis/jdev/scrapers/img_uk/zara_uk_1'
#
# # Enable and configure the AutoThrottle extension (disabled by default)
# # See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# # The initial download delay
# AUTOTHROTTLE_START_DELAY = 0
# # The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 20
# # The average number of requests Scrapy should be sending in parallel to
# # each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 5
# # Enable showing throttling stats for every response received:
# #AUTOTHROTTLE_DEBUG = False
#
# # Enable and configure HTTP caching (disabled by default)
# # See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# #HTTPCACHE_ENABLED = True
# #HTTPCACHE_EXPIRATION_SECS = 0
# #HTTPCACHE_DIR = 'httpcache'
# #HTTPCACHE_IGNORE_HTTP_CODES = []
# #HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
#



















# -*- coding: utf-8 -*-

# Scrapy settings for new_look project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'new_look'

SPIDER_MODULES = ['new_look.spiders']
NEWSPIDER_MODULE = 'new_look.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'new_look (+http://www.yourdomain.com)'
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
CONCURRENT_REQUESTS_PER_DOMAIN = 1
RETRY_TIMES = 0

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,lv;q=0.8',
    'cookie': 'web_version=STANDARD; bm_sz=A6377E9B4171247ED4E1787937A304D1~YAAQF93dWO/2MMBpAQAA7vNMMAObY9jO/G6+AjrcVvrfpDjr9uYQGH3kPkwpKQKy3kyae9sCyFmgQLo2dUFmq69M9VXt/yAT5jHLkEdLN7RgR2M6u/B/g34ViKpnhP90I6Yvo23/qBNyGO5Ik1IZxrKgq6T8ZukmrjpmIaOW2/GudloC2BHm3+eIEsCzdw==; optimizelyEndUserId=oeu1555588511147r0.5341322124115195; socControl=https%3A%2F%2Fwww.zara.com; _abck=E9C4AE997C8F1ED3F10F7328D035A03858DDDD173E0F00009E65B85CBD3B7502~0~e21KbjrABjJtj4rAlkSB0G21/uDfFjsrH9CU9yogvD4=~-1~-1; _ga=GA1.2.1482112061.1555588512; _gid=GA1.2.216663099.1555588512; rid=b08b1b8d-c1f3-40d4-a6a5-db0dabd6ae1c; _fbp=fb.1.1555588512026.1537971650; chin={"status":"chat-status:not_connected","uid":"","crid":"","email":"","userJid":"","uiCurrentView":"view:hidden","areMessagesNotRead":false,"privacyAccepted":false,"isChatAttended":false,"timeShowInteractiveChat":0}; ak_bmsc=F8427E1BC141972B5CEEBC4898ABD18758DDDD173E0F00009E65B85CE8F3532F~plJIMSl8F7pfGFJPBB8upKLhvRwOsAwyAbAavYDwGMvK+UT8K8sbuq+QN604qpUvFcJQMSxmsSNax4nyJMp+UVKF0Y/zY1VMUqlBZ2jcVKRn/gZL1zs43ynKQno+s3ZNqzUq7qaPqIMz7BVMoMVZZ/Aq0gX/fOBJ0vRcO/HU5Xhvi44qTSPNc3doJd5aneJT+ctfYbdSf9zJRfD4J+H9zKfDOVBhCw4zWYI+mJYBzMHwVVlO5K4gZhb/OVp2ac3XRGHFxAtB0qFXN8yjpRnLA4AQ==; rskxRunCookie=0; rCookie=euevs798yyqxd1kbkns1; WC_cookiesMsg=1; policyVersion=1527202800000; storepath=uk%2Fen; lastRskxRun=1555588530255; bm_sv=BA7896552C453713F32D8ACFE3EDA08F~MyvGdegTYulYazCn2iIk5WeZ/Sgdzyh6ZUJfRIlqX1AL367Mbi2Fo6lUvRAn0nErpA4KANkUp10yXQ34qtHFe83PzviphUNs7m8tc+ZeCo4JnctA/SA+KkBI5/8gheL8rioL8MmxJiMRT7Lia4gbEg==; RT="sl=2&ss=1555588510395&tt=4293&obo=0&bcn=%2F%2F0211c844.akstat.io%2F&sh=1555588531314%3D2%3A0%3A4293%2C1555588516293%3D1%3A0%3A4034&dm=zara.com&si=f2efe0ce-4114-45de-9ac2-68f8cfccffaf&nu=https%3A%2F%2Fwww.zara.com%2Fuk%2Fen%2Fwoman-editorial-11-l1523.html%3Fv1%3D1180552&cl=1555588871021&r=https%3A%2F%2Fwww.zara.com%2Fuk%2Fen%2Fwoman-l1000.html%3Fv1%3D358532&ul=1555588880604"',
    'pragma': 'no-cache',
    'referer': 'https://www.zara.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

# PROXY
PROXY = 'http://127.0.0.1:8888/?noconnect'

# SCRAPOXY
API_SCRAPOXY = 'http://127.0.0.1:8889/api'
API_SCRAPOXY_PASSWORD = 'Kurlasmaskas3345'

# BLACKLISTING
BLACKLIST_HTTP_STATUS_CODES = [503, 403]

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'new_look.middlewares.NewLookSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'new_look.middlewares.NewLookDownloaderMiddleware': 543,
#}

DOWNLOADER_MIDDLEWARES = {
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
#    'new_look.pipelines.NewLookPipeline': 300,
#}
ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}

IMAGES_STORE = '/home/janis/jdev/scrapers/img_uk/newlook_uk_1'

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
AUTOTHROTTLE_MAX_DELAY = 20
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
