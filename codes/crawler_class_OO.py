class Content:
    #Classe comum para artigos e páginas
    
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body
        
    def print(self):
        #Função resiliente para exibição e controle de saída.
        print('URL: {}'.format(self.url))
        print('TITLE:'.format(self.title))
        print('BODY:'.format(self.body))
        
class Website:
    #Informações estruturais do site
    
    def __init__(self, name, url, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag
        self.bodyTag = bodyTag
        
import requests
from bs4 import BeautifulSoup

class Crawler:
    
    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')
        
    def safeGet(self, pageObj, selector):
        
        ''' 
            Função que obtem uma string de conteúdo de um objeto BeautifulSoup e um seletor.
            Devolve uma string vazia caso nenhum objeto seja encontrado para o dado seletor.
        '''
        
        selectedElems = pageObj.select(selector)
        
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join([elem.get_text() for elem in selectedElems])
        else:
            return ''
    
    def parse(self, site, url):
        #Extrai o conteúdo de um URL da páginas
        
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()
                
#Definindo os objetos e dando start ao processo:

crawler = Crawler()

siteData = [
    ['O\'Reilly Media', 'http://oreilly.com', 'h1', 'section#product-description'], 
    ['Reuters', 'http://reuters.com', 'h1', 'div.StandardArticleBody_body_1gnLA'], 
    ['Brookings', 'http://www.brookings.edu', 'h1', 'div.post-body'], 
    ['New York Times', 'http://nytimes.com', 'h1', 'p.story-content'] 
    
    ]
    
websites = []

for row in siteData:
    websites.append(Website(row[0], row[1], row[2], row[3]))
    
crawler.parse(websites[0],"http://shop.oreilly.com/product/0636920028154.do")
crawler.parse(websites[1],"http://www.reuters.com/article/us-usa-epa-pruitt-idUSKBN19W2D0")
crawler.parse(websites[2],"https://www.brookings.edu/blog/techtank/2016/03/01/idea-to-retire-old-methods-of-policy-education/")
crawler.parse(websites[3],"https://www.nytimes.com/2018/01/28/business/energy-environment/oil-boom.html")