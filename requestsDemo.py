#! /usr/bin/env python
# -*- coding:utf-8 -*-

import requests

# 判断接口结果
class ApiResult(object):

    def get_api_result(apiName, params):
        base_url = 'http://192.168.4.215:23110'
        r = requests.post(base_url + apiName, json=params)
        if r.status_code == 200:
            print(r.text)
        else:
            print(r.status_code)

    # 查询营销区拼团列表
    def test_cases():
        apiName = '/groupBuy/getQuickSaleGroupBuyList'
        params = {
            "uid":"18057911",
            "lang":"1",
            "top_group_buy_id":"null",
            "limit":"30",
            "page":"1"
            }



if __name__ == '__main__':
    ApiResult.get_api_result()



