<<<<<<< HEAD
import re
import urllib.request
import urllib

from collections import deque

queue = deque()
visited = set()

url = 'http://news.dbanotes.net'

queue.append(url)
cnt = 0 

while  queue:
	pass
	url = queue.popleft()
	visited |={url}

	print('already fetched' + str(cnt) + 'now fetching <----' + url)
	cnt += 1
	urlop = urllib.request.urlopen(url)
	if 'html' not in urlop.getheader('Content-Type'):
		continue

	try:
		data = urlop.read().decode('utf-8')
	except:
		continue

	linkre = re.compile('href=\"(.+?)\"')

	for x in linkre.findall(data):
		if 'http' in x and x not in visited:
			queue.append(x)
=======
import re
import urllib.request
import urllib

from collections import deque

queue = deque()
visited = set()

url = 'http://news.dbanotes.net'

queue.append(url)
cnt = 0 

while  queue:
	pass
	url = queue.popleft()
	visited |={url}

	print('already fetched' + str(cnt) + 'now fetching <----' + url)
	cnt += 1
	urlop = urllib.request.urlopen(url)
	if 'html' not in urlop.getheader('Content-Type'):
		continue

	try:
		data = urlop.read().decode('utf-8')
	except:
		continue

	linkre = re.compile('href=\"(.+?)\"')

	for x in linkre.findall(data):
		if 'http' in x and x not in visited:
			queue.append(x)
>>>>>>> 21fe4fce0100a233f0a22ed0d819b061ac9fe4fd
			print('add to queue --->' + x)