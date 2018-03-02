import json
from urllib.request import urlopen

'''
json 是 python 默认的标准库
使用该库可以直接将 json 字符串解析转换成字典，json 数组转换成列表 
'''
def getZhiHuNews():
    response = urlopen("http://news-at.zhihu.com/api/4/news/latest").read().decode('utf-8')
    print(response)
    responseJson = json.loads(response)
    return responseJson


print(getZhiHuNews().get("stories")[0])
