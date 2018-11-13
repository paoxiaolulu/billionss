# -*- coding: utf-8 -*-
from client import *

path = '/message/GetNewNum'
url = URL.url + path

@ddt.ddt
class GetNewNum(unittest.TestCase):
    '''冒烟-01-消息数量'''

    def setUp(self):
        self.url = url
        self.client = Client(url=self.url, method=Method.POST, type=Type.URL_ENCODE)

    def tearDown(self):
        self.client.result()

    def testcase01(self):
        '''1.正向获取'''
        client = self.client
        client.set_header('token', token)   # 因为请求头还需要输入token
        client.send()
        client.status_code_is_200()
        client.res_times_less_than(200)
        client.incloud('ok', client.json.get('message'))

    def testcase02(self):
        '''2.请求头未传token'''
        client = self.client
        client.set_header('token', token1)   # 因为请求头还需要输入token
        client.send()
        client.status_code_is_200()
        client.res_times_less_than(200)
        client.incloud('无效', client.json.get('message'))

    def testcase03(self):
        '''3.根据用户信息验证返回的消息数与数据库是否一致'''
        client = self.client
        client.set_header('token', token)
        client.send()
        # client.equal(client.json.get('data')['num'], db.results[0])    # 接口返回的数据与数据库的值进行对比
        # print(client.json.get('data')['num'])
        client.db_equal(client.json.get('data')['num'], 'select count(*) from `tp_message` where `user_id` = 82')   # 要保证测试的token和user_id匹配