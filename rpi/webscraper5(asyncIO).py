"""..."""
import asyncio
import os
import re

from typing import BinaryIO, List, Set  # Optional, AnyStr, Union
from urllib.parse import urlsplit  # , urljoin

import mechanicalsoup as ms  # TODO(swap for aiohttp)
import aiohttp
from bs4 import BeautifulSoup as bs

# import random
# from urllib.request import urlopen
# import urllib3
# import re
# from string import printable
# from PIL import Image
# from io import BytesIO, StringIO

DEBUG = True

if DEBUG:
    start_url = "https://dmlsite.herokuapp.com"
    save_dir: str = os.path.abspath(os.path.dirname(__file__))  # ;print(save_dir)
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

if not os.path.exists(save_dir + "/results"):
    os.makedirs(save_dir + "/results")
save_results_dir = save_dir + "/results"

filetype = [".pdf", ".epub", ".mobi"]
imagetype = [".jpg", ".ico", ".gif"]


async def get_base_url(url: str) -> str:
    """."""
    browser_url: str = url  # browser.get_url()  # ;print(browser_url)
    split_url = urlsplit(browser_url)  # ;print(browser_url)
    base_url = split_url.scheme + "://" + split_url.netloc  # ;print(base_url)
    return base_url


async def get_soup(url: str) -> bs:
    """."""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # print(response.status)
            # print(await response.text())
            try:
                html: str = await response.text(encoding='utf-8')  # ;print(html)
                soup = bs(html, 'lxml')  # ;print(soup.prettify())
            except Exception as e:  # or; if soup is None...
                pass
                # print(e)
                # print(response)
                # raise UnicodeEncodeError
            else:
                return soup


async def get_none_soup(url: str) -> bytes:
    """Get string of page content if not html eg. if embedded file."""
    browser = ms.StatefulBrowser(soup_config={'features': 'lxml'})  # ms.Browser()
    response = browser.open(url)  # ;print(response)
    return response.content


async def download_unknowns(url: str) -> None:
    """."""
    page_content: bytes = await get_none_soup(url)
    page_string: bytes = page_content[0:100]
    # print(page_string)
    """parse section of page bytes and use as name. If unknown encoding
    convert to number string (exclude first few bytes that state filetype) """
    try:
        page_unicode = page_string.decode("ISO-8859-1").replace(R'%', '_')
        page_parsed = [char for char in page_unicode if char.isalnum() or char == '_']
        unknown_file_name = "".join(page_parsed)[10:30]
        # print(page_unicode)
    except UnicodeDecodeError:
        try:
            page_unicode = page_string.decode('utf-8').replace(R'%', '_')
            page_parsed = [char for char in page_unicode if char.isalnum() or char == '_']
            unknown_file_name = "".join(page_parsed)[10:30]
        except UnicodeDecodeError:
            unknown_file_name = "unk_"
            for char in page_content[10:30]:
                if char != b'\\':
                    unknown_file_name += str(char)
    print(unknown_file_name)
    """check beginning of page bytes for a filetype"""
    if b'%PDF' in page_string:  # ;
        extension = '.pdf'
    else:
        extension = '.unk.txt'

    with open(save_file_dir + '/' + unknown_file_name + extension, 'wb') as file:
        file.write(page_content)  # ; print(save_file_dir)


async def make_dir_from_href(href: str) -> str:
    """."""
    href_raw = str(href)
    href_slash_ind = [i for i, ind in enumerate(href_raw) if ind == '/']  # ; print(href_slash_ind)
    if len(href_slash_ind) == 2:
        directory_name = href_raw[(href_slash_ind[0] + 1):href_slash_ind[1]]  # ; print(directoryName)
    elif len(href_slash_ind) == 1:
        directory_name = href_raw[(href_slash_ind[0] + 1):-1]  # ; print(directoryName)
    if not os.path.exists(save_file_dir + '/' + directory_name):
        os.makedirs(save_file_dir + '/' + directory_name)
    return directory_name


