#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-11-23 21:53
# filename: PyCharm-dict_get


# 获取嵌套字典中的key: 字典相互嵌套
# def dict_get(dict1, objkey, default=None):
#     for k, v in dict1.items():
#         if k == objkey:
#             return v
#         else:
#             if type(v) is dict:
#                 ret = dict_get(v, objkey, default)
#                 if ret is not default:
#                     return ret
#     return default

"""
获取嵌套列表字典中的key: 字典/列表/元组相互嵌套
dic: 字典
key: 目标key
"""
def getdictvalue(dic, key):
    result = []
    if isinstance(dic, dict):
        try:
            value = dic[key]
            result.append(value)
        except Exception as e:
            pass
        for valuedd in dic.values():
            if isinstance(valuedd, dict):
                yied_result = getdictvalue(valuedd, key)
                if len(yied_result) != 0:
                    result.append(getdictvalue(valuedd, key))
            elif isinstance(valuedd, (list, tuple)):
                for item in dic:
                    valueitem = getdictvalue(valuedd, key)
                    if valueitem != "None" and valueitem is not None and len(valueitem) != 0:
                        if valueitem not in result:
                            result.append(valueitem)

    elif isinstance(dic, (list, tuple)):
        for item in dic:
            value = getdictvalue(item, key)
            if value != "None" and value is not None and len(value) != 0:
                if value not in result:
                    result.append(value)
    return result

class listchangetype(object):
  """对于查找后的list的数据的清洗"""
  def __init__(self):
    self.arg = []
  def make(self,listone):
    for i in listone:
      if isinstance(i,(type,list)):
        for l in i:
          self.make(i)
      else:
        if i not in self.arg:
          self.arg.append(i)
    return self.arg

if __name__ == '__main__':
    dicttest = {'data': {'list1': [{'test1': (1, 2, 3)}, {'test2': '2'}, {'test3': '3'}],
                          'list2': [{'test1': '11'}, {'test2': '22'}, {'test3': '33'}],
                          'list3': [{'test1': '12'}, {'test2': '23'}, {'test3': '34'}]
                          }
                 }
    res = getdictvalue(dicttest, 'test1')
    a = listchangetype()
    print(a.make(res))
    # ret = dict_get(dicttest, 'test1')
    # print(ret)
