# -*- coding: utf-8 -*-
from client import *


path = '/goods/search'
url = URL.url + path

@ddt.ddt  # 轮询
class Goods_search(unittest.TestCase):
    '''冒烟-07-商品搜索'''

    def setUp(self):
        self.url = url
        self.client = Client(url=self.url, method=Method.POST, type=Type.URL_ENCODE)

    def tearDown(self):
        self.client.result()
    # data = {'page':'1',
    #         'limit':'10',
    #         'keyword':'手机'}
    #
    # @ddt.data(data)
    def testcase01(self):
        '''1.正向获取'''
        client = self.client
        client.set_header('token', token)   # 因为请求头还需要输入token
        client.set_data({'page':'1', 'limit':'10', 'keyword':'手机'})
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