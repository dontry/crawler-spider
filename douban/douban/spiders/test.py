from  bs4 import BeautifulSoup  
# from douban.items import DoubanItem
import re
import requests


if __name__ == "__main__":

	url = "http://www.douban.com/group/blackeye/"
	response = requests.get(url)
	soup = BeautifulSoup(response.text)
  	tag = soup.find_all('div',{"class":"side-nav"})
  	# item = DoubanItem()
  	print tag
	members = tag[0].find('a').string
	numCmp = re.compile("""\d+""")
	number = numCmp.findall(members)
	print number[0].decode()
	# print members
    # match = re.compile("""\\d+""")
    # number = members.find_all(match)
    # item['totalNumber'] = number
    # print item['totalNumber']
    # print item['groupURL']