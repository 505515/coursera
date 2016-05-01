import urllib.request
import json

# sample data
#url = 'http://python-data.dr-chuck.net/comments_42.json'
# actual data
url = ' http://python-data.dr-chuck.net/comments_248485.json'

try:
    # hent encoding fra url, og decode etterpå med den dataen
    data = urllib.request.urlopen(url).read().decode('utf-8')
except:
    print('Invalid url', url)
    quit()

js = json.loads(data)
#print(type(js))
#print(json.dumps(js, indent=4))

count = 0

for c in js['comments']:
    cc = c['count']
    count = count + cc


print(count)

