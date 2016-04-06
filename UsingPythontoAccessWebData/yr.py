import xml.etree.ElementTree as ET
import urllib.request

url = 'http://www.yr.no/sted/Norge/oslo/oslo/oslo/varsel.xml'

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
forecast = xmldata.findall('forecast/text/location/time')

for i in forecast:
    x = i.find('body').text
    print(x)