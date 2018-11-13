#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# 数据准备调用mysql


import pymysql

# 打开数据库连接
db = pymysql.connect(host='47.100.182.135',
                     user='tpshop',
                     password='tpshop123456',
                     db='tpshop',
                     port=3306)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql_message = 'select count(*) from `tp_message` where `user_id` = 82 and `is_read`=0'     # 查询用户的短消息条数
# category_id = 'select is_lock from tp_users where user_id = 82'
try:
    # 执行SQL语句
    print(cursor.execute(sql_message))
    # 获取所有记录列表
    # print(cursor.fetchall())
    # print(results)
except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()
