from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import linkextractor

class MininovaSpider(CrawlSpider):

	name = 'mininova'
	allowed_domains = ['mininova.org']
	start_urls = ['http://www.mininova.org/today']
	rules = [Rule(linkextractor(allow=['/tor/\d+']),'parse_torrent']

	def parse_torrent(self,response):
		torrent = TorrentItem()
		torrent['url'] = response.url
		torrent['name'] = response.xpath('//h1/text()').extract()
		torrent['description'] = response.xpath("//div[@id='description'").extract()
		torrent['size'] = response.xpath("//div[@id='info-left']/p[2]/text()[2]|").extract()
		return torrenthttp://s1.filedais.biz:182/d/wpklrqxivt5pqngdid4j6rqja7dg5euf2arakq3uzj7bhxgquhxdjack/Mememe.rar