# -*- coding: utf-8 -*-
from client import *


path = '/main/newHome'
url = URL.url + path

@ddt.ddt  # 轮询
class Main_index(unittest.TestCase):
    '''冒烟-02-新首页-v6'''

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
        client.equal(client.json.get('code'), 200)
        client.save('find_id', client.json.get('data.find')['find_id'])   # 动态获取find_id
        # client.save('goods_id', client.json.get('data')['goods_id'])

    def testcase02(self):
        '''2.请求头未传token'''
        client = self.client
        client.set_header('token', token1)
        client.send()
        client.status_code_is_200()
        client.res_times_less_than(200)
        client.equal(client.json.get('code'), 200)    #一级首页不需要token

    def testcase03(self):
        '''3.该用户的商品'''
        client = self.client
        client.set_header('token', token1)   # 因为请求头还需要输入token
        client.send()
        client.status_code_is_200()
        client.res_times_less_than(200)
        client.equal(client.json.get('code'), 200)    #一级首页不需要token