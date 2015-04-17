# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from bs4 import BeautifulSoup as BS
from douban.items import DoubanItem
from scrapy.http import Request,FormRequest
import re
import os
import logging
from PIL import Image
import urllib

logging.basicConfig(filename = os.path.join('scrapy_log.txt'), level = logging.DEBUG, 
                    filemode ='w', format ='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger('logger')


class GroupieSpider(CrawlSpider):
    name = 'groupie'
    allowed_domains = ['douban.com']
    start_urls = {
      'http://www.douban.com/group/explore?tag=%E8%B4%AD%E7%89%A9',
        'http://www.douban.com'
    }

    rules = (
        Rule(LinkExtractor(allow=r'/group/[^/]+/$'), callback='parse_group_homepage'),       #following the rules to extract the components by callback function
    )

    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Content-Type':'application/x-www-form-ulrencoded',
        'DNT':'1',
        # 'Host':'accounts.douban.com',
        'Host':'www.douban.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'
    }

    

    def download_captcha(self,fileurl):
        isOK = False
        try:
            if fileurl:
                logger.info('download: %s', fileurl)
                # os.remove('my_captcha.jpg')
                urllib.urlretrieve(fileurl,'my_captcha.jpg')               
                isOK = True
                logger.info('download succeed')
                # image = Image.open('my_captcha.jpg') 
                # image.show()               
            else:
                logger.info("Error fileUrl is Null")
        except:
            logger.info('download failed')
            return isOK


    def start_requests(self):
        # print "start_requests"
        logger.info('start_requests')
        return [Request("http://www.douban.com",meta = {'cookiejar':1}, callback = self.post_login)]
    

    def post_login(self,response):
        logger.info('preparing log in')
        outfile = open('post_login.html','wb')
        outfile.write(response.body)
        soup = BS(response.body)
        captcha = soup.find('img', id = 'captcha_image')
        form_data = {}
        if captcha:
            logger.info('captcha shown')
            captcha_link = captcha.get('src')
            print captcha_link
            self.download_captcha(captcha_link)
            captcha_code =  raw_input('Please enter captcha code:')
            form_data =  formdata={
                'form_email':'mccoy018@gmail.com',
                'form_password':'mccoy0104130051',
                'captcha-solution':captcha_code,
                'remember':'true'
                }
        else:
            logger.info('no captcha')
            formdata={
                'form_email':'mccoy018@gmail.com',
                'form_password':'mccoy0104130051',
                'remember':'true'
                }
        print formdata
        return [FormRequest.from_response(response,
            meta={'cookiejar':response.meta['cookiejar']},
            # headers=self.headers,
            formdata = form_data,
            callback = self.after_login,
            dont_filter = True
            )]

    def after_login(self,response):
        # check login succeed before going on
        if 'error' in response.body:
            # log.debug(response.body)
            outfile = open('log_in.html','wb')
            outfile.write(response.body)
            print 'Login Failed'
            return 
        else:
            print 'Login succeed.'
            for url in self.start_urls:
                yield self.make_requests_from_url(url)
            


    def parse_item(self, response):
        i = DoubanItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i

    def parse_group_homepage(self,response):
        self.log("Fetch group homepage: %s" % response.url)
        soup = BS(unicode(response.body.decode(response.encoding)).encode('utf-8'))
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
