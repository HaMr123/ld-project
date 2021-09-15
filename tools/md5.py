# 在python3中使用hashlib模块进行md5操作
import hashlib

class Md5Demo(object):
    def md5_method(self,param,timestamp,clientid,uid):
        # 待加密信息
        strdata = str(param) + timestamp + clientid + uid
        #调试信息
        #print(strdata)
        # 创建md5对象
        hl = hashlib.md5()
        # 此处必须声明encode,若写法为hl.update(strdata) 报错为： Unicode-objects must be encoded before hashing
        # 因为python3里默认的字符编码是unicode,
        hl.update(strdata.encode(encoding='utf-8'))
        str_md5 = hl.hexdigest()
        return str_md5

if __name__ == '__main__':
    param = {
        "url":"http://test.hyunst.com/ht/login_staffLogin.do",
        "user":"gcs",
        "pswd":"E10ADC3949BA59ABBE56E057F20F883E",
        "result": "成功",
        "resultcode": 200
    }
    clientid = "100122"
    timestamp = "1617002172290"
    uid = "1234546544"

    d = Md5Demo().md5_method(param,timestamp,clientid,uid)
    print(d)