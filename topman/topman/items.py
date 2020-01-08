# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class TopmanItem(Item):
    shop = Field()
    name = Field()
    price = Field()
    saleprice = Field()
    sale = Field()
    prod_url = Field()
    prod_id = Field()
    image_urls = Field()
    image_hash = Field()
    sex = Field()
    color_string = Field()
    brand = Field()
    currency = Field()
    date = Field()
    description = Field()
    category = Field()
    size_stock = Field()
    in_stock = Field()
