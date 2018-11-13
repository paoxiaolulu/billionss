# -*- coding: utf-8 -*-
from client import *

path = '/main/rank'
url = URL.url + path

@ddt.ddt
class MainRank(unittest.TestCase):
    '''冒烟-41-首页商品排行榜列表'''

    def setUp(self):
        self.url = url
        self.client = Client(url=self.url, method=Method.GET, type=Type.URL_ENCODE)

    def tearDown(self):
        self.client.result()

    def testcase01(self):
        '''1.正向获取，type为1的接口返回'''
        client = self.client
        client.set_header('token', token)   # 因为请求头还需要输入token
        client.set_data({"category_id":"0","type":"1","page":"1","limit":"6"})
        client.send()
        client.status_code_is_200()
        client.res_times_less_than(200)
        # client.incloud('ok', client.json.get('message'))
        client.equal(client.json.get('message'), 'ok')

    def testcase02(self):
        '''2.正向获取，type为2的接口返回'''
        client = self.client
        client.set_header('token', token)   # 因为请求头还需要输入token
        client.set_data({"type":"2","category_id":"0","page":"1","limit":"6"})
        client.send()
        client.status_code_is_200()
        client.res_times_less_than(200)
        client.incloud('ok', client.json.get('message'))

    def testcase03(self):
        '''4.正向获取，type为3的接口返回'''
        client = self.client
        client.set_header('token', token)   # 因为请求头还需要输入token
        client.set_data({'type': '3', 'category_id': '0', 'page': '1', 'limit': '6'})
        client.send()
        client.status_code_is_200()
        client.res_times_less_than(200)
        # client.incloud('ok', client.json.get('message'))
        client.equal(client.json.get('message'), 'ok')

    def testcase04(self):
        '''4.请求头未传token'''
        client = self.client
        client.set_header('token', token1)
        client.send()
        client.status_code_is_200()
        client.res_times_less_than(200)
        client.incloud('未传', client.json.get('message'))

    data = [{'category_id': 'h', 'type': '1', 'page': '1', 'limit': '1'},
            {'category_id': '', 'type': '@', 'page': '1', 'limit': '1'},
            {'category_id': '1', 'type': '3', 'page': '@', 'limit': '1'},
            {'category_id': '1', 'type': '1', 'page': '1', 'limit': '@'},
            {'category_id': '0', 'type': '4', 'page': '1', 'limit': '1'},
            {'category_id': 'h', 'type': 'g', 'page': 'h', 'limit': 'j'},
            {'category_id': '', 'type': '', 'page': '', 'limit': ''}
            ]  # 请求参数，即测试数据

    @ddt.data(data)
    def testcase05(self, *values):
        '''5.请求参数错误，验证接口返回的状态是否与预期一直'''
        client = self.client
        client.set_header('token', token)
        client.set_data({'category_id' : values.count('category_id'),
                         'limit' : values.count('limit'),
                         'page' : values.count('page'),
                         'type' : values.count('type')})
        client.send()
        client.status_code_is_200()
        client.res_times_less_than(200)
        client.equal(client.json.get('code'), 400)
