# -*- coding: utf-8 -*-
import scrapy

class CraiglistscrapperSpider(scrapy.Spider):
    name = 'craiglistscrapper'
    allowed_domains = ['craigslist.org']
    start_urls = ['https://chicago.craigslist.org/d/apts-housing-for-rent/search/apa/']

    def parse(self, response):
        #Now parse the response
        date = response.css(".result-date::text").getall()
        title = response.css(".result-title.hdrlnk::text").getall()
        bedrooms = response.css("span[class=result-meta] .housing::text").getall()
        price = response.css('span[class=result-meta] .result-price::text').getall()
        neighborhood = response.css("span[class=result-meta] .result-hood::text").getall()
        has_map = response.css("span[class=result-meta] .maptag::text").getall()
        has_pics = response.css("span[class=result-meta] .result-tags::text").getall()
        # convert extracted content row wise
        scraped_info = {}
        for item in zip(date,title,bedrooms,price,neighborhood,has_map,has_pics):
            scraped_info = {
                    'Date' : item[0],
                    'title' : item[1],
                    'bedrooms': item[2],
                    'price' : item[3],
                    'neighborhood' : item[4],
                    'has_map' : item[5],
                    'has_pics' : item[6]
                    }
            yield scraped_info
        
        for i in range(5):
            page_ct = 120*(i+1)
            next_page = '/search/apa?s=%d' %page_ct
            next_page = response.urljoin(next_page)
            print(next_page)
            yield scrapy.Request(next_page, callback = self.parse)
