# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ted.items import TedItem

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ted.items import TedItem

class GetridSpider(CrawlSpider):
    name = 'ted_crawler'
    allowed_domains = ['patents.google.com']
    start_urls = ['https://patents.google.com/patent/US3567632A/en?q=any']

    rules = (Rule(LinkExtractor(allow=(".*",)), callback="parse_item"),)

    def parse_item(self, response):

        i = TedItem()
        i['title'] = response.xpath('//a/text()').extract()
        i['url'] = response.xpath('//a/@href').extract()
        i['citations'] = response.xpath('//a/@wrapper').extract()
        i['text'] = response.xpath('//span/text()').extract()
        yield i

