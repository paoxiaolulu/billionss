# -*- coding: utf-8 -*-
from client import *


path = '/message/_list'
url = URL.url + path

@ddt.ddt  # 轮询
class Message_list(unittest.TestCase):
    '''冒烟-02-消息列表'''

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