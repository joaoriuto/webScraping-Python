# http://www.pythonscraping.com/pages/page3.html

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

# for filho in bs.find('table', {'id':'giftList'}).children:
    # print(filho)

# for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings:
    # print(sibling)
    
print(bs.find('img',{'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())