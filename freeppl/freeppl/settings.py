# -*- coding: utf-8 -*-

# Scrapy settings for freeppl project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'freeppl'

SPIDER_MODULES = ['freeppl.spiders']
NEWSPIDER_MODULE = 'freeppl.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/35.0.1916.47 Safari/537.36 '

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


CONCURRENT_REQUESTS_PER_DOMAIN = 1
RETRY_TIMES = 0

# # PROXY
# PROXY = 'http://127.0.0.1:8888/?noconnect'

# SCRAPOXY
# API_SCRAPOXY = 'http://127.0.0.1:8889/api'
# API_SCRAPOXY_PASSWORD = 'Kurlasmaskas9921'
#
# # BLACKLISTING
# BLACKLIST_HTTP_STATUS_CODES = [503, 403]

# DOWNLOADER_MIDDLEWARES = {
#     'scrapoxy.downloadmiddlewares.proxy.ProxyMiddleware': 100,
#     'scrapoxy.downloadmiddlewares.wait.WaitMiddleware': 101,
#     'scrapoxy.downloadmiddlewares.scale.ScaleMiddleware': 102,
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
#     'scrapoxy.downloadmiddlewares.blacklist.BlacklistDownloaderMiddleware': 950,
#     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
#     'scrapy_useragents.downloadermiddlewares.useragents.UserAgentsMiddleware': 500,
# }

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
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,lv;q=0.8',
    'cache-control': 'no-cache',
    'cookie': 'SSLB=1; _dy_c_exps=; split_tag_control=Conversant; _dycnst=dg; _dyid=4926938466357341237; _dycst=dk.m.c.ws.; _abck=7799E3DECD839D214D8FCC2BA54D6E62~0~YAAQPVtlX+00TYhuAQAA/zNjhwOpwOXQ5KqPXy+HgeCujvsT7WhpSyGUg/ByAnSQ/xKu2VOsBegD7t1PSCHyM9wMlwPlxxB6IzFzH3kRU7TlD1tx+z/mCusk1qYQfUPJZV1wqGCf1Hrz7ClYI8QUBy+bxpPEZxAOFzq0bFOiA6Rj1I/Jw7gV+xpLstzeLRY2Bz9vlSxEMVK3gWx0LFzyYh14xbQlQz3q8Ol2zI+f06SxPlAIpsKxZjh/r+QtVAzOBb/1pBe03E434Ut8VaDVdIL7SyMTHYSbUdk+Xz5yVmiV1gCKTHbXBNQ/NT2vPcKwxXDNYquhCQ5i7MM=~-1~-1~-1; _ga=GA1.2.1633901761.1578524424; ab.storage.deviceId.ac9d3372-8a20-4479-ad5e-e26b3cb1c321=%7B%22g%22%3A%223c938fa3-33f9-6421-ee34-5fc21297ed9e%22%2C%22c%22%3A1578524423678%2C%22l%22%3A1578524423678%7D; _gcl_au=1.1.1823446121.1578524424; _pxvid=a7067527-326a-11ea-bdee-0242ac12000e; MGX_P=a28de37e-8505-4b3a-8d0b-43fe4d6f2eb7; MGX_U=faccacb1-2748-4af9-ad12-bbeb6e6a008f; MGX_CID=c9586c38-ecf4-452c-ba18-43e1564d9ce6; _mibhv=anon-1578524424177-5072702669_6190; _dy_c_att_exps=; _dy_toffset=0; SS_PWA_SHOP=0; SSID_BE=CABM2h0cACAAAAAEXxZe3AaDGARfFl4HAAAAAACNfDpg4UdZXgDRnMXIAAPbkxsAEMxFXgIAUsoAAxDRGwDhR1leAQDTwQAAHsEAAP_GAACKvAAABboAAEHGAABzwgAAbMkAAA; SSSC_A15=513.G6779710760248608476.7|51397.1807323:51794.1822992; urbn_currency=GBP; urbn_tracer=WOENI7F4YK; AKA_A2=A; siteId=fp-uk; urbn_device_type=LARGE; urbn_data_center_id=US-PA; urbn_language=en-GB; urbn_site_id=fp-uk; urbn_geo_region=EU-LN; urbn_edgescape_site_id=fp-us; urbn_inventory_pool=GB_DIRECT; urbn_channel=web; urbn_auth_payload=%7B%22authToken%22%3A%20%22eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJmcCIsImV4cCI6MTU4MjkxMDAwOS42MTc5NzEsImlhdCI6MTU4MjkwOTQwOS42MTc5NzEsImRhdGEiOiJ7XCJjcmVhdGVkVGltZVwiOiAxNTc4NTI0NDIwLjU1ODUyOTQsIFwicHJvZmlsZUlkXCI6IFwiWks1Tnk3SXVJMzVORXBVTkJyU0g4b2s0UHBmTUFDdUNjMDdnY2FMV3Bjd2lhalNHZHpPZklPUmdVSk43bnA4ZjVVKzNyczJyeGhqbTRwRDMwQ2NJQnc9PThiODQ3YjI2M2E3NmQ1YWEwNmM4NzUzMDc5MWU0YjQ1OWFiYTE2OTJkOGZjMTUxMzAyNzY1N2Q1M2VlMjNmZDNcIiwgXCJhbm9ueW1vdXNcIjogdHJ1ZSwgXCJ0cmFjZXJcIjogXCJXT0VOSTdGNFlLXCIsIFwic2NvcGVcIjogW1wiR1VFU1RcIl0sIFwic2l0ZUlkXCI6IFwiZnAtdWtcIiwgXCJicmFuZElkXCI6IFwiZnBcIiwgXCJzaXRlR3JvdXBcIjogXCJmcFwiLCBcImRhdGFDZW50ZXJJZFwiOiBcIlVTLVBBXCIsIFwiZ2VvUmVnaW9uXCI6IFwiRVUtTE5cIiwgXCJlZGdlc2NhcGVcIjoge1wicmVnaW9uQ29kZVwiOiBcIkJFXCJ9LCBcImNhcnRJZFwiOiBcIkdHaFBta3grRjJBaFBWRXhVY28rQjB3bTJZdkZKdjZ0aWtPUWI4Y2x1Y1NaTm9WV21xR0F5bngrNVFOUnBXM3I1VSszcnMycnhoam00cEQzMENjSUJ3PT0yMTljMWI3ZmJhZTE5NjNmMzgxNDAzNmM2ODNhNWVhYmQwMTkwNTUxNTU1M2E5NDRhZjEyODU0NmU1NzIyZjc2XCJ9In0.wvaQcSQfHm77FNgrbcrwR9JHGcfEpDRSBeQoMUBOd7c%22%2C%20%22reauthToken%22%3A%20%22eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJmcCIsImV4cCI6MTU5ODQ2MTQwOS42MTg0Mzk3LCJpYXQiOjE1ODI5MDk0MDkuNjE4NDM5NywiZGF0YSI6IntcImNyZWF0ZWRUaW1lXCI6IDE1ODI5MDk0MDkuNjE4NDI1LCBcInNjb3BlXCI6IFtcIkdVRVNUXCJdLCBcInRyYWNlclwiOiBcIldPRU5JN0Y0WUtcIiwgXCJwcm9maWxlSWRcIjogXCJaSzVOeTdJdUkzNU5FcFVOQnJTSDhvazRQcGZNQUN1Q2MwN2djYUxXcGN3aWFqU0dkek9mSU9SZ1VKTjducDhmNVUrM3JzMnJ4aGptNHBEMzBDY0lCdz09OGI4NDdiMjYzYTc2ZDVhYTA2Yzg3NTMwNzkxZTRiNDU5YWJhMTY5MmQ4ZmMxNTEzMDI3NjU3ZDUzZWUyM2ZkM1wifSJ9.VZublcbACCl3uY6eS7PrbukFWIDDd0YxKKSEXrxdIgI%22%2C%20%22expiresIn%22%3A%20600.0%2C%20%22reauthExpiresIn%22%3A%2015552000.0%2C%20%22scope%22%3A%20%22GUEST%22%2C%20%22tracer%22%3A%20%22WOENI7F4YK%22%2C%20%22dataCenterId%22%3A%20%22US-PA%22%2C%20%22geoRegion%22%3A%20%22EU-LN%22%2C%20%22createdAt%22%3A%201582909409622.7102%2C%20%22authExpiresTime%22%3A%201582909889.622711%2C%20%22reauthExpiresTime%22%3A%201598461409.6227121%7D; urbn_personalization_context=%5B%5B%22device_type%22%2C%20%22LARGE%22%5D%2C%20%5B%22personalization%22%2C%20%5B%5B%22ab%22%2C%20%5B%5B%22SS_PWA_SHOP%22%2C%200%5D%5D%5D%2C%20%5B%22experience%22%2C%20%5B%5B%22image_quality%22%2C%2080%5D%2C%20%5B%22reduced%22%2C%20false%5D%5D%5D%2C%20%5B%22initialized%22%2C%20false%5D%2C%20%5B%22isCallCenterSession%22%2C%20false%5D%2C%20%5B%22isSiteOutsideNorthAmerica%22%2C%20true%5D%2C%20%5B%22isSiteOutsideUSA%22%2C%20true%5D%2C%20%5B%22isViewingInEnglish%22%2C%20true%5D%2C%20%5B%22isViewingRegionalSite%22%2C%20false%5D%2C%20%5B%22loyalty%22%2C%20false%5D%2C%20%5B%22loyaltyPoints%22%2C%20%22%22%5D%2C%20%5B%22privacyRestriction%22%2C%20false%5D%2C%20%5B%22siteDown%22%2C%20false%5D%2C%20%5B%22thirdParty%22%2C%20%5B%5B%22dynamicYield%22%2C%20true%5D%2C%20%5B%22googleMaps%22%2C%20true%5D%2C%20%5B%22moduleImages%22%2C%20true%5D%2C%20%5B%22personalizationQs%22%2C%20%22%22%5D%2C%20%5B%22productImages%22%2C%20true%5D%2C%20%5B%22promoBanners%22%2C%20true%5D%2C%20%5B%22tealium%22%2C%20true%5D%5D%5D%2C%20%5B%22userHasAgreedToCookies%22%2C%20false%5D%5D%5D%2C%20%5B%22scope%22%2C%20%22GUEST%22%5D%2C%20%5B%22user_location%22%2C%20%22c14b2e5b8e5a0c7105bee057cf1be80e%22%5D%5D; akacd_ss1=3760362208~rv=15~id=7a1b1211f192e9445b3b644459e013a6; _dy_csc_ses=t; _dy_ses_load_seq=80441%3A1582909410763; FP_ATTR=other; _dyjsession=c68f3393c2b8f1c652432e014ac4fd27; _dy_geo=ES.EU.ES_CT.ES_CT_Barcelona; _dy_df_geo=Spain..Barcelona; urbn_page_visits_count=%7B%22fp-uk%22%3A1%7D; _gid=GA1.2.2094573328.1582909413; ab.storage.sessionId.ac9d3372-8a20-4479-ad5e-e26b3cb1c321=%7B%22g%22%3A%2214a9c200-28ba-6b2b-5e0c-fac431f6648e%22%2C%22e%22%3A1582911213437%2C%22c%22%3A1582909413438%2C%22l%22%3A1582909413438%7D; mp_dev_mixpanel=%7B%22distinct_id%22%3A%20%2216f876337ad1cb-05cc334bd6ebd5-1d376b5b-232800-16f876337aee5c%22%2C%22bc_persist_updated%22%3A%201578524452426%2C%22customer_language%22%3A%20%22english%22%2C%22g_search_engine%22%3A%20%22google%22%7D; _micpn=esp:-1::1582909413520; stc114946=env:1582909413%7C20200330170333%7C20200228173333%7C1%7C1044753:20210227170333|uid:1578524424314.885409828.4934726.114946.2144372830.:20210227170333|srchist:1044754%3A1581632532%3A20200315222212%7C1044753%3A1582909413%3A20200330170333:20210227170333|tsa:1582909413598.1940282646.7925057.16281568730395524:20200228173333; _derived_epik=dj0yJnU9amlEb1dBbUNZa0VBLVc5NjNCU2RNRml3VzBaaVZnSkImbj1nd2tZTldqN0t5RmpfTVpqWHllRzhBJm09NyZ0PUFBQUFBRjVaUi1V; MGX_VS=1; MGX_PX=33f6da1a-91df-4dfa-8c21-ec4d1d82d5ff; _dy_soct=279600.430785.1582909410*340090.551206.1582909410*342129.554937.1582909410*400408.686131.1582909410*165298.236606.1582909410*264077.403653.1582909410*266365.407945.1582909410*277633.427405.1582909411*368684.613691.1582909412*395757.675105.1582909414; MGX_EID=bnNfc2VnXzAwMA==; urbn_has_accepted_cookies_fp=true; urbn_site_choice=fp-uk->fp-uk; urbn_country=GB; SSRT_A15=DklZXgADAA; SSOD_A15=AASpAAAAEADg6TAAFwAAAARfFl4OSVleAAA; utag_main=v_id:016f87633038003b6baf6d44265603078001e07000c48$_sn:7$_ss:0$_st:1582911592899$ses_id:1582909411426%3Bexp-session$_pn:1%3Bexp-session$isLoggedIn:false%3Bexp-session',
    'pragma': 'no-cache',
    'referer': 'https://www.freepeople.com/uk/',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'freeppl.middlewares.FreepplSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# # See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
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
#    'freeppl.pipelines.FreepplPipeline': 300,
#}

ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}

IMAGES_STORE = '/Users/janis/dev/garms_data/data_uk/freepeople_uk/images/2020_feb'

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
DOWNLOAD_DELAY = 0.3

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
HTTPERROR_ALLOWED_CODES = [404, 403]
