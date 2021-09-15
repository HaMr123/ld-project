import unittest
from api.api_login import ApiLogin
from parameterized import parameterized
from tools.read_json import ReadJson
from api.api_goods import ApiGoods
from tools.md5 import Md5Demo


#准备数据用来参数化，没有类的时候函数不需要加self
def get_data():

    data = ReadJson("goods.json").readjson()
    arrs = []
    arrs.append((data.get("url"),
                 data.get("user"),
                 data.get("pswd"),
                 data.get("url2"),
                 data.get("brandid"),
                 data.get("result"),
                 data.get("resultcode")
                 ))
    return arrs


class TestLogin(unittest.TestCase):

    # 获取参数用来传给test_login()方法
    @parameterized.expand(get_data())
    def test_goods(self,url,user,pswd,url2,brandid,result,resultcode):

        #调用api封装函数
        s = ApiGoods().api_post_goods(url,user,pswd,url2,brandid)
        print(s.json())
        #断言结果
        self.assertEqual(result,s.json()['Message'])
        self.assertEqual(resultcode,s.status_code)
if __name__ == '__main__':
    unittest.main()
