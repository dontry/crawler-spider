from  bs4 import BeautifulSoup  as BS
# from douban.items import DoubanItem
import re
import requests
import urllib


def download_captcha(fileurl):
    isDownOK = False

    try:
        if fileurl:
            # outfile = open(r'my_captcha.jpg','wb')
            # outfile.write(urllib.urlopen(fileurl).read())
            os.remove('captcha.jpg')
            urllib.urlretrieve(fileurl,'captcha.jpg')       
            isDownOK =True
            print 'Download Succeeded'
        else:
            print 'Error fileUrl is Null'
            isDownOK = False
    except:    
        print 'Download Failed'
        return isDownOK

if __name__ == "__main__":
    url = "http://www.douban.com/group/blackeye/"
    response = requests.get(url)
    soup = BS(response.text)
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
    url = "http://www.douban.com"
    response = requests.get(url)
    soup = BS(response.text)
    captcha = soup.find('img', id = 'captcha_image')
    captcha_link = captcha.get("src")
    print captcha_link
    download_captcha(captcha_link)
	# regEx = 'http://.*(?<=\")'
	# linkCmp = re.compile(regEx)
	# captcha_link = linkCmp.findall(captcha.get_text())
	# print captcha_link[0].decode()

