# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanNewMovieItem(scrapy.Item):
    # Three fields that I want to save to the database
    movie_name = scrapy.Field()
    movie_star = scrapy.Field()
    movie_url = scrapy.Field()
