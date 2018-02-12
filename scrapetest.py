from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
# def getTitle(url):
#     try:
#         html = urlopen(url)
#     except (HTTPError, URLError) as e:
#         return None
#     try:
#         bsObj = BeautifulSoup(html.read())
#         title = bsObj.body.h1
#     except AttributeError as e:
#         return None
#     return title
#     title = getTitle("http://www.pythonscraping.com/pages/page1.html")
#     if title == None:
#         print("Title coule not be found")
#     else:
#         print(title)

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)
nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())