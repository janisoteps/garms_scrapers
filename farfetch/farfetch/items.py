# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class FarfetchItem(Item):
    # define the fields for item:
    shop = Field()
    name = Field()
    price = Field()
    prod_url = Field()
    image_urls = Field()
    image_hash = Field()
    sex = Field()
    sale = Field()
    saleprice = Field()
    color = Field()
    brand = Field()
    currency = Field()
    date = Field()
    description = Field()
    category = Field()
