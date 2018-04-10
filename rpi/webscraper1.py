import mechanicalsoup

import time
from bs4 import BeautifulSoup
import re
import urllib
import string
import os
 
def downloadProcess (html, base, filetype, linkList):
    """This does the actual file downloading."""
    soup = BeautifulSoup(html, "lxml")
    print(soup)
    for link in soup.find_all('a'):
        linkText = str(link.get('href'))
 
    if filetype in linkText:
        slashList = [i for i, ind in enumerate(linkText) if ind == '/']
        directoryName = linkText[(slashList[0]+1):slashList[1]]
        if not os.path.exists(directoryName):
            os.makedirs(directoryName)
        linkGet = base + linkText
        #image = requests.get(linkGet)
        #
        #filesave = linkText.lstrip("/")
        #image.retrieve (linkGet, filesave)
    elif "htm" in linkText: #covers both "html" and "htm"
        linkList.append(link)
 
start = "http://" + input ("Where would you like to start searching?\n")
filetype = input ("What file type are you looking for?\n")
 
numSlash = start.count('/') #number of slashes in start—need to remove everything after third slash
slashList = [i for i, ind in enumerate(start) if ind == '/'] #list of indices of slashes
 
if (len(slashList) >= 3): #if there are 3 or more slashes, cut after 3
    third = slashList[2]
    base = start[:third] #base is everything up to third slash
else:
    base = start
 
br = mechanicalsoup.StatefulBrowser(soup_config={'features': 'html5lib'}) 
r = br.open(start)
html = r.text
linkList = [] #empty list of links

print("Parsing " + start)
downloadProcess(html, base, filetype, linkList)
 
for leftover in linkList:
    time.sleep(0.1)  # wait 0.1 seconds to avoid overloading server
    linkText = str(leftover.get('href'))
    print("Parsing " + base + linkText)
    br = mechanicalsoup.StatefulBrowser(soup_config={'features': 'html5lib'}) 
    r = br.open(base + linkText)
    html = r.text
    linkList = []
    downloadProcess(html, base, filetype, linkList)