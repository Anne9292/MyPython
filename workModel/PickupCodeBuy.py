#! /usr/bin/env python
# -*- coding:utf-8 -*-

import json
import requests
import yaml
from ConnectSql import ConnectSql # 从模块里导入类

"""取货码购买流程"""
class PickupCode(object):

    def __init__(self, uid, secret):
        self.uid = uid
        self.secret = secret

        # 导入yaml文件
        file = open('./TestCase/pickupCode.yaml', 'rb')
        api_list = yaml.full_load(file)   #list类型

        # 统一替换secret和uid
        api_list_json = json.dumps(api_list)  #列表转换成json字符串类型
        api_list_json = api_list_json.replace('{secret}', self.secret).replace("{uid}", str(self.uid))  # 链式replace替换
        self.api_list = json.loads(api_list_json)  #字符串转换成字典

    # 购买取货码
    def code_buy(self):
        url = self.api_list[0]['url']
        params = self.api_list[0]['params']
        print('=============> 取货码购买请求参数是：\n', json.dumps(params, indent=4))  #将python字典转换成json对象,indent指缩进4个字符
        r = requests.post(url, json=params)
        if r.status_code==200:
            print('============> 取货码购买接口响应是：\n')
            print(r.text)
        else:
            return r.json()['data']['order_id']   # r.json()将json对象转换成字典

    # 确认订单
    def code_confirmpay(self, order_id):
        url = self.api_list[1]['url']
        params = self.api_list[1]['params']
        params['id'] = order_id
        print('=============> 订单确认请求参数是：\n', json.dumps(params, indent=4))
        r = requests.post(url, json=params)
        print('============> 订单确认接口响应是：\n', r.json())
        return r.json()['data']['product_id']

    # 创建订单
    def code_newTrade(self, product_id):
        url = self.api_list[2]['url']
        params = self.api_list[2]['params']
        params['product_id'] = product_id
        print('============> 创建订单请求参数是：\n', json.dumps(params, indent=4))
        r = requests.post(url, json=params)
        if r.status_code==200:
            print('============> 创建订单接口响应是：\n', r.json())
            return r.json()['shopping_id']
        else:
            return r.status_code

    # 支付
    def code_pay(self, shopping_id):
        url = self.api_list[3]['url']
        params = self.api_list[3]['params']
        params['shopping_id'] = shopping_id
        print('============> 订单支付请求参数是：\n', json.dumps(params, indent=4))
        r = requests.post(url, json=params)
        if r.status_code==200:
            print('============> 订单支付接口响应是：\n', r.json())
        else:
            return r.status_code

    # 获得取货码
    def code_getpickup(self):
        url = self.api_list[4]['url']
        params = self.api_list[4]['params']
        print('============> 取货码查询请求参数是：\n', json.dumps(params, indent=4))
        r = requests.post(url, json=params)
        print('============> 取货码查询接口响应是：\n', r.json())
        return  r.json()['data'][0]['pickUpCode']

def main():
    user_info = ConnectSql().queryUser('6281700001930')
    pickupCode = PickupCode(user_info[0], user_info[1])
    order_id = pickupCode.code_buy()
    product_id = pickupCode.code_confirmpay(order_id)
    shopping_id = pickupCode.code_newTrade(product_id)
    pickupCode.code_pay(shopping_id)
    pickupCode.code_getpickup()

if __name__ == '__main__':
    main()