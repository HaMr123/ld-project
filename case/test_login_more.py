import unittest
from api.api_login import ApiLogin
from parameterized import parameterized
from tools.read_json import ReadJson


#准备数据用来参数化,没有类的时候函数不需要加self
def get_data():

    datas = ReadJson("login_more.json").readjson()
    arrs = []
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("user"),
                     data.get("pswd"),
                     data.get("result"),
                     data.get("resultcode")
                     ))
    return arrs


class TestLogin(unittest.TestCase):
    @parameterized.expand(get_data())
    def test_login(self,url,user,pswd,result,resultcode):
        # url = "http://test.hyunst.com/ht/login_staffLogin.do"
        # user = "gcs"
        # pswd = "E10ADC3949BA59ABBE56E057F20F883E"
        s = ApiLogin().api_post_login(url,user,pswd)
        print(s.json())
        self.assertEqual(result,s.json()['Message'])
        self.assertEqual(resultcode,s.status_code)
if __name__ == '__main__':
    unittest.main()
