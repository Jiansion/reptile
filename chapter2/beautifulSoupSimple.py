from urllib.request import urlopen
from bs4 import BeautifulSoup

# 通过请求网路获取网页数据
html = urlopen('http://www.pythonscraping.com/pages/page3.html').read()
bsObj = BeautifulSoup(html, 'html.parser')

# 获取 src 为 ../img/gifts/img1.jpg 的标签
imgTag = bsObj.find('img', {'src': '../img/gifts/img1.jpg'})
print('imgTag-->', imgTag)

# 获取之前取得 img 标签的 父节点标签
imgParentTag = imgTag.parent
print('imgParentTag-->', imgParentTag)

# 获取目标标签
intentTag = imgParentTag.previous_sibling
print('intentTag-->', intentTag.get_text())
'''
采用这种迂回的方案是为了防止数据位置发生改变，从而导致程序崩溃
'''
