from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import re
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

# html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
# bsObj = BeautifulSoup(html)
# nameList = bsObj.findAll("span", {"class":"green"})
# for name in nameList:
#     print(name.get_text())


html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)

# 只找出子標籤，用.children標籤
# for child in bsObj.find("table", {"id": "giftList"}).children:
#     print(child)


# 處理兄弟標籤
# for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
#     print(sibling)


# 父標籤處理
# print(bsObj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling)


# 通過文件途徑查找信息
# images = bsObj.findAll("img", {"src": re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
# for image in images:
#     print(image["src"])


# print(bsObj.img.attrs)  # 獲取屬性
# print(bsObj.img.attrs["src"])  # 獲取資源位置


# lambda表達式
print(bsObj.findAll(lambda tag: len(tag.attrs) == 2))