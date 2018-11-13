# -*- coding: utf-8 -*-
from client import *


path = '/main/more'
url = URL.url + path

@ddt.ddt  # 轮询
class Main_more(unittest.TestCase):
    '''冒烟-02-商城-查看更多'''

    def setUp(self):
        self.url = url
        self.client = Client(url=self.url, method=Method.GET, type=Type.URL_ENCODE)

    def tearDown(self):
        self.client.result()

    def testcase01(self):
        '''1.正向获取'''
        client = self.client
        client.set_header('token', token)   # 因为请求头还需要输入token
        client.send()
        client.status_code_is_200()
        client.res_times_less_than(200)
        client.equal(client.json.get('message'), 'ok')

    def testcase02(self):
        '''2.请求头未传token'''
        client = self.client
        client.set_header('token', token1)   # 因为请求头还需要输入token
        client.send()
        client.status_code_is_200()
        client.res_times_less_than(200)
        client.incloud('无效', client.json.get('message'))

    def testcase03(self):
        '''3.验证该用户账户重点消息未读数与数据库是否一致'''
        client = self.client
        client.set_header('token', token)   # 因为请求头还需要输入token
        client.send()
        client.status_code_is_200()
        client.res_times_less_than(200)
        client.db_equal(client.json.get('data')['num'], 'select count(*) from `tp_message` where `user_id` = 82')