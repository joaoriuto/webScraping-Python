from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle('http://pythonscraping.com/pages/page1.html')
if title == None:
    print('Title could not be found')
else:
    print(title)



#html = urlopen('http://pythonscraping.com/pages/page1.html')

#bsObj = BeautifulSoup(html.read())

#print(bsObj.body)

#-------------------------------------------------------------------------------

# try:
    # html = urlopen('http://pythonscraping.com/pages/page1.html')
# except HTTPError as e:
    # print(e)
# else:
    # print('continue')
    
    
# try:
    # badContent = bsObj.nonExistentTag
# except AttributeError as e:
    # print('Tag not found')
# else:
    # if badContent == None:
        # print('tag was not found')
    # else:
        # print(badContent)
    
