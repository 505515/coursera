import xml.etree.ElementTree as ET
import urllib.request

#url = 'http://python-data.dr-chuck.net/comments_42.xml'
url = 'http://python-data.dr-chuck.net/comments_248481.xml'

try:
    print('Retriving url:', url)
    html = urllib.request.urlopen(url)
    meta = html.info() # header
    html = html.read()
    print('Retrived', meta['Content-Length'], 'characters')
except:
    print('Not a valid url or could not open url', url)
    quit()

xmldata = ET.fromstring(html)
comment = xmldata.findall('comments/comment')
# or
comment = xmldata.findall('.//comment')

c = 0

for i in comment:
    x = i.find('count').text
    c = c + int(x)

print('Sum:', c)
