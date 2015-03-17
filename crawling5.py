import requests
from bs4 import BeautifulSoup

response = requests.get("http://jecvay.com")
soup = BeautifulSoup(response.text)

print(soup.title.text)

for x in soup.findAll("a"):
	print(x['href'])


soup1 = BeautifulSoup(requests.get("http://www.zhihu.com").text)
print(soup1.find("input",{"name":"_xsrf"})['value'])