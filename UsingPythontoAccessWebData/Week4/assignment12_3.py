import urllib.request
from bs4 import *

urllist = []
namelist = []

# sample problem
"""
starturl = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
startname = 'Fikret'
interval = 4
position = 3
"""

# problem
starturl = 'http://python-data.dr-chuck.net/known_by_Safia.html'
startname = 'Safia'
interval = 7
position = 18

urllist.append(starturl)
namelist.append(startname)

def openpage(url):
    try:
        html = urllib.request.urlopen(url).read()
        bsit = BeautifulSoup(html, 'html.parser')
        return(bsit)
    except:
        print('Not a valid url or could not open url', url)
        quit()

def addvalues():

    tmpurllist = []
    tmpnamelist = []

    for l in soup.find_all('a', href=True):

        tmpurllist.append(l.get('href'))
        tmpnamelist.append(l.get_text())

    urllist.append(tmpurllist[position - 1])
    namelist.append(tmpnamelist[position - 1])

for i in range(0,interval):
    url = urllist[i]
    soup = openpage(url)
    addvalues()

print(namelist[interval])