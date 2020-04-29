# -*- coding:utf-8 -*-
# GroupBuy.py

import requests
def get_group_buy_list():
    url = 'http://192.168.4.215:23110/groupBuy/getGroupBuyList'
    params = {
    "uid":"18057911",
    "lang":"1",
    "pickup_address_id":1,
    "is_recommend":1,
    "group_buy_id":5413,
    "top_group_buy_id":'',
    "limit":10,
    "page":1
    }
    r = requests.post(url, json=params)
    if r.status_code == 200:
        print(r.json())
    else :
        print(r.status_code)

if __name__ == "__main__":
    get_group_buy_list()