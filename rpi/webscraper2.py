"""..."""
import os
import time
import random
# from PIL import Image
# from io import BytesIO, StringIO
from urllib.parse import urlsplit  # , urljoin

import mechanicalsoup as ms
from bs4 import BeautifulSoup as bs
import requests
from typing import List, BinaryIO, Optional

# from urllib.request import urlopen
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
print(start_url + ' -> ' + save_dir)

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
    browser = ms.StatefulBrowser(soup_config={'features': 'lxml'})  # ms.Browser()
    response = browser.open(url)  # ;print(response)
    # html: str = response.text  # ;print(html)
    # soup = bs(html)
    try:
        soup = browser.get_current_page()  # ;print(soup.prettify())
    except UnicodeEncodeError:
        raise UnicodeEncodeError
    else:
        return soup
    finally:
        browser.close()

def get_none_soup(url: str) -> str:
    """Gets string of page content if not html eg. if embedded file"""
    browser = ms.StatefulBrowser(soup_config={'features': 'lxml'})  # ms.Browser()
    response = browser.open(url)  # ;print(response)
    return response.content


def download_links(start_url: str, filetypes: List[str]) -> List[str]:
    link_list: List[str] = []
    base_url = get_base_url(start_url)
    # embeddedfilenum = 0
    soup = get_soup(start_url)  # ;print(soup)
    try: 
        for index, link in enumerate(soup.select('a')):  # print(link.text, '->', link.attrs['href'])
            number_links = index
            href_raw = str(link.get('href'))
            # print(href_raw)
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
        # print(number_links, link_list)
    except AttributeError:
        # print("AttributeError: Soup returned None? Embedded file?")
        page_content = get_none_soup(start_url)
        embeddedfilenum = random.randint(0, 1000000)
        with open(save_file_dir + '/' + str(embeddedfilenum) + '.pdf', 'wb') as f:
            f.write(page_content)

    except Exception as e: 
        print(e)
    finally:
        return link_list


def download_images(start_url: str, filetypes: List[str]) -> None:
    base_url = get_base_url(start_url)
    print(start_url)
    soup = get_soup(start_url)  # ;print(soup)
    try:
        for index, image in enumerate(soup.select('img')):  # print(image)
            # image_raw = str(image)
            src_raw = str(image.get('src'))
            for image_type in filetypes:  # print(image)
                if image_type in src_raw:
                    # print(image.attrs['src'])
                    if src_raw.startswith('http'):
                        image_url = src_raw
                    elif src_raw.startswith('/'):
                        image_url = base_url + src_raw
                    # print(image_url)
                    image_response = requests.get(image_url, stream=True)
                    if image_response.status_code == 200:
                        image_name = src_raw.lstrip("/")
                        fp: BinaryIO = open(save_image_dir + '/' + 'image ' + str(index) + image_type, 'wb')
                        fp.write(image_response.content)
                        fp.close()
                        # i = Image.open(BytesIO(image_response.content))
                        # i.save(image_name)
    except Exception as e:
        pass  # print(e)

download_images(start_url, imagetype)

link_list = download_links(start_url, filetype)  # ;print(follow_urls)
url_list: List[str] = [].append(link_list)
base_url = get_base_url(start_url)

intern_links = []
extern_links = []
for leftover in link_list:  # print(leftover)
    time.sleep(0.1)
    if leftover.startswith('/'):
        start_url = base_url + leftover
        if start_url not in intern_links:
            intern_links.append(start_url) 
    elif leftover.startswith('http'):
        start_url = leftover
        if start_url not in extern_links:
            extern_links.append(start_url)
    else:
        start_url = None

print(link_list)
print(intern_links)
print(extern_links)

for start_url in intern_links:
    download_images(start_url, imagetype)
    download_links(start_url, filetype) 

if not os.path.exists(save_dir + "/results"):
    os.makedirs(save_dir + "/results")
save_results_dir = save_dir + "/results"