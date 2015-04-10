# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup
from douban.items import DoubanItem
import re


class GroupieSpider(CrawlSpider):
    name = 'groupie'
    allowed_domains = ['douban.com']
    start_urls = ['http://www.douban.com/group/explore?tag=%E8%B4%AD%E7%89%A9']

    rules = (
        Rule(LinkExtractor(allow=r'/group/[^/]+/$'), callback='parse_group_homepage'),
    )

    def parse_item(self, response):
        i = DoubanItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i

    def parse_group_homepage(self,response):
        self.log("Fetch group homepage: %s" % response.url)
        soup = BeautifulSoup(unicode(response.body.decode(response.encoding)).encode('utf-8'))
        # soup = BeautifulSoup(response.body)
        item = DoubanItem()  
        try:
            # get group name
            group_name_regEx = '(?<=\\n\s{8}).*(?=\\n)'
            cmpName = re.compile(group_name_regEx)
            group_name = cmpName.findall(soup.h1.string)
            item['groupName'] = group_name[0]
            # item['groupName'] = soup.h1.string
            print type(item['groupName'])
            print item['groupName']
            
            # get group id
            item['groupURL'] = response.url
            print item['groupURL']
            
            # get member number
            tag = soup.find_all('div',class_="mod side-nav")
            # tag = soup.find_all('div',{"class":"side-nav"})
            members = tag[0].find('a').string
            numCmp = re.compile("""\d+""")
            number = numCmp.findall(members)
            item['totalNumber'] = number[0].decode()
            print item['totalNumber']
            return item         
        except UnicodeEncodeError:
            print "unable to access"
