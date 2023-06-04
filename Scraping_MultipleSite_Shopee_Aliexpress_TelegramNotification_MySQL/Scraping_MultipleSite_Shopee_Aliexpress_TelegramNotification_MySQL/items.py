# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
# import item loader
# data cleaning with item loader processor
# in this case we are using backend api
# therefore this is unnecessary
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags


class ScrapingMultiplesiteShopeeAliexpressTelegramnotificationMysqlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Name = scrapy.Field()
    Price = scrapy.Field()
    Currency = scrapy.Field()
    Sold = scrapy.Field()
    SHOPEE_Ref = scrapy.Field()
    SHOPEE_Price = scrapy.Field()
    SHOPEE_Sold = scrapy.Field()