"""..."""
import os
import time
# from PIL import Image
# from io import BytesIO, StringIO
from urllib.parse import urlsplit  # , urljoin

import mechanicalsoup as ms
import requests
from typing import List, BinaryIO, Optional

# from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
# import urllib3
# import re
# from string import printable

DEBUG = True

if DEBUG:
    start_url = "https://dmlsite.herokuapp.com"
    save_dir: str = os.path.abspath(os.path.dirname(__file__)) # ;print(save_dir)
else:
    start_url = "http://" + input("Where would you like to start searching?\n")
    save_dir = os.getcwd()  # ;print(save_dir)
print(start_url + '->' + save_dir)

if not os.path.exists(save_dir + "/images"):
    os.makedirs(save_dir + "/images")
save_image_dir = save_dir + "/images"

if not os.path.exists(save_dir + "/files"):
    os.makedirs(save_dir + "/files")
save_file_dir = save_dir + "/files"

filetype = [".pdf", ".epub", ".mobi"]
imagetype = [".jpg", ".ico", ".gif"]


def get_base_url(url: str) -> str:
    browser = ms.StatefulBrowser(soup_config={'features': 'html5lib'})  # ms.Browser()
    response = browser.open(url)  # ;print(response)
    browser_url: str = response.url  # browser.get_url()  # ;print(browser_url)
    split_url = urlsplit(browser_url)  # ;print(browser_url)
    base_url = split_url.scheme + "://" + split_url.netloc  # ;print(base_url)
    return base_url


def get_soup(url: str) -> bs:
    browser = ms.StatefulBrowser(soup_config={'features': 'html5lib'})  # ms.Browser()
    response = browser.open(url)  # ;print(response)
    # html: str = response.text  # ;print(html)
    # soup = bs(html)
    soup: bs = browser.get_current_page()  # ;print(soup.prettify())
    browser.close()
    return soup


base_url = get_base_url(start_url)
soup = get_soup(start_url)  # ;print(soup)
link_list: List[str] = []

def download_links(soup: bs, start_url: str, filetypes: List[str]) -> List[str]:
    # link_list: List[str] = []
    for i, link in enumerate(soup.select('a')):  # print(link.text, '->', link.attrs['href'])
        href_raw = str(link.get('href'))
        print(href_raw)
        if any(x in href_raw for x in filetype): # print(link.attrs['href'])
            href_slash_ind = [i for i, ind in enumerate(href_raw) if ind == '/'] #; print(href_slash_ind)
            if len(href_slash_ind) > 1:
                directoryName = href_raw[(href_slash_ind[0]+1):href_slash_ind[1]]  #; print(directoryName)
            elif len(href_slash_ind) == 1:
                directoryName = href_raw[(href_slash_ind[0]+1):-1]  ; print(directoryName)
            if not os.path.exists(save_file_dir + '/' + directoryName):
                os.makedirs(save_file_dir + '/' + directoryName)
            
            link_response = requests.get(base_url + href_raw, stream=True)
            if link_response.status_code == 200:
                link_name = href_raw.lstrip("/")
                f: BinaryIO
                with open(save_file_dir + '/' + link_name, 'wb') as f:
                    f.write(link_response.content)
        elif ".htm" in href_raw:
            link_list.append(href_raw)
        else:
            link_list.append(href_raw)
    print(link_list)
    return link_list


download_links(soup, start_url, filetype)  # ;print(follow_urls)


def download_images(soup: bs) -> None:
    for image in soup.select('img'):  # print(image)
        image_raw = str(image)
        src_raw = str(image.get('src'))
        if any(x in src_raw for x in imagetype):  # print(image)
            # print(image.attrs['src'])
            image_response = requests.get(base_url + src_raw, stream=True)
            if image_response.status_code == 200:
                image_name = src_raw.lstrip("/")
                fp: BinaryIO = open(save_dir + '/' + image_name, 'wb')
                fp.write(image_response.content)
                fp.close()
                # i = Image.open(BytesIO(image_response.content))
                # i.save(image_name)

download_images(soup)
print(link_list)

for leftover in link_list:  # print(leftover)
    time.sleep(0.1)
    if leftover.startswith('/'):
        start_url = base_url + leftover 
    elif leftover.startswith('http'):
        start_url = leftover
    print(start_url)
    soup = get_soup(start_url) # ; print(soup)
    download_images(soup)
    #download_links(soup, start_url, filetype) 

