import os
import threading
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver

browserPath = ('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
homePage = 'https://mm.taobao.com/search_tstar_model.htm?'
outputDir = 'F:\photo'
parser = 'html5lib'

driver = webdriver.Chrome(executable_path=browserPath)
driver.get(homePage)
bsObj = BeautifulSoup(driver.page_source, parser)

girlsList = driver.find_element_by_id('J_GirlsList').text.split('\n')
# print(driver.find_element_by_id('J_GirlsList').text)
girlsUrl = bsObj.find_all("a",{"href": re.compile("\/\/..*\.htm\?(userId=)\d*")})
imagesUrl = re.findall('\/\/gtd\.com\/sns_logo.*\.jpg', driver.page_source)


def mkdir(path):
    isExitst = os.path.exists(path)
    if not isExitst:
        print("    [*]新建了文件夹", path)
        os.makedirs(path)
    else:
        print('    [+]文件夹', path, '已创建')