import unittest

class MyTest01(unittest.TestCase):

    def setUp(self):
        print('setUp')

    def test_case01(self):
        print('test_case01')


    def test_case02(self):
        print('test_case02')

    def tearDown(self):
        print('testDown')


import client as c
import pymysql
import common.db_data as db_data
c.Client.db= pymysql.connect(db_data.db_config)
c.Client.db_execute(sql='select sex from tp_users where user_id=82;')






