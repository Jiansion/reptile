from urllib.request import urlopen

response = urlopen('http://pythonscraping.com/pages/page1.html')
html = response.read()
# 打印该网页的劝募 HTML 代码
print(html)
