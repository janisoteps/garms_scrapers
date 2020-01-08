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

DOWNLOADER_MIDDLEWARES = {
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
    'accept-language': 'en',
    'cache-control': 'private, max-age=0, proxy-revalidate, no-store, no-cache, must-revalidate',
    'content-encoding': 'gzip',
    'content-security-policy': 'default-src \'self\' \'unsafe-eval\' \'unsafe-inline\' data: https://*.go-mpulse.net https://cdn.polyfill.io https://*.dynamicyield.com https://intljs.rmtag.com https://d16fk4ms6rqz1v.cloudfront.net https://cdn.merklesearch.com https://cdn.pbbl.co https://s.pinimg.com https://bat.bing.com https://script.crazyegg.com https://assistjs.skimresources.com https://connect.facebook.net https://*.twitter.com https://cdn.groupbycloud.com https://tags.tiqcdn.com https://www.googleadservices.com https://js.appboycdn.com https://static.ads-twitter.com https://js-agent.newrelic.com https://*.afterpay.com https://mpsnare.iesnare.com https://bam.nr-data.net https://*.datasteam.io https://ci-mpsnare.iovation.com https://*.bazaarvoice.com https://*.bluecore.com https://tpc.googlesyndication.com https://*.salesforceliveagent.com https://static.site24x7rum.com https://*.paypal.com https://*.apple.com https://*.criteo.com https://tags.tiqcdn.cn https://adadvisor.net https://s3.amazonaws.com https://www.gstatic.com http://maps.google.cn https://www.myregistry.com https://www.shopstylecollective.com https://www.shopstylecollective.co.uk https://*.agkn.com https://polyfill.io http://ditu.google.cn https://*.clearpay.co.uk https://*.stg-sessionm.com https://*.sessionm.com https://maxcdn.bootstrapcdn.com https://fast.fonts.net https://service.force.com https://urbn.my.salesforce.com https://urbanoutfitters.secure.force.com https://app.curalate.com https://*.cs23.my.salesforce.com https://full-urbanoutfitters.cs23.force.com https://images.ctfassets.net https://*.google.com https://images.contentful.com https://h.nexac.com https://p.dlx.addthis.com https://y8ui6jzp.micpn.com https://ct1.ra.linksynergy.com https://consent.nxtck.com https://consent.mediaforge.com https://consent.jrs5.com https://*.linksynergy.com https://*.fpassets.com https://www.googletagmanager.com https://*.googleapis.com https://*.dc-storm.com https://*.ggpht.com https://*.akstat.io https://*.groupbycloud.com https://static.criteo.com https://cdn.dynamicyield.com https://*.rkdms.com https://*.gstatic.com http://images.freepeople.com https://www.google.ca https://www.google.com.au https://static.criteo.net https://www.google.co.uk https://*.freepeople.com https://*.facebook.com https://www.google.nl https://www.google.de https://user-event-tracker.crazyegg.com https://www.google.fr https://www.google.es https://www.google.com.mx https://www.google.co.jp https://www.google.it https://www.google.co.il https://www.google.com.ar https://cdn.dashhudson.com https://track.securedvisit.com https://cx.atdmt.com https://fonts.gstatic.com https://use.fontawesome.com https://ct.pinterest.com https://c.go-mpulse.net https://nyt2.dc-storm.com https://sentry.io https://*.fls.doubleclick.net https://www.facebook.com https://dis.as.criteo.com https://dis.us.criteo.com https://videos.contentful.com https://www.youtube.com https://dis.eu.criteo.com https://*.api.bazaarvoice.com https://videos.ctfassets.net https://*.g.doubleclick.net https://dev.appboy.com https://*.perimeterx.net https://api.bazaarvoice.com https://www.google-analytics.com https://*.akamaihd.net https://freepeople.wufoo.com https://*.rewardstyle.com https://core.conversant.mgr.consensu.org https://*.scene7.com https://*.cs23.force.com https://*.attn.tv https://*.dotomi.com https://events.attentivemobile.com https://sample-api-v2.crazyegg.com https://*.adsymptotic.com https://t.co https://cdn.honey.io https://g.3gl.net https://r.3gl.net.cn https://r.3gl.net https://*.hotjar.com https://cdn.contentful.com wss://*.hotjar.com https://static.lightning.force.com https://*.hotjar.io https://*.attentivemobile.com;frame-ancestors \'none\';report-uri https://sentry.io/api/219529/security/?sentry_key=57d8fc981b394b5e8f2a538e58c4012d',
    'content-type': 'text/html; charset=UTF-8',
    'date': 'Wed, 08 Jan 2020 23:00:49 GMT',
    'expires': 'Fri, 12 Jul 2019 22:45:42 GMT',
    'link': '<https://cdn.polyfill.io>;rel="preconnect"',
    'locale': 'en_GB',
    'pragma': 'no-cache',
    'rtss': '1-2-15',
    'rtss1': 'a15site',
    'server': 'nginx',
    'set-cookie': 'FP_CART_ABAN_TEST=1; path=/; domain=.freepeople.com; expires=Wed, 08-Jan-2020 23:30:45 GMT; SSLB=1; path=/; domain=.freepeople.com; expires=Thu, 07-Jan-2021 23:05:20 GMT; SSID_BE=CAA74h04AAAAAAAEXxZe3AaDGARfFl4BAAAAAACwk_dfBF8WXgDRnAW6AAO0ohgABF8WXgEA08EAAwZIGgAEXxZeAQAewQADfhkaAARfFl4BAHPCAAOVaBoABF8WXgEA; path=/; domain=.freepeople.com; expires=Thu, 07-Jan-2021 23:00:45 GMT; SSOD_A15=AE3IAAAAEADg6TAAAgAAAARfFl4dXxZeAAA; path=/; domain=.freepeople.com; expires=Thu, 07-Jan-2021 23:00:45 GMT; urbn_device_type=LARGE; Path=/; urbn_inventory_pool=GB_DIRECT; Path=/; urbn_convenience_currency=""; expires=Tue, 08 Jan 2019 23:00:45 GMT; Path=/; urbn_currency=GBP; Path=/; uofilter=""; expires=Tue, 08 Jan 2019 23:00:45 GMT; Path=/; siteId=fp-uk; Path=/; urbn_search_provider=urbnsearch; Path=/; urbn_language=en-GB; Path=/; urbn_edgescape_site_id=fp-us; Path=/; urbn_site_id=fp-uk; Path=/; bm_sv=2547B965E864723314F152955EC5A247~aPOnq60SZAhXrN3xeFVDwS2NJQMxrICrYZ+O/dlq24gxlqh0NiQNBB1eOycbzJsbjVssdMzewa8XGM2q+YlxFTPDbsPrezQzNOtFMPUwLtuhRK+N/JIMmjRM5DfklBfI9h9/b66S9cbG6NZjODlRQeiID+L3630qtzOrqRlBZz0=; Domain=.freepeople.com; Path=/; Max-Age=7174; HttpOnly',
    'status': '200',
    'strict-transport-security': 'max-age=15768000',
    'vary': 'Accept-Encoding',
    'x-akamai-request-id2': '92.122.54.22:1b5fd63b',
    'x-akamai-transformed': '9 - 0 pmb=mTOE,1',
    'x-frame-options': 'deny',
    'x-urbn-context-path': '/uk/',
    'x-urbn-site-id': 'fp-uk'
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

IMAGES_STORE = '/Users/janis/dev/garms_data/data_uk/freepeople_uk/images/2019_dec'

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
