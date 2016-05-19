#-*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess

class TshirtsCrawler(scrapy.Spider):
    name = 'Tshirt Crawler'
    start_urls = ['http://ddab0ng.tistory.com/category/%EC%B6%94%EC%B2%9C%20%EC%83%81%EC%9D%98%28%EC%9D%B4%EB%84%88%29/%EC%85%94%EC%B8%A0/%EA%B0%80%EB%94%94%EA%B1%B4/%ED%8B%B0%EC%85%94%EC%B8%A0']
    def parse(self, response):
        tshirts = response.css('ul>li>a>strong::text').extract()
        for tshirt in tshirts:
            if tshirt == " ":
                continue
            print repr(tshirt).decode('raw_unicode_escape')
            #print response.css(query_homeplaya).extract()

class BajiCrawler(scrapy.Spider):
    name = 'Baji Crawler'
    start_urls = ['http://ddab0ng.tistory.com/category/%EC%B6%94%EC%B2%9C%20%ED%95%98%EC%9D%98/%EC%B2%AD%EB%B0%94%EC%A7%80/%EB%A9%B4%EB%B0%94%EC%A7%80/%EC%8A%AC%EB%9E%99%EC%8A%A4']
    def parse(self, response):
        bajis = response.css('ul>li>a>strong::text').extract()
        for baji in bajis:
            if baji == " ":
                continue
            print repr(baji).decode('raw_unicode_escape')
            #print response.css(query_homeplaya).extract()

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(TshirtsCrawler)
process.crawl(BajiCrawler)
process.start()
