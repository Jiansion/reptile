from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen('http://www.pythonscraping.com/pages/page3.html')
html = response.read()
bsObj = BeautifulSoup(html, 'html.parser')
# 查找 id 为 giftList 的 table 标签，并遍历打印其中的直接子节点
childrenList = bsObj.find('table', {'id': 'giftList'}).children
for child in childrenList:
    print(child, '----')


# 提取目标标签下的所有 img 标签
# imgList = bsObj.div.table.findAll('img')
# for img in imgList:
#     print(img)
