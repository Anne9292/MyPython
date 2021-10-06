#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-11-23 21:53
# filename: PyCharm-dict_get

import time
import logging

"""
获取嵌套列表字典中的key: 字典/列表/元组相互嵌套
迭代当前dict的所有元素, 对元素挨个依次比较key与所需要的key, 如果相同就保存在输出的list中.
然后如果遇到value是属于又一个dict, 则进行递归, 再次对这个子dict进行相同操作. 最后循环结束后输出list
in_json: 字典
key: 目标key
"""

def get_dict_value_by_key(in_json, target_key, results=None):

    if results is None:
        results = []
    if isinstance(in_json, dict):  # 如果输入数据的格式为dict
        for key in in_json.keys():  # 循环获取key
            data = in_json[key]
            get_dict_value_by_key(data, target_key, results=results)  # 递归当前key对应的value
            if key == target_key:
                results.append(data)  # 如果当前key与目标key相同就将当前key的value添加到输出列表
    elif isinstance(in_json, (list, tuple)):  # 如果输入数据格式为list或者tuple
        for data in in_json:  # 循环当前列表
            get_dict_value_by_key(data, target_key, results=results)  # 回归列表的当前的元素
    return results

# 搞不赢
# def json_get(data, target_key):
#     map = {}
#     for key in data.keys():
#         value = data[key]
#         key = value[target_key]
#         map[key] = value
#     return map

# 对查找后的list数据进行清洗
# def make(listone, arg=None):
#     if arg is None:
#         arg = []
#     for i in listone:
#         if isinstance(i, (type, list)):
#             for _ in i:
#                 make(i, arg=arg)
#         else:
#             if i not in arg:
#                 arg.append(i)
#     return arg


if __name__ == '__main__':
    dict_test = {'data': {'list1': [{'test1': (1, 2, 3)}, {'test2': '2'}, {'test3': '3'}],
                          'list2': [{'test1': {'price_range': [10.2, 12.4]}}, {'test2': '22'}, {'test3': '33'}],
                          'list3': [{'test1': 1}, {'test2': '23'}, {'test3': '34'}]
                          }
                 }
    dict_test1 = {"info": "2班成绩单",
                  "grades": {"小明": [{"chinese": 60}, {"math": 80}, {"english": 100}],
                             "小红": [{"chinese": 90}, {"math": 70}, {"english": 50}],
                             "小蓝": [{"chinese": 80}, {"math": 80}, {"english": 80}],
                             },
                  "newGrades": {
                      "info": "新增数据",
                      "newChinese": 77
                                }
                  }
    res = get_dict_value_by_key(dict_test1, "info", [1, 2])
    print(res)
