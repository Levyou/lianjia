# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class LianjiaItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Region = Field()
    District = Field()
    Id = Field()
    Layout = Field()
    Floor = Field()
    Year = Field()
    Size = Field()
    Elevator = Field()
    Renovation = Field()

    Price = Field()
