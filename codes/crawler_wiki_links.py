from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            #encontramos uma nova página
            newPage = link.attrs['href']
            print(newPage)
            pages.add(newPage)
            getLinks(newPage)
    
getLinks('')

''' 
saída: Wikipedia:Protection_policy#semi

'''