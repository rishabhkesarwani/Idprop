# -*- coding: utf-8 -*-
import scrapy
from Idprop.items import Person


class DetailExtractorSpider(scrapy.Spider):
    name = 'DetailExtractor'
    allowed_domains = ['www.idprop.com']
    start_urls = ['http://www.idprop.com/']

    def parse(self, response):
        person = Person()
        info_pad = response.css('div.pp-desc')
        person['name'] = info_pad.css('span.title::text')[0].extract()
        person['url'] = response.url
        person['profile'] = info_pad.css('span.db::text')[1].extract()
        contact = info_pad.css('div.cd-info.clearfix span.cd-nm::text')
        person['email'] = contact[0].extract()
        if len(contact) == 2:
            person['mobile'] = contact[1].extract()
        yield person
