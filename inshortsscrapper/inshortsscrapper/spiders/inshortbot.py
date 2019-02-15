# -*- coding: utf-8 -*-
import scrapy


class InshortbotSpider(scrapy.Spider):
    name = 'inshortbot'
    allowed_domains = ['inshorts.com']
    start_urls = ['https://inshorts.com/en/read']

    def parse(self, response):
        headline = response.css('span[itemprop="headline"]::text').getall()
        body = response.css('div[itemprop="articleBody"]::text').getall()
        date = response.css('.date::text').getall()
        news = {}
        for item in zip(date, headline, body):
            news = {
                    'Date' : item[0],
                    'headline' : item[1],
                    'article_body' : item[2]
                }
            yield news
		
