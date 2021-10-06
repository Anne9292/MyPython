#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""a test module"""
__author__ = 'anne yang'

import requests


# group models
class ApiResult(object):

    def get_api_result(apiName, params):
        base_url = 'http://192.168.4.215:23110'
        r = requests.post(base_url + apiName, json=params)
        if r.status_code == 200:
            print(r.text)
        else:
            print(r.status_code)

    # 查询营销区拼团列表
    def test_cases(self):
        apiName = '/groupBuy/getQuickSaleGroupBuyList'
        params = {
            "uid": "18057911",
            "lang": "1",
            "top_group_buy_id": "null",
            "limit": "30",
            "page": "1"
        }

    # 查询普通区拼团列表
    def get_common_group_list(self):
        pass


if __name__ == '__main__':
    ApiResult.get_api_result()