async def download_links(start_url: str, filetypes: List[str]) -> List[str]:
    """."""
    link_list: List[str] = []
    base_url = await get_base_url(start_url)

    try:  # TODO /invoice is returning a soup instead of error, investigate why
        soup = await get_soup(start_url)  # ;print(soup)
        for index, link in enumerate(soup.select('a')):  # print(link.text, '->', link.attrs['href'])
            href: str = link.get('href')  # TODA(do i need to stringify?)
            href_raw = str(href)
            if any(x in href_raw for x in filetypes):  # print(link.attrs['href'])
                await make_dir_from_href(href)
                async with aiohttp.ClientSession() as session:
                    async with session.get(base_url + href_raw) as response:
                        link_response = await response
                        if link_response.status == 200:
                            link_name = href_raw.lstrip("/") + '_' + str(index)
                            f: BinaryIO
                            with open(save_file_dir + '/' + link_name, 'wb') as f:
                                f.write(link_response.content)
            elif ".htm" in href_raw:
                link_list.append(href_raw)
            else:
                link_list.append(href_raw)
        # print(number_links, link_list)
    except (AttributeError, UnicodeDecodeError):
        # print("AttributeError: Soup returned None? Embedded file?")
        await download_unknowns(start_url)
    except Exception as e:
        # print(e)
        # print(start_url)
        await download_unknowns(start_url)

    finally:
        return link_list


async def download_images(start_url: str, filetypes: List[str]) -> None:
    """.."""
    base_url = await get_base_url(start_url)
    # print(start_url)

    try:
        soup = await get_soup(start_url)  # ;print(soup)
    except UnicodeDecodeError:
        soup = None
    if soup is not None:
        for index, image in enumerate(soup.select('img')):  # print(image)
            # image_raw = str(image)
            src_raw = str(image.get('src'))  # print(image.attrs['src'])
            if src_raw.startswith('http'):
                image_url = src_raw
            elif src_raw.startswith('/'):
                image_url = base_url + src_raw
            else:
                image_url = src_raw
            # print(image_url)
            for image_type in filter(lambda x: x in src_raw, filetypes):  # print(image)
                async with aiohttp.ClientSession() as session:
                    async with session.get(image_url) as response:
                        image_response = response
                        # print(await image_response.read())
                        image_binary: bytes = await image_response.read()
                        if image_response.status == 200:
                            image_name = re.sub(r'.*/', '', src_raw).replace(R'.', '_')
                            # print(image_name, index)
                            fp: BinaryIO = open(save_image_dir + '/' + image_name + str(index) + image_type, 'wb')
                            fp.write(image_binary)
                            fp.close()
                            # i = Image.open(BytesIO(image_response.content))
                            # i.save(image_name)


async def get_url_from_list() -> List[str]:
    """."""
    link_list = await download_links(start_url, filetype)  # ;print(follow_urls)
    base_url = await get_base_url(start_url)
    await asyncio.sleep(0.1)

    url_list: List[str] = []
    url_list += link_list
    intern_links: List[str] = []
    extern_links: List[str] = []
    for x in url_list:
        # print(x)
        if x.startswith('/'):
            the_url = base_url + x
            if the_url not in intern_links:
                intern_links.append(the_url)
        elif x.startswith('http'):
            the_url = x
            if the_url not in extern_links:
                extern_links.append(the_url)
        else:
            the_url = ""  
    # print(intern_links)
    return intern_links

async def main() -> None:
    """."""
    url_list = await get_url_from_list()
    # print(url_list)
    for url in url_list:
            print(url)
            await download_links(url, filetype),
            await download_images(url, imagetype),

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

# print(link_list)
# print(intern_links)
# print(extern_links)

""" with ThreadPoolExecutor(max_workers=50) as pool:
    futures: List[Future] = []
    link_set: Set[str] = set()
    for the_url in intern_links:
        pool.submit(print, the_url)
        pool.submit(download_images, the_url, imagetype)
        future = pool.submit(download_links, the_url, filetype)
        futures.append(future)

    for future in as_completed(futures):
        link_set = link_set | set(future.result())
        link_setlist = sorted(link_set)
    # print(link_set)

    with open(save_results_dir + '/' + 'link_set.txt', 'w') as res_file:
        for link in link_setlist:
            res_file.write(link + '\n') """
