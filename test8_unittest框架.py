"""
响应对象.json()跟响应对象.text的区别
"""

import requests
import json
import unittest


class login(unittest.TestCase):
    def setUp(self):
        self.url = "http://test.hyunst.com/pos/login_cashierLogin.do"

    def test_login_1(self):
        body = {'Api': 'doLogin',
                'Params': '{"username":"dd","password":"E10ADC3949BA59ABBE56E057F20F883E"}',
                'ClientId': 100123,
                'Timestamp': 1615971042933
                }

        r = requests.post(self.url, data=body)
        r_json = r.json()
        print("r_json1:", r_json)

        try:
            self.assertEqual("成功", r_json['Message'])

        except AssertionError as e:
            print(e)

    def test_login_2(self):
        body = {'Api': 'doLogin',
                'Params': '{"username":"dd","password":"E10ADC3949BA59ABBE56E057F20F88E"}',
                'ClientId': 100123,
                'Timestamp': 1615971042933
                }

        r = requests.post(self.url, data=body)
        r_json = r.json()
        print("r_json2:", r_json)

        try:
            self.assertEqual("密码", r_json['Message'])

        except AssertionError as e:
            print(e)

    def test_login_3(self):
        body = {'Api': 'doLogin',
                'Params': '{"username":"d2222","password":"E10ADC3949BA59ABBE56E057F20F883E"}',
                'ClientId': 100123,
                'Timestamp': 1615971042933
                }

        r = requests.post(self.url, data=body)
        r_json = r.json()
        print("r_json3:", r_json)

        try:
            self.assertEqual("用户名", r_json['Message'])

        except AssertionError as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
