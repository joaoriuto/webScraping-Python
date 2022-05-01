#Importar libs

#Biblioteca padrão + urlopen
from urllib.request import urlopen
#Importar o BeautifulSoap 4
from bs4 import BeautifulSoup
import re

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')

#Funções

#Primeira versão (requisição geral)
# for link in bs.find_all('a'):
    # if 'href' in link.attrs:
        # print(link.attrs['href'])
        
#Versão com regex
for link in bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])