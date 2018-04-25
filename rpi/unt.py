import mechanicalsoup as ms

url = 'https://dmlsite.herokuapp.com/invoice'

browser = ms.StatefulBrowser(soup_config={'features': 'lxml'})  # ms.Browser()
browser.open(url)
soup = browser.get_current_page()
print(soup)

import aiohttp
from bs4 import BeautifulSoup as bs

response = aiohttp.ClientSession().get(url)
html = response.text()
soup = bs(html)
print(soup)