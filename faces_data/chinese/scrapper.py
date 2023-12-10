import requests
import urllib
from bs4 import BeautifulSoup
import re


url = "https://www.thefamouspeople.com/ajax/page_ajax.php"

header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
                     'AppleWebKit/537.11 (KHTML, like Gecko) '
                      'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

def image_download(url):
    regex = re.search("([^./]+).jpg$", url)
    try:
        image_name = regex.group()
    except AttributeError:
        return None
    if image_name == ("not-found.jpg"):
        return None
    print((image_name))
    f = open(image_name, 'wb')
    req = urllib.request.Request(url, headers=header)
    try:
        f.write(urllib.request.urlopen(req).read())
    except urllib.error.HTTPError:
        return None
    f.close()

for i in range(96, 2000, 21):
    data = "action=scrollpagination&number=21&offset="+ str(i) + "&sqlc=%5B%22country_id%3D45%22%5D&c1=country_master&c2="
    data = bytes(data, 'utf-8')
    req = urllib.request.Request(url, headers=header, data = data)
    plain_text = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(plain_text, features="html.parser")
    for link in soup.findAll('img', {'class' : 'img-responsive img-thumbnail-new margincls rp deskdefineheight'}):
        image_url = "https:" + link.get('src')
        print(image_url)
        image_download(image_url)

