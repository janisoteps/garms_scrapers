# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class TopshopItem(Item):
    # define the fields for your item here like:
    shop = Field()
    name = Field()
    price = Field()
    prod_url = Field()
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