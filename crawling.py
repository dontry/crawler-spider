<<<<<<< HEAD
#encoding:UTF-8
import urllib.request

url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
# data = data.decode('UTF-8')
print(data)

data1 = {}
data1['word'] = 'Jecvay Notes'

url_values = urllib.parse.urlencode(data1)
url =  "http://www.baidu.com/s?"
full_url = url + url_values

data1 = urllib.request.urlopen(full_url).read()
# data1 = data.decode('UTF-8')
print(data1)
=======
#encoding:UTF-8
import urllib.request

url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
# data = data.decode('UTF-8')
print(data)

data1 = {}
data1['word'] = 'Jecvay Notes'

url_values = urllib.parse.urlencode(data1)
url =  "http://www.baidu.com/s?"
full_url = url + url_values

data1 = urllib.request.urlopen(full_url).read()
# data1 = data.decode('UTF-8')
print(data1)
>>>>>>> 21fe4fce0100a233f0a22ed0d819b061ac9fe4fd
