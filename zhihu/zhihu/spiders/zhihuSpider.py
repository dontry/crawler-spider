# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request, FormRequest
from zhihu.items import ZhihuItem

class ZhihuspiderSpider(scrapy.CrawlSpider):
    name = "zhihuSpider"
    allowed_domains = ["zhihu.com"]
    start_urls = (
        'http://www.zhihu.com/',
    )

    headers = {

    }

 #重写了爬虫类的方法, 实现了自定义请求, 运行成功后会调用callback回调函数
 # for i, url in enumerate(urls):
 #    yield scrapy.Request("http://www.example.com", meta={'cookiejar': i},
 #        callback=self.parse_page)
    def start_requests(self):
    	return [Request("https://www.zhihu.com/login",meta={'cookiejar':1},callback = self.post_login)]  #cookiejar保留cookie

 #FormRequese
    def post_login(self,response):
    	print 'Preparing login'
    	return [FormRequest.from_response(response,
    		meta = {'cookiejar':response.meta['cookiejar']},
    		headers=self.headers,
    		formdata={
    		'_xsrf':xsrf,
    		'email':'123456',
    		'password':'123456'
    		},
    		callback=self.after_login
    		)]


    def after_login(self,response):
    	print "login successfully"
    	pass




    def parse_page(self, response):
        pass
