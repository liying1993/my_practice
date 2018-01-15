# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
# from ..mysqlpipelines

class DingdianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    author = scrapy.Field()
    novelurl = scrapy.Field()
    serialstatus = scrapy.Field()#状态
    serialnumber = scrapy.Field()#连载字数
    category = scrapy.Field()
    name_id = scrapy.Field()

class LianjiaItem(scrapy.Item):
    house_fitmend = scrapy.Field()  #房子装修，精装还是简装
    house_area = scrapy.Field()  #房子面积
    total_price = scrapy.Field()  #总价
    house_name = scrapy.Field()  #房子的小区名字
    house_located = scrapy.Field()   #所在区域
    unit_price = scrapy.Field()  #单价
    house_room = scrapy.Field()  #房间多少
    house_towards = scrapy.Field()   #房间朝向

