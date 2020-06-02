#! /usr/bin/env python
# -*- coding:utf-8 -*-

'''anne practice request model'''
__author__='anne yang'

import  requests
def search_api_name(request):
    #自定义接口
    url = 'http://192.168.4.215:21802/vmen/order/buy'
    params = {
        "id": "458",
        "quantity": "1",
        "type": "1",
        "vmId": "240",
        "scenType": "3",
        "sdk": "ec80104d769fb83a0a7ee9e4bf65aad2",
        "app_from": "0",
        "app_version": "511000",
        "secret": "XWP3e24LgJSmTTTUQcKo",
        "uid": "4496",
        "lang": "1",
        "api": "1",
        "newWalletApiRequest": ""
    }
    r = requests.post(url,json=params)
    if r != '':
        event_turple = db_test.select_all('select * from vm_goods where user_id like '+ "'%" + r + "%'")
        event_list = []
        if len(event_turple) != 0:
            for i in event_turple:
                event_list.append({})
                return  r.json({'Stauts_code':'200'})
        else:
            return  r.json(())

