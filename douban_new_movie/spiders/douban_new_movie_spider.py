from scrapy.spiders import Spider
from scrapy.selector import Selector

from douban_new_movie.items import DoubanNewMovieItem


class DoubanNewMovieSpider(Spider):
    # Spider's name
    name = 'douban_new_movie_spider'

    # Spider's URL
    start_urls = ['http://movie.douban.com/chart']

    # Spider's function
    def parse(self, response):
        sel = Selector(response)

        # Search the item with xpath and return with a list
        movie_name = sel.xpath("//a[@class='nbg']/@title").extract()
        movie_star = sel.xpath("//div[@class='pl2']/div/span[@class='rating_nums']/text()").extract()
        movie_url = sel.xpath("//div[@class='pl2']/a/@href").extract()

        # State a instance of DoubanNewMovieItem and save all items with a loop
        item = DoubanNewMovieItem()
        item['movie_name'] = [n.encode('utf-8') for n in movie_name]
        item['movie_star'] = [n for n in movie_star]
        item['movie_url'] = [n for n in movie_url]

        # Yield item and give it to pipelines
        yield item
