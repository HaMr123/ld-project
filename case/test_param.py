# parameterized模块介绍:使用parameterized进行参数化
# 在unittest中没有可以直接进行参数化的方式，必须要借助一些第三方的库进行相关的参数化执行。
#它的使用方式很简单，在unittest的TestCase的某个测试方法中直接用

import unittest
from parameterized import parameterized  # 引入parameterized模块


class T(unittest.TestCase):
    # @parameterized.expand（参数）括号中参数必须是列表形式；
    #如[值1，值2]或者[(参1值，参2值),(参1值，参2值)]
    @parameterized.expand([(1,2,3), (4,7,11), (7,9,16)])
    def test_1(self, a, b, c):
        print("a=",a)
        print("b=",b)
        print("c=",c)

if __name__ == '__main__':
    unittest.main()
