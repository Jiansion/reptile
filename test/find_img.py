from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.qianjia.com/").read()
bsObj = BeautifulSoup(html, 'html.parser')
imgList = bsObj.findAll('img')
for img in imgList:
    try:
        title = img['alt']
        if title == '':
            title = "图片没有说明"
    except Exception as e:
        title = "图片没有说明"
    print(img['src'], title)
