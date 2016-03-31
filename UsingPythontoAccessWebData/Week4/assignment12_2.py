import re
import urllib.request
from bs4 import *

try:
    url = input('Enter - ')
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
except:
    print('Not a valid url', url)
    quit()

span = soup.find_all('span', {'class': 'comments'})

s = 0
c = 0

for i in span:
    i = str(i)
    x = re.findall('>([0-9]+)', i)
    x = x[0]
    x = int(x)
    s = x + s
    c = c + 1

print('Count', c)
print('Sum', s)
