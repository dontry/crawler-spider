# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs


class DoubanPipeline(object):
	def __init__(self):
		self.file = codecs.open('scraped_data_utf8.json', 'w', encoding='utf-8')
		# self.file.write("ok")
	def process_item(self, item, spider):
		if item['groupName']:
			line = json.dumps(dict(item),ensure_ascii = False) + '\n'
			# line = json.dumps(dict(item)).decode('unicode-escape').encode('gbk') + '\n'
			print type(line)
			self.file.write(line)
			return item

	def spider_closed(self, spider):
		self.file.close()
