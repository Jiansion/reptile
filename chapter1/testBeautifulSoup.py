from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen("http://pythonscraping.com/pages/page1.html")
html = response.read()
# 通过 解析获取 BeautifulSoup 对象
bsObj = BeautifulSoup(html, 'html.parser')
# 通过标签名获取信息，直接通过解析的对象获取 HTML 标签内容
print('h1==>', bsObj.h1)
print('title==>', bsObj.title)
print('div==>', bsObj.div)
