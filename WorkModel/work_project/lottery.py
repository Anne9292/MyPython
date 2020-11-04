# !/usr/bin/env python
# -*- coding:utf-8 -*-

import yaml
import requests
import time
from collections import Counter
from ConnectSql import ConnectSql

file = open("../TestCase/groupLottery.yaml", "rb")
api_list = yaml.full_load(file)


def check_chance(uid):

    url = api_list[0]['url']
    params = api_list[0]['params']
    params['uid'] = uid
    print("================> 抽奖次数查询请求参数是：", params)
    r = requests.post(url, json=params)
    if r.status_code == 200:
        print("================> 查询结果为：", r.json())
        return r.json()['data']['num']
    else:
        print("================> 接口返回错误码：", r.status_code)


def lottery(uid):

    url = api_list[1]['url']
    params = api_list[1]['params']
    params['uid'] = uid
    # print("================> 抽奖请求参数是：", params)
    r = requests.post(url, json=params)
    if r.status_code == 200:
        print("================> 当前抽奖结果为：", r.json()['data']['reward_name'], r.json()['data']['remark'])
        return r.json()['data']['reward_name'], r.json()['data']['remark']
    else:
        print("================> 接口返回错误码：", r.status_code)


# 统计抽奖结果
def lottery_result(num):

    remark_list = []
    remark_dict = {}
    if num == 0:
        print("================> 没有抽奖次数了！！！")
    else:
        for i in range(num):
            print("第%d次抽奖" % (i+1))
            reward_name, remark = lottery(uid)
            remark_list.append('{}&&{}'.format(reward_name, remark))
            time.sleep(1)
        # 统计抽奖结果
        lottery_dict = dict(Counter(remark_list).most_common())   # 返回前topN列表，N未指定，返回全部
        print("================> %d次抽奖整体结果为：" % num, lottery_dict)

        for key, value in lottery_dict.items():  # 返回可遍历的(键, 值) 元组数组
            total = len(remark_list)   # 列表长度
            remark_dict.update({key: ('%.3f' % (value/total*100) + '%')})    # update()更新字典
        print("================> %d次抽奖整体概率为：" % num, remark_dict)


if __name__ == "__main__":
    uid = ConnectSql().queryUser('6281700001930')[0]
    num = check_chance(uid)
    lottery_result(num)

