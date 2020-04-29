#! /usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql

class ConnectSql(object):
    # 连接数据库
    def __init__(self):
        try:
            # 打开bluepayplus数据库
            db_info = \
                {
                    "ip": "192.168.4.215",
                    "port": 21406,
                    "database": "voucherdb",
                    "username": "bp_dev",
                    "password": "bp_dev"
                }
            self.connect = pymysql.connect(host=db_info['ip'],
                                            port=db_info['port'],
                                            user=db_info['username'],
                                            password=db_info['password'],
                                            database=db_info['database'])

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
        queryResult = self.cursor.fetchall()
        self.close()
        return queryResult

    def queryUser(self, msisdn):
        sql = "select user_id, secret from user_info where msisdn='{}'".format(msisdn)
        queryResult = self.execute(sql)
        return queryResult

    def queryVoucher(self):
        sql = "select card_id,reward_type,mode_effect,lower_limit,rule_name from reward_info where \
        status=1 and reward_type in (4,11) order by create_time desc limit 10"
        queryResult = self.execute(sql)
        return queryResult


if __name__ == '__main__':
    # result = ConnectSql().queryUser('6281700001930')
    result1 = ConnectSql().queryVoucher()
    print(result1)