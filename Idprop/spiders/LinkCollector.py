# -*- coding: utf-8 -*-
import scrapy
from Idprop.spiders.DetailExtractor import DetailExtractorSpider


class LinkCollectorSpider(scrapy.Spider):
    name = 'LinkCollector'
    allowed_domains = ['www.idprop.com']
    architect_url = 'http://www.idprop.com/experts/architects?page={}'
    designer_url = 'http://www.idprop.com/experts/interiordesigners?page={}'
    page_no = 1
    start_urls = [
        designer_url.format(page_no)
    ]
    detail_extractor = DetailExtractorSpider()

    def parse(self, response):
        urls = response.css('div.pp-desc > span.title.truncate > a::attr(href)').extract()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.detail_extractor.parse)

        self.page_no += 1
        if response.status == 200:
            yield scrapy.Request(url=self.designer_url.format(self.page_no), callback=self.parse)
