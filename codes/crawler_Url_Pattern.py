#Sem instruções específicas para posições de links

class Website:
    def __init__(self, name, url, targetPattern, absoluteUrl, littleTag, bodyTag):
        self.name = name
        self.url = url
        self.targetPattern = targetPattern
        self.absoluteUrl = absoluteUrl
        self.littleTag = littleTag
        self.bodyTag = bodyTag
        
class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body
        
        
    def print(self):
        print("Url: {}".format(self.url))
        print("Title: {}".format(self.title))
        print("Body: {}".format(self.body))


'''
    Encontra na página inicial, links internos e realiza o parse
    de cada um.
'''
import re
import requests
from bs4 import BeautifulSoup

class Crawler:
    def __init__(self, site):
        self.site = site
        self.visited = []
        
    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')
        
    def safeGet(self, pageObj, selector):
        selectedElems = pageObj.select(selector)
        if selectedElems is not None and len(slectedElems) > 0:
            return '\n'.join([elem.get_text() for 
                elem in selectedElems]) 
        return ''
        
    def parse(self, url):
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, self.site.titleTag)
            body = self.safeGet(bs, slef.site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()
                
    def crawl(self):
        '''
            Obtém páginas da página inicial do site
        '''
        bs = self.getPage(self.site.url)
        targetPages = bs.findAll('a', href = re.compile(self.site.targetPattern))
        for targetPage in targetPages:
            targetPage = targetPage.attrs['href']
            if targetPage not in self.visited:
                self.visited.append(targetPage)
                if not self.site.absoluteUrl:
                    targetPage = '{}{}'.format(self.site.url, targetPage)
                self.parse(targetPage)
                

reuters = Website('Reuters', "https://www.reuters.com", '^(/article/)', False, 'h1', 'div.StandardArticleBody_body_1gnLA')
crawler = Crawler(reuters)
crawler.crawl()