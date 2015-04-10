from scrapy.item import Item, Field

class TorrentItem(scrapy.item):
	url = scrapy.Field()
	name = scrapy.Field()
	description = scrapy.Field()
	size = scrapy.Field()


