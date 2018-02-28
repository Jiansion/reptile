from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html').read()
bsObj = BeautifulSoup(html, 'html.parser')
# 使用正则匹配 ../img/gifts/img 开头 .jpg 结尾的图片
images = bsObj.findAll('img', {'src': re.compile("\.\./img/gifts/img.*\.jpg")})
for img in images:
    print(img)
    print(img['src'])
