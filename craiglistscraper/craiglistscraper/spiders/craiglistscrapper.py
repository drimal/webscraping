# -*- coding: utf-8 -*-
import scrapy
from craiglistscraper.items import craiglistscraperItem

class CraiglistscraperSpider(scrapy.Spider):
    name = 'craiglistscrapper'
    allowed_domains = ['craigslist.org']
    base_url = 'https://chicago.craigslist.org/search/see/apa?'
    start_urls = []

    for page in range(0,10):
        start_urls.append(base_url+'s='+ str(120*page))

    def parse(self, response):
        # Get listings from the response
        postings = response.xpath(".//p")
        
        for i in range(len(postings)):
            item = craiglistscraperItem()
            item['postid'] = int("".join(postings[i].xpath(".//@data-id").extract()))
            item['title'] = "".join(postings[i].xpath(".//*[@class='result-title hdrlnk']/text()").extract())
            item['postdate'] = "".join(postings[i].xpath(".//*[@class='result-date']/text()").extract())
            item['link'] = "".join(postings[i].xpath(".//*[contains(@class, 'result-title hdrlnk')]/@href").extract())
            item['price'] = "".join(postings[i].xpath(".//span[@class='result-meta']/span[@class='result-price']/text()").extract())          
            
            # parsing response to follow the posting link for more detailed information
            follow = item['link']
            
            request = scrapy.Request(follow, callback=self.parse_from_item_detail_page)
            request.meta['item'] = item
            yield request
    
    def parse_from_item_detail_page(self, response):
        item = response.meta['item']
        latparser = response.xpath("//div[contains(@id,'map')]")
        item['latitude'] = ''.join(latparser.xpath("@data-latitude").extract())
        item['longitude'] = ''.join(latparser.xpath("@data-longitude").extract())
        
        #extract attributes of the listing 
        attr = response.xpath("//p[@class='attrgroup']")
        attributes = attr.xpath("span/b/text()").extract()
        try: 
            item['beds'] = attributes[0]
            item['baths'] = attributes[1]
            item['area'] = attributes[2]
            item['others'] = attr.xpath("span/text()").extract()[2:]
        except:
            pass 
        return item
        
    
