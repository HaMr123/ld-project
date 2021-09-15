import unittest
from tools.read_db import ReadDB

class TestDB(unittest.TestCase):
    def test_db(self):
        sql = "select name from u_user where tel= 18705008120"
        data = ReadDB().get_sql_one(sql)
        self.assertEqual("奈小麦",data[0])

if __name__ == '__main__':
    unittest.main()