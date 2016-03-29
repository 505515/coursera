import socket
import urllib.request
import re

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.pythonlearn.com', 80))

mysock.send(('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n').encode())

while True:
    data = mysock.recv(512).decode()
    if len(data) < 1:
        break
    #print(data)

mysock.close()

url = 'http://www.pythonlearn.com/code/intro-short.txt'
ourl = urllib.request.urlopen(url)

for i in ourl:
    i = i.strip()
    x = str(i)
    y = re.findall('\'(\S+[a-zA-Z0-9 ().,]+)', x)
    print(y)
