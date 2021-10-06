#! /usr/bin/env python
# -*- coding:utf-8 -*-

import json


def cmp(src_f1, dst_f2):
    for src_value, dst_value in zip(sorted(src_f1), sorted(dst_f2)):
        if str(src_f1[src_value]) != str(dst_f2[dst_value]):
            print('src是——>{}:{}，\ndst是——>{}:{}'.format(src_value, src_f1[src_value], dst_value, dst_f2[dst_value]))


if __name__ == '__main__':
    # src_data = {"name":"anne","age":20,"source":["math","chinese"],"grade":1,"pets":{"dog":"tangshao","age":[1, 2]}}
    # dst_data = {"name":"anne","age":20,"source":["english","math","chinese"],"grade":1}
    src_data = "src_data.json"
    dst_data = "dst_data.json"
    with open(src_data) as f1:
        f1_dict = json.load(f1)
    with open(dst_data) as f2:
        f2_dict = json.load(f2)
    cmp(f1_dict, f2_dict)
