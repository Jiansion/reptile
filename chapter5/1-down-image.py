from urllib.request import urlopen
from urllib.request import urlretrieve

from bs4 import BeautifulSoup

host = "http://www.qianjia.com/"
downloadDirectory = 'downlaoded'


def getImageUrl(baseUrl, soure):
    if soure.startswith('http'):
        url = soure
    else:
        url = baseUrl + soure

    return url


html = urlopen(host)
bsObj = BeautifulSoup(html, 'html.parser')
downLoadList = bsObj.findAll('img')

for img in downLoadList:
    try:
        title = img['alt'] + '.jpg'
    except Exception as e:
        print(e)
        title = img['src']

    loadUrl = getImageUrl(host, img['src'])
    print(title)
    print(loadUrl)
    # urlretrieve(loadUrl, title)
