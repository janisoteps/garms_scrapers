# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class BoohooItem(Item):
    # define the fields for item:
    shop = Field()
    name = Field()
    price = Field()
    prod_url = Field()
    prod_id = Field()
    image_urls = Field()
    image_hash = Field()
    sex = Field()
    sale = Field()
    saleprice = Field()
    brand = Field()
    currency = Field()
    date = Field()
    description = Field()
    color_string = Field()
    color_hex = Field()
    category = Field()
    size_stock = Field()
