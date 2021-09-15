#导包 unittest HTMLTestRunner time
import unittest
from tools.HTMLTestRunner import HTMLTestRunner
import time

if __name__ == '__main__':
    # 第一步：组装测试套件
    suite = unittest.defaultTestLoader.discover("../case", pattern="test_*.py")

    # 第二步：指定报告存放路径及文件名称
    now = time.strftime("%Y_%m_%d %H_%M_%S")
    # {}.format 格式化字符串的函数，{}为占位符，把format的内容传给{}
    filename = "../report/{}.html".format(now)

    # 第三步：运行测试套件并生成测试报告
    with open(filename, 'wb') as f:
        HTMLTestRunner(stream=f,
                       title='测试报告',
                       description='用例执行情况：').run(suite)
