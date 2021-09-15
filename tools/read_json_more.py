"""
1、为了方便调用，把文件名作为动态入参，下载不同文件存储的数据
2、数据是字典形式，把字典形式转换为列表形式，以便被@parameterized.expand（参数）使用
3、数据有多条的情况下，可以利用字典中values()读取所有值
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
    #ReadJson("login.json").readjson()



#多条测试数据的时候利用字典中values()遍历所有值,生成[(),()]这种xian
    datas = ReadJson("login_more.json").readjson()
    arrs = []
    #语法：dict.values(),字典 values()方法返回一个迭代器，可以使用 list() 来转换为列表，列表为字典中的所有值。
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("user"),
                     data.get("pswd"),
                     data.get("result"),
                     data.get("resultcode")
                     ))

    print(arrs)


