# -*- coding: utf-8 -*-
from client import *
import common.db_data as  db

path = '/main/new'
url = URL.url + path

@ddt.ddt
class MainNew(unittest.TestCase):
    '''冒烟-40-新人有礼'''

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
        client.incloud('ok', client.json.get('message'))

    def testcase02(self):
        '''2.请求头未传token'''
        client = self.client
        client.set_header('token', token1)
        client.send()
        client.status_code_is_200()
        client.res_times_less_than(200)
        client.incloud('ok', client.json.get('message'))

    data = [{'page': 'h', 'limit': '1'},
            {'page': '@', 'limit': '1'},
            {'page': '1', 'limit': 'h'},
            {'page': '2', 'limit': '@'},
            {'page': '@', 'limit': '@'},
            ]  # 请求参数，即测试数据

    @ddt.data(data)
    def testcase03(self, *values):
        '''3.请求参数错误，验证接口返回的状态是否与预期一致'''
        client = self.client
        client.set_header('token', token)
        client.set_data({'page' : values.count('page'), 'limit' : values.count('limit')})
        client.send()
        client.status_code_is_200()
        client.res_times_less_than(200)
        client.equal(client.json.get('code'), 400)
