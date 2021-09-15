import requests
import json
from api.api_login import ApiLogin
from tools.md5 import Md5Demo


class ApiGoods(object):

    def api_post_goods(self,url,user,pswd,url2,brandid):
        s = ApiLogin().api_post_login(url, user, pswd)
        data = s.json()
        #调试信息
        #print(data)
        uid = data.get("Uid")
        #print(uid)
        token = data.get("Token")
        #print(token)
        item = data.get("Result")
        #登录接口返回的id作为后续接口的operateId
        opid = item.get("id")
        #print(opid)
        comid = item.get("companyId")
        #print(comid)
        name = item.get("username")
        #print(name)
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        #登录账号是公司账号时，要查询那个品牌传对应品牌的brandid，若是登录账号是品牌账号只能传该登录品牌对应的brandid
        param = {"brandId":brandid,"operateId":opid,"operateName":name,"COMPANY_ID":comid}
        timestamp = "1617002172290"
        clientid = "100122"
        sign = Md5Demo().md5_method(param,timestamp,clientid,uid)
        body = {"Api": "getAllGoodsTypeList",
                "Params": str(param),
                "ClientId": "100122",
                "Timestamp": "1617002172290",
                "OperateId": opid,
                "Token": token,
                "Sign": sign

        }
        return requests.post(url2,headers = headers,data=body)


if __name__ == '__main__':
    url = "http://test.hyunst.com/ht/login_staffLogin.do"
    user = "gcs"
    pswd = "E10ADC3949BA59ABBE56E057F20F883E"
    url2 = "http://test.hyunst.com/ht/goods_callApi.do"
    brandid = "200318182A8862218E"
    s = ApiGoods().api_post_goods(url,user,pswd,url2,brandid)
    print(s.json())




