# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class craiglistscraperItem(scrapy.Item):
    
    #date = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    area = scrapy.Field()
    beds = scrapy.Field()
    postid = scrapy.Field()
    postdate = scrapy.Field()
    baths = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    #content = scrapy.Field()
    others = scrapy.Field()