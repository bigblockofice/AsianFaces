import requests
import urllib.request
from bs4 import BeautifulSoup
import re

def image_download(url):
    regex = re.search("([^./]+).jpg$", url)
    image_name = regex.group()
    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
                      'AppleWebKit/537.11 (KHTML, like Gecko) '
                      'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
    f = open(image_name, 'wb')
    req = urllib.request.Request(url, headers=header)
    f.write(urllib.request.urlopen(req).read())
    f.close()
    
def main_image(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features="html.parser")
    for link in soup.findAll('img', {'class' : 'carousel-desktop img-responsive hide_on_m adx_small_desktop'}):
        image_url = "https:" + link.get('src')
        print(image_url)
        image_download(image_url)

def people_download(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, features="html.parser")
    for link in soup.findAll('a'):
        print(link.get('href'))
        
##image_download('https://www.thefamouspeople.com/profiles/hayao-miyazaki-4814.php')

text = "https://www.thefamouspeople.com/profiles/thumbs/hayao-miyazaki-8.jpg"

people_download("https://www.thefamouspeople.com/ajax/page_ajax.php")
