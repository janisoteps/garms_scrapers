# -*- coding: utf-8 -*-

# Scrapy settings for hm project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'hm'

SPIDER_MODULES = ['hm.spiders']
NEWSPIDER_MODULE = 'hm.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'hm (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

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
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,lv;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'adform_qv=1; akainst=EU1; bm_sz=371D238A55056C204874C555E01A6A8B~YAAQlboQAvLYuzJvAQAAGQY8awauq69/pGSHws4wcsKGgsPT6LdyCAjmaZV0GX9uvTihCIvA65KDYhrJqC4qAMtvIZxorc+pakGPK1bJrjqrHD0ZqxIQJ1DXAhwyjgRo+oQqTcbNBzsLQai2KYVvP1nyX/EdY7Lr93lQgrDx+sQP6RHgdcwLZdii7iI=; ab_first_session=true; ab_new_user=true; optimizelyEndUserId=oeu1578052093793r0.7104636023804616; TS013be3eb=01dd555d354971cb206c5bba70bf2e9d04d1a58426f162ab00cd4fc26a21fa3cb65c42bf9f93779068d9851f4cef8aa1b49de293ff4b883a07208aea327f2633fb2a3e81b2; HMX_123=1; agCookie=42072c9b-119c-42ed-89e9-44593ab6965c; JSESSIONID=ACB6A971DFD79F8048A71BB30598A902B94A5121B0B95BC07F7E13732414B6C1C7F35BCDC30EE5D0C1B95CFE6CC8FA88CD3F587BEA5F7B524F8BB8947C24F66D.HYBECMPRDEU1P04; userCookie=##eyJjYXJ0Q291bnQiOjB9##; hm-greatbritain-favourites=""; TS0150476f=01dd555d35a598ad3f045c681e28059232d3555981f162ab00cd4fc26a21fa3cb65c42bf9f5f2238745280e5d31c5a0423cf824cef95b49b72684695a6c5c0658469808db7d9f76b09d804f675e6d09b914e97787bf51720c957e3e859a523fab247a3304ddc07fa1348d93c8e244d9cbadcf553ab; _abck=B470CB0246C637DAA9DA0AD2201507F5~0~YAAQlboQAv7YuzJvAQAAWwo8awMLy/Zk99YwNaI8nRCge8fc/c1cPB0Ff+CX8kNb4fCBNM/jqQfVNsWJRwBRDsn0uaiHJYC+5U4U6KI56MFX71+EC/HIoUcY1k3PY0KR5NmDOu7TvunrDCJtEGjUUO3NsFzaEPfyyypl9YLGuZI7Tt1teu2/wfiOGWDCgOuhvjO9csQnhXzBSL2Cd7arWcJichru5/VSyBcaFljhhzMlnQWZRMExmirLiKMYmBN7OwMgzZRta4X6deI4EAphsB05ZZd7DqqBBK3EkEoah1gbg+JceufVd7rt/AU2WLD8cjdn~-1~-1~-1; ak_bmsc=200CC601CA62B5AED384CA445B0647A10210BA9569290000FD290F5EEF53C94F~plNkbv1Q+bUCEJ6s5avcoQhFfz3EVrc0AEef/9D8Y/tUuNC9kCVnfUOYCauuWxgxQFUtTuTLoVGbCAdoanppR1ZAWLZw8x42q4VVSqrFqUSoMfr9S9O7jut45Vu2vCa6nJWzVswR2M7n6HfKaAzwaISbd/9EJabwhHX0Ohv2gRH/BQQjCZQxQStOn4mSBqlAtcUgb7DFsdqjrnDfxtsvWzNKpvdo9kyJYvTZWOQqkk76Y1Er+RGtcnmxagpo42WIzi; AMCVS_32B2238B555215F50A4C98A4%40AdobeOrg=1; AMCV_32B2238B555215F50A4C98A4%40AdobeOrg=-1891778711%7CMCIDTS%7C18265%7CMCMID%7C32509042840667002613805168883976474988%7CMCAAMLH-1578656894%7C6%7CMCAAMB-1578656894%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1578059294s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C2.4.0; akamref=en_gb; s_cc=true; _ga=GA1.2.1762485173.1578052097; _gid=GA1.2.91507510.1578052097; _gat_GA_GLOBAL=1; _gat_GA_LOCAL=1; aasegs=aal%3D16770768; aamgasegs=segid%3D16770768; aemsegs=aem%3D15496949; AAMAA=AAMSegID%3D6499983; aamoptsegs=aam%3D6499983; aam_uuid=32480940005034741573801223354624019812; rmStore=atm:mop; _scid=55e0609b-c299-4698-9659-7336d7bbb9c5; _gcl_au=1.1.1999456257.1578052098; _derived_epik=dj0yJnU9dHVNb1ZwU1BWLWdTakR1WkI4SXBJRExWTTJscGNheWImbj05YjRzMTJUTkltbHRLOG9NeG1DZ253Jm09NyZ0PUFBQUFBRjRQS2dF; stc114913=tsa:1578052097860.965267166.0997734.22803766749101118.:20200103121817|env:1%7C20200203114817%7C20200103121817%7C1%7C1044345:20210102114817|uid:1578052097860.462183129.81846285.114913.1270117984:20210102114817|srchist:1044345%3A1%3A20200203114817:20210102114817; _CT_RS_=Recording; WRUIDAWS20180923=2588372142063675; __CT_Data=gpv=1&ckp=tld&dm=hm.com&apv_44_www36=1&cpv_44_www36=1&rpv_44_www36=1; dtPC=-; dtLatC=1; akavpau_www2_en_gb=1578052402~id=a2de8376130a19b91e7d6cad1c6f1b7e; bm_sv=1DF3FBF8986D2EB7A0C29B188D1263F7~U+1nPa2Om/ebIZWhib5B/8Dya3ev8adQ827V85zw3aEAcltUGL7gYLgUQbji0wlaE8HZTmA6/KPn+2/K+/hoPFACslUrlnMDlMRVNJx5INL+HfutnoCBxB7+pbQUBnZn9ye0CggRbnf34bCIAQdC2A==; ctm={\'pgv\':8652317113624582|\'vst\':3673420648741103|\'vstr\':3489893303812675|\'intr\':1578052105258|\'v\':1}; utag_main=v_id:016f6b3c0ac2002c3d3c4fb28e6803078002507000c48$_sn:1$_se:5$_ss:0$_st:1578053907148$ses_id:1578052094659%3Bexp-session$_pn:1%3Bexp-session$touchpoint:DESKTOP%3Bexp-session$vc:%7B%7D%3Bexp-session$cart_active:No%3Bexp-session$opt_ga:16836871062_16857820741%3Bexp-session$vapi_domain:hm.com; dtCookie=127A539A60CFA9971BCCF7218A073C8D|SCUyNk0rUHJvZHVjdGlvbitXZWJ8MQ; dtSa=true%7CKD82%7C-1%7CHM.com%20%20LadiesNew%20ArrivalsClothesShoes%20%26%20AccessoriesBeautyShop%20by%20ProductView%20AllDressesShirts%20%26%20Blo...%7C-%7C1578052107710%7C52093668_530%7Chttps%3A%2F%2Fwww2.hm.com%2Fen_5Fgb%2Fladies.html%7CWomen%27s%20Clothing%20%26%20Fashion%20-%20shop%20the%20latest%20trends%20%5Ep%20H%26M%20GB%7C1578052101992%7C; RT="sl=1&ss=1578052093291&tt=3673&obo=0&bcn=%2F%2F0211c844.akstat.io%2F&sh=1578052096970%3D1%3A0%3A3673&dm=hm.com&si=b2ea6600-abba-4323-9fee-d836e61c05a9&ld=1578052096970&r=https%3A%2F%2Fwww2.hm.com%2Fen_gb%2Fladies.html&ul=1578052107734"',
    'Host': 'www2.hm.com',
    'Pragma': 'no-cache',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'hm.middlewares.HmSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'hm.middlewares.HmDownloaderMiddleware': 543,
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
#    'hm.pipelines.HmPipeline': 300,
#}

ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}

IMAGES_STORE = '/home/janis/dev/garms_data/data_uk/hm_uk/images/dec_2019'

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 30
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
