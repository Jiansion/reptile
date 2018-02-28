import re
from urllib.request import urlopen

from bs4 import BeautifulSoup

# html = urlopen('http://www.qianjia.com/').read()
# bsObj = BeautifulSoup(html, 'html.parser')
# aList = bsObj.findAll('a', href=re.compile('^http'))
# # 用于保存链接,使用 set() 实现链接去重
# pages = set()
# for link in aList:
#     href = link['href']
#     if href not in pages:
#         pages.add(href)
#

pages = set()


def getLink(pageUrl):
    global pages
    try:
        html = urlopen(pageUrl).read()
        bsObj = BeautifulSoup(html, 'html.parser')
        aList = bsObj.findAll('a', href=re.compile('^http'))
        for link in aList:
            href = link['href']
            if href not in pages:
                pages.add(href)
                print(href)
                getLink(href)
    except Exception as e:
        print(e)


getLink('http://www.qianjia.com/')
