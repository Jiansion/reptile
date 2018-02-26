# 演示 BeautifulSoup 通过标签的属性查找标签数据
from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
html = response.read()
bsObj = BeautifulSoup(html, 'html.parser')

# 获取 Html 中所有的 属性为 green 的 span 标签,并封装为一个 list
nameList = bsObj.findAll('span', {'class': 'green'})
'''
使用 findAll 可以查找指定的所有标签
'''
# 遍历列表数据，并去除 HTML 标签
for data in nameList:
    print(data.get_text())
