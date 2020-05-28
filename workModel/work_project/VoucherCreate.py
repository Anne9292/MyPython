#! /usr/bin/env python
# -*- coding:utf-8 -*-

# from ConnectMysql import ConnectMysql
import yaml
import requests

"""卡券发放--先查可使用的券，再发放对应类型的券"""

file = open("./TestCase/SendVoucher.yaml", "rb")
api_list = yaml.full_load(file)
print(api_list)

def createVoucher(cardId,uid):
    url = api_list[0]['url']
    params = api_list[0]['params']
    api_list[0]['params']['cardId'] = cardId
    api_list[0]['params']['userId'] = uid
    api_list[0]['params']['trackId'] = time_str
    api_list[0]['params']['sig'] = new_md5str
    print('=============> 请求参数是：\n', params)
    r = requests.post(url,data=params)
    if r.status_code==200:
        print(r.text)
    else:
        print(r.status_code)



if __name__ == "__main__":
    createVoucher(1439,18057911)

