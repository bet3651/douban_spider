# -*- coding: utf-8 -*-
import scrapy
from ..items import DoubanItem

class DoubanSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        # print(response.text)
        # xpath
        # //div[@class='article']/ol[@class='grid_view']/li
        movie_list = response.xpath("//div[@class='article']/ol[@class='grid_view']/li")
        for li_item in movie_list:
            douban_item = DoubanItem()
            # 序号
            douban_item["sid"] = li_item.xpath(".//div[@class='item']/div/em/text()").extract_first()
            # 电影名
            douban_item["movie_name"] = li_item.xpath(".//div[@class='info']/div[@class='hd']/a/span/text()").extract()
            # 电影介绍信息
            content = li_item.xpath(".//div[@class='info']/div[@class='bd']/p[1]/text()").extract()

            for i_content in content:
                content_s = "".join(i_content.split())
                douban_item["movie_info"] = content_s
            # 电影评分
            star = li_item.xpath(".//span[@class='rating_num']/text()").extract_first()
            douban_item["movie_star"] = star
            # 电影评价数
            movie_eval = li_item.xpath(
                ".//div[@class='info']/div[@class='bd']/div[@class='star']/span[4]/text()").extract()
            douban_item["movie_eval"] = movie_eval
            # 电影描述
            movie_desc = li_item.xpath(".//div[@class='info']/div[@class='bd']/p[@class='quote']/span/text()").extract()
            douban_item["movie_desc"] = movie_desc
            # print(douban_item)
            yield douban_item

        movie_next = response.xpath("//span[@class='next']/link/@href").extract()
        if movie_next:
            next_url = 'https://movie.douban.com/top250' + movie_next[0]
            # print(next_url)
            yield scrapy.Request(next_url, callback=self.parse)