#Este crawler acessa conteúdos imprevisiveis - Cuidado
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.Random()

#Obtém uma lista de todos os links INTERNOS encontrados em uma página
def getInternalLinks(bs, includeUrl):
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc)
    internalLinks = []
    
    #Encontra todos os links que começam com '/'
    for link in bs.find_all('a', href=re.compile('^(/|.*'+includeUrl+')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if(link.attrs['href'].startswith('/')):
                    internalLinks.append(includeUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
                return internalLinks
    
#Obtém uma lista de todos os links EXTERNOS encontrados em uma página
def getExternalLinks(bs, excludeUrl):
    externalLinks = []
    #Encontra toso os links que começam com 'http' e que não contenham a url atual
    for link in bs.find_all('a',href=re.compile('^(http|www)((?!'+excludeUrl+').)*$')):
        if link.attrs['href'] not in externalLinks:
            externalLinks.append(link.attrs['href'])
    return externalLinks
    
def getRandomExternalLinks(startingPage):
    html = urlopen(startingPage)
    bs = BeautifulSoup(html, 'html.parser')
    externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print('No external links, looking around the site for one')
        domain = '{}://{}'.format(urlparse(startingPage).scheme, urlparse(startingPage).netloc)
        internalLinks = getInternalLinks(bs, domain)
        return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]
        
def followExternalOnly(startingSite):
    externalLink = getRandomExternalLinks(startingSite)
    print('Random external link is: {}'.format(externalLink))
    
followExternalOnly('http://oreilly.com')
        
                    