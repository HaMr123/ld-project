"""
1、为了方便调用，把文件名作为动态入参，下载不同文件存储的数据
2、数据是字典形式，把字典形式转换为列表形式，以便被@parameterized.expand（参数）使用

"""

import json

class ReadJson(object):
    #数据存放文件不一样，为了方便调用所以把数据文件名作为传参
    def __init__(self,filename):
        self.path = "../data/"+ filename

#用with open()打开文件后,用json.load()下载文件流
    def readjson(self):
        with open(self.path,"r",encoding="utf-8") as f:
            data = json.load(f)
            return data

if __name__ == "__main__":
    ReadJson("login.json").readjson()

''' 
登录数据调试
    data = ReadJson("login.json").readjson()
    arrs = [] #新建空列表    
    arrs.append((data.get("url"),
                 data.get("user"),
                 data.get("pswd"),
                 data.get("result"),
                 data.get("resultcode")
                 ))
    #用data["键名"]或data.get("键名")获取对应值都可以，两者的区别就是用data.get("键名")键名输入错误可以继续运行下去，data["键名"]键名错误不会继续运行
    # arrs.append((data["url"],
    #              data["user"],
    #              data["pswd"],
    #              data["result"],
    #              data["resultcode"]
    #              ))
  
    print(arrs)
'''

