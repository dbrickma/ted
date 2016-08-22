# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html



import scrapy




class TedItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    citations = scrapy.Field()

    text = scrapy.Field()

