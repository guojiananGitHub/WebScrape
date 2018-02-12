from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

# html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
# bsObj = BeautifulSoup(html)
# for link in bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])


# 實現一個網站上隨機地從一個鏈接跳到另一個鏈接
# random.seed(datetime.datetime.now())
#
#
# def getLinks(articleUrl):
#     html = urlopen("http://en.wikipedia.org"+articleUrl)
#     bsObj = BeautifulSoup(html)
#     return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
#
# links = getLinks("/wiki/Kevin_Bacon")
# while len(links) > 0:
#     newArtcle = links[random.randint(0, len(links)-1)].attrs["href"]
#     print(newArtcle)
#     links = getLinks(newArtcle)


# 去重
pages = set()


def getLinks(pageUrl):
    global pages
    html = urlopen("https://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html)
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").findAll("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs["href"])
    except AttributeError:
        print("頁面缺少一些屬性")
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 遇到新頁面
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks("")