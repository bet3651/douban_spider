# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #序号
    sid = scrapy.Field()
    #电影名称
    movie_name = scrapy.Field()
    #电影介绍信息
    movie_info = scrapy.Field()
    #电影星星评级
    movie_star = scrapy.Field()
    #电影评论数
    movie_eval = scrapy.Field()
    #电影的描述
    movie_desc = scrapy.Field()
