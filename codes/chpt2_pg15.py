from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bsObj = BeautifulSoup(html.read(), 'xml')

nameList = bsObj.findAll('span', {'class' : 'green', 'class':'red'})
textList = bsObj.findAll('div', {'id':'text'})
textInP = bsObj.body.div

# for name in nameList:
    # print(name.get_text())
  
# for texto in textList:
  # print(texto.get_text())

for p in textInP:
    print(p.get_text())
    print(p)
    