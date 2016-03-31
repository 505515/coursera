import socket
import urllib.request
import re

# using socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.pythonlearn.com', 80))

mysock.send(('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n').encode())

while True:
    data = mysock.recv(512).decode()
    if len(data) < 1:
        break
    #print(data)

mysock.shutdown(socket.SHUT_RDWR)
mysock.close()

# using urllib

url = 'http://www.pythonlearn.com/code/intro-short.txt'
ourl = urllib.request.urlopen(url)

for i in ourl:
    i = i.strip()
    x = str(i)
    y = re.findall('\'(\S+[a-zA-Z0-9 ().,]+)', x)
#    print(y)

page = urllib.request.urlopen(url).read()

#with urllib.request.urlopen(url) as response:
#    page = response.read()

print(type(page)) # is bytes
print(page)

decodepage = page.decode('utf-8')

print(type(decodepage)) # is string
print(decodepage)

x = decodepage.split()
print(x)

# beautifulsoup
from bs4 import *

url = 'http://www.pythonlearn.com'

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('a')

for tag in tags:
    href = tag.get('href', None)
    if href.startswith('http'):
        print(href)

    #print(tag.get('href', None))





