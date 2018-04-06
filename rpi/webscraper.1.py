import BeautifulSoup as bs

import re

doc = ['<html><head><title>Page title</title></head>',
       '<body><p id="firstpara" align="center">This is paragraph <b>one</b>.',
       '<p id="secondpara" align="blah">This is paragraph <b>two</b>.',
       '</html>']

soup = bs(''.join(doc))  # not a double quote

print(soup.prettify())

m = re.search(r'(?<=-)\w+', 'free-bird')
m.group(0)
