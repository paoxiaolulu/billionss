# coding:utf-8
import requests
import unittest
import pymysql
import yaml
import ddt
from pymysql import cursors


class Client(unittest.TestCase):

    DATA = {}
    DB = None

    def __init__(self, url, method, type=0):  # 分离单独封装url，方法等
        self.url = url
        self.method = method
        self.type = type
        self.headers = {}
        self.data = {}
        self.res = None
        self.flag = 0
        self._type_equality_funcs = {}       # 检查点equal的引用
        self.db = pymysql.connect(host='47.100.182.135',
                             user='tpshop',
                             password='tpshop123456',
                             db='tpshop',
                             port=3306)

    @property
    def status_code(self):
        return self.res.status_code

    @property
    def text(self):
        return self.res.text

    @property
    def json(self):
        return self.res.json()

    @property
    def times(self):
        return int(round(self.res.elapsed.total_seconds() * 1000))

    def set_header(self, key, value):
        self.headers[key] = value

    def set_data(self, dic):
        self.set_data = dic

    def send(self):
        if self.method == 'get':
            self.res = requests.get(url=self.url, headers=self.headers, params=self.data)
        elif self.method == 'post':
            if self.type == 1:
                self.res = requests.post(url=self.url, headers=self.headers, data=self.data)
            elif self.type == 5:
                self.res = requests.post(url=self.url, headers=self.headers, files=self.data)
            elif self.type == 2:
                self.set_header('Content-Type', 'application/x-www-form-urlencoded')
                self.res = requests.post(url=self.url, headers=self.headers, data=self.data)
            elif self.type == 3:
                xml = self.data.get('xml')
                if xml:
                    self.res = requests.post(url=self.url, headers=self.headers, data=xml)
                else:
                    raise Exception('xml正文，入参格式：{"xml": "xxx"}')
            elif self.type == 4:
                self.set_header('Content-Type', 'application/json')
                self.res = requests.post(url=self.url, headers=self.headers, json=self.data)
            elif self.type == 0:
                self.res = requests.post(url=self.url, headers=self.headers)
            else:
                raise Exception('正文格式不支持')
        else:
            raise Exception('请求的方法类型不支持')

    def save(self, name, value):
        Client.DATA[name] = value   # 传值

    def value(self, name):
        return Client.DATA.get(name, None)    # 取值


    def result(self):
        self.db.close()
        if self.flag > 0:
            self.assertTrue(False, '断言出现错误')

    def equal(self, f, s):
        try:
            self.assertEqual(f, s)
            print('检查点成功：实际结果[{f}]，预期结果[{s}]'.format(f=f, s=s))
        except:
            print('检查点失败：实际结果[{f}], 预期结果[{s}]'.format(f=f, s=s))
            self.flag += 1

    def incloud(self, f, s):
        try:
            self.assertIn(f, s)
            print('检查点成功：预期结果包含关键字[{f}], 实际结果[{s}]'.format(f=f, s=s))
        except:
            print('检查点失败：预期结果包含关键字[{f}], 实际结果{{s}}'.format(f=f, s=s))
            self.flag += 1

    def status_code_is_200(self):
        self.equal(self.status_code, 200)

    def res_times_less_than(self, ms):
        self.less_than(self.times, ms)

    def less_than(self, f, s):
        try:
            self.assertLess(f, s)
            print('检查点成功：实际结果[{f}]，预期结果[<{s}]'.format(f=f, s=s))
        except:
            print('检查点失败：实际结果[{f}]，预期结果[<{s}]'.format(f=f, s=s))
            self.flag += 1

    def db_execute(self, sql):
        '''数据库封装'''
        cursor = Client.DB.cursor()
        cursor.execute(sql)
        Client.DB.commit()

    def db_equal(self, f, sql):
        cursor = self.db.cursor()
        result = cursor.execute(sql)
        # result = cursor.fetchone()[0]
        try:
            self.assertEqual(f, result)
            print('检查点成功：实际结果[{f}], 预期结果[{s}]'.format(f=f, s=result))
        except:
            print('检查点失败：实际结果[{f}], 预期结果[{s}]'.format(f=f, s=result))
            self.flag += 1

    def db_equals(self, f, sql):
        cursor = Client.DB.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        try:
            self.assertEqual(f, result)
            print('检查点成功：实际结果[{f}], 预期结果[{s}]'.format(f=f, s=result))
        except:
            print('检查点失败：实际结果[{f}], 预期结果[{s}]'.format(f=f, s=result))
            self.flag += 1

class Method:
    GET = 'get'
    POST = 'post'

class Type:
    FORM = 1
    URL_ENCODE = 2
    XML = 3
    JSON = 4
    FILE = 5

class URL:
    url = 'https://lanxiongdianshang.billionss.com/api/v6'   # ---线上

#======存放token=======
f = open('/Users/air/Documents/bill/common/token.yaml')
res = yaml.load(f)   #加载读出文件 将键值对转化为字典

token = '7ea3fb8bd27d54268481f4164c6f3dfa'
token1 = ''