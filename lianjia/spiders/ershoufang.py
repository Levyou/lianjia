# -*- coding: utf-8 -*-
import scrapy
from lianjia.items import LianjiaItem


class ErshoufangSpider(scrapy.Spider):
    name = 'ershoufang'

    start_urls = ['http://cd.lianjia.com/ershoufang/']

    def parse(self, response):
        urls = response.xpath('//div[@class="info clear"]/div[@class="title"]/a/@href').extract()
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_one)

        for i in range(2, 101):
            link = 'https://cd.lianjia.com/ershoufang/pg{}/'.format(str(i))
            yield scrapy.Request(link, callback=self.parse)

    def parse_one(self, response):

        item = LianjiaItem()

        Region = response.xpath('//div[@class="houseInfo"]/div[@class="type"]/div[@class="mainInfo"]/text()').extract_first()
        District = response.xpath('//div[@class="aroundInfo"]/div[@class="areaName"]/span[@class="info"]/a[2]/text()').extract_first()
        Elevator = response.xpath('//div[@class="introContent"]/div[@class="base"]/div[@class="content"]/ul/li[11]/text()').extract_first()
        Floor = response.xpath('//div[@class="introContent"]/div[@class="base"]/div[@class="content"]/ul/li[2]/text()').extract_first()
        Id = response.xpath('//div[@class="houseRecord"]/span[@class="info"]/text()').extract_first()
        Layout = response.xpath('//div[@class="houseInfo"]/div[@class="room"]/div[@class="mainInfo"]/text()').extract_first()
        Price = response.xpath('//div[@class="content"]/div[@class="price "]/span[@class="total"]/text()').extract_first()
        Renovation = response.xpath('//div[@class="introContent"]/div[@class="base"]/div[@class="content"]/ul/li[9]/text()').extract_first()
        Size = response.xpath('//div[@class="introContent"]/div[@class="base"]/div[@class="content"]/ul/li[3]/text()').extract_first()
        Year = response.xpath('//div[@class="houseInfo"]/div[@class="area"]/div[@class="subInfo"]/text()').extract_first().split('/')[0]

        item['Region'] = Region
        item['District'] = District
        item['Elevator'] = Elevator
        item['Floor'] = Floor
        item['Id'] = Id
        item['Layout'] = Layout
        item['Price'] = Price
        item['Renovation'] = Renovation
        item['Size'] = Size
        item['Year'] = Year
        yield item

