#! /usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql

class ConnectSql(object):
    # 连接数据库
    def __init__(self):
        try:
            # 打开数据库连接
            db_info = \
                {
                    "host": "192.168.4.215",
                    "port": 21406,
                    "database": "blue_pay_plus_indo",
                    "user": "bp_dev",
                    "password": "bp_dev"
                }

            self.connect = pymysql.connect(**db_info)
            # 使用cursor()方法创建一个游标对象cursor
            self.cursor = self.connect.cursor()
        except:
            print("Ops, 数据库连接失败！！！")

    # 关闭数据库
    def close(self):
        self.connect.close()  # 关闭连接对象
        self.cursor.close()  # 关闭指针对象

    #  执行sql
    def execute(self, querySql):
        # 使用execute()执行查询事务
        self.cursor.execute(querySql)
        # 使用fetchone()获取单条数据
        queryResult = self.cursor.fetchone()
        self.close()
        return queryResult

    def queryUser(self, msisdn):
        sql = "select user_id, secret from user_info where msisdn='{}'".format(msisdn)
        queryResult = self.execute(sql)
        return queryResult


if __name__ == '__main__':
    result = ConnectSql().queryUser('6281700001930')
    print(result)