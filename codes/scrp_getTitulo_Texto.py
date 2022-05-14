''' 
    Este programa captura títulos e o primeiro paragrafo de cada página.

'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    
    try:
        print(bs.h1.get_text())
        print(bs.find(id='mw-content-text').find_all('p')[0])
        #print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
            print('this page is missing something! Continuing.')
    
    for link in bs.find_all('a',href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print('-'*20)
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks('')


''' 
Melhor não testar muito...

/wiki/Category:Administrative_backlog
Category:Administrative backlog
<p>This category lists <b>backlogs</b> which require the attention of <a href="/wiki/Wikipedia:Administrators" title="Wikipedia:Administrators">administrators</a>.
Backlogs which do not require the attention of administrators may be found at <a href="/wiki/Category:Wikipedia_backlog" title="Category:Wikipedia backlog">Category:Wikipedia backlog</a>.
</p>

'''