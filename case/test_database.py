# 导包 先执行命令安装：pip3 install PyMySQL
import pymysql


# 获取连接对象
conn = pymysql.connect(host="47.110.33.149",#数据库ip地址
                       user="hysj",#用户名
                       password="123456",#密码
                       database="hy",#数据库名称
                       charset="utf8")#通信采用的编码方式
#通过连接获取游标对象，conn.cursor()返回Cursor对象，用于执行sql语句并获得结果
cursor = conn.cursor()
#执行方法sql
sql = "select name from u_user where tel= 18705008120"
cursor.execute(sql)
#获取结果并进行断言
result = cursor.fetchone()
#print(result)
assert "奈小麦" == result[0]
#关闭游标对象
cursor.close()
#关闭连接对象
conn.close()






