# -*- coding:utf-8 -*-

import random

list1 = [1,2,3,4,5]
def fn(x):
    assert(x>0)
    return x**2

res = map(fn,list1)
res = [i for i in res if i > 10]
print(res)

def random_test():
    random.randint(5,10)  # 随机整数
    random.random(0,1)  # 随机数0-1
    random.uniform(1)  # 随机小数
