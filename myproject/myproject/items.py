# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BangumiItem(scrapy.Item):
    # define the fields for your item here like:
    name  = scrapy.Field()
    link  = scrapy.Field()
    score = scrapy.Field()
    num   = scrapy.Field()
    info  = scrapy.Field()
    
class BilibiliItem(scrapy.Item):
    # define the fields for your item here like:
    source= scrapy.Field()
    name  = scrapy.Field()
    link  = scrapy.Field()
    time  = scrapy.Field()
    play  = scrapy.Field()
    danmu = scrapy.Field()
    rank  = scrapy.Field()
    coins = scrapy.Field()
    favo  = scrapy.Field()
    
class AdsItem(scrapy.Item):
    link  = scrapy.Field()

    
    
    
