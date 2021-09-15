import pymysql

class ReadDB:
    #conn设置为类的属性，这样至始至终都以一个连接对象为主
    conn = None
    #获取连接对象
    def get_conn(self):
        if self.conn is None:
            self.conn = pymysql.connect(host="47.110.33.149",  # 数据库ip地址
                                        user="hysj",  # 用户名
                                        password="123456",  # 密码
                                        database="hy",  # 数据库名称
                                        charset="utf8")  # 通信采用的编码方式
        return self.conn

    #获取游标对象
    def get_cursor(self):
        return self.get_conn().cursor()

    #关闭游标对象
    def close_cursor(self,cursor):
        if cursor:
            cursor.close()

    #关闭连接对象
    def close_conn(self):
        if self.conn:
            self.conn.close()
        # 关闭连接对象后，对象还存在内存中，需要手动设置为None
        self.conn = None

     #主要执行方法，在外界调用该方法就可以完成数据相应操作
    #获取一条结果
    def get_sql_one(self,sql):
        curs = None
        data = None
        try:
            # 把获取的游标对象赋值给curs
            curs = self.get_cursor()
            # 执行sql语句
            curs.execute(sql)
            # 获取结果赋值给data
            data = curs.fetchone()
        except Exception as e:
            print("get_sql_one错误日志：",e)
        finally:
            # 关闭游标对象
            self.close_cursor(curs)
            # 关闭连接对象
            self.close_conn()
            # 返回结果
            return data

   #获取所有结果集
    def get_sql_all(self):
        curs = None
        data = None
        try:
            # 把获取的游标对象赋值给curs
            curs = self.get_cursor()
            # 执行sql语句
            curs.execute(sql)
            # 获取结果赋值给data
            data = curs.fetchall()
        except Exception as e:
            print("get_sql_one错误日志：", e)
        finally:
            # 关闭游标对象
            self.close_cursor(curs)
            # 关闭连接对象
            self.close_conn()
            # 返回结果
            return data
   #更新、修改数据
    def updata_sql(self):
        curs = None
        try:
            # 把获取的游标对象赋值给curs
            curs = self.get_cursor()
            # 执行sql语句
            curs.execute(sql)
            #提交事务
            self.conn.commit()

        except Exception as e:
            # 事务回滚
            self.conn.rollback()
        finally:
            # 关闭游标对象
            self.close_cursor(curs)
            # 关闭连接对象
            self.close_conn()







