import scrapy
from scrapy.selector import Selector
from boohoo.items import BoohooItem
import hashlib
import re
import requests
import json
import datetime


class BoohooSpider(scrapy.Spider):
    name = "boohoo_spider_uk"

    # The main start function which initializes the scraping URLs and triggers parse function
    def start_requests(self):
        urls = [
            'http://www.topshop.com/?geoip=home'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.link_collection)

    # Go through the top menu in initial response to collect links of each category
    def link_collection(self, response):