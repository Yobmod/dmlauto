import mechanicalsoup as ms
from urllib.parse import urlsplit, urljoin
from PIL import Image
from io import StringIO, BytesIO
import requests
import time
import os

# from urllib.request import urlopen
# from bs4 import BeautifulSoup as bs
# import urllib3
# import re
# from string import printable

DEBUG = True

if DEBUG:
    url = "http://www.irrelevantcheetah.com/browserimages.html"
else:
    url = "http://" + input("Where would you like to start searching?\n")
print(url)

filetype = [".pdf", ".epub", ".mobi"]
imagetype = [".jpg", ".ico", ".gif"]

browser = ms.StatefulBrowser(soup_config={'features': 'html5lib'})  # ms.Browser()
response = browser.open(url)  # ;print(response)
browser_url = response.url  # browser.get_url()  # ;print(browser_url)
split_url = urlsplit(browser_url)  # ;print(browser_url)
base_url = split_url.scheme + "://" + split_url.netloc  # ;print(base_url)
html = response.text  # ;print(html)
soup = browser.get_current_page()  # ;print(soup.prettify())
browser.close()

dir = os.getcwd()
print(dir)

for link in soup.select('a'):
    # print(link.text, '->', link.attrs['href'])
    # link_raw = str(link)
    href_raw = str(link.get('href'))
    if any(x in href_raw for x in filetype):
        # print(link)
        # print(link.attrs['href'])
        pass

for image in soup.select('img'):  # print(image)
    image_raw = str(image)
    src_raw = str(image.get('src'))
    if any(x in src_raw for x in imagetype):  # print(image)
        # print(image.attrs['src'])
        image_response = requests.get(base_url + src_raw, stream=True)
        if image_response.status_code == 200:
            image_name = src_raw.lstrip("/")
            f = open(dir + '/' + image_name,'wb')
            f.write(image_response.content)
            f.close()
            #i = Image.open(BytesIO(image_response.content))
            #i.save(image_name)


    
"""  # w/o mechanicalsoup method
response = requests.get(url)  # ;print(response)
html: str = response.text  # ;print(html)
# parsers: 'lxml, 'html.parser', 'hml5lib'
soup = bs(html, 'lxml')  # ;print(soup.prettify())
for link in soup.find_all('a'):
    print(link.get('href'))
for image in soup.find_all('img'):
    # print(image)
    image_raw = str(image)
    if ".jpg" in image_raw:
        print(image.attrs['src'])
"""
