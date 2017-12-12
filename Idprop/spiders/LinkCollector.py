# -*- coding: utf-8 -*-
import scrapy
from Idprop.spiders.DetailExtractor import DetailExtractorSpider


class LinkCollectorSpider(scrapy.Spider):
    name = 'LinkCollector'
    allowed_domains = ['www.idprop.com']
    architects = 'http://www.idprop.com/experts/architects?page={}'
    interior_designers = 'http://www.idprop.com/experts/interiordesigners?page={}'
    general_contractors = 'http://www.idprop.com/experts/generalcontractors?page={}'
    home_builders = 'http://www.idprop.com/experts/homebuilders?page={}'
    landscape_architects = 'http://www.idprop.com/experts/landscapearchitects?page={}'
    landscape_contractors = 'http://www.idprop.com/experts/landscapecontractors?page={}'
    design_build_firms = 'http://www.idprop.com/experts/designbuildfirms?page={}'
    stone_pavers_concrete = 'http://www.idprop.com/experts/stonepaversconcrete?page={}'
    kitchen_bath_remodelers = 'http://www.idprop.com/experts/kitchenbathremodelers?page={}'
    page_no = 1
    items_crawled = 0
    start_urls = [
        kitchen_bath_remodelers.format(page_no)
    ]
    detail_extractor = DetailExtractorSpider()

    def parse(self, response):
        urls = response.css('div.pp-desc > span.title.truncate > a::attr(href)').extract()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.detail_extractor.parse)
        self.items_crawled += len(urls)
        print('pages crawled {}, items crawled {}'.format(self.page_no, self.items_crawled))
        if len(urls) != 0:
            self.page_no += 1
            yield scrapy.Request(url=self.kitchen_bath_remodelers.format(self.page_no), callback=self.parse)
