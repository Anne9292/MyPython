# -*- coding:utf-8 -*-

import random
from functools import reduce

list1 = [1,2,3,4,5]
def fn(x):
    assert(x>0)
    return x**2

def fn1(x):
    return x % 2 == 0


if __name__ == '__main__':
    res = map(fn,list1)
    print(type(res))
    res = [i for i in res if i > 10]
    print(res)

    res1 = filter(fn1, list1)
    print(type(res1))
    print(list(res1))

    res2 = reduce(lambda x, y: x + y, list1)
    print(type(res2))
    print(res2)



# def random_test():
#     random.randint(5,10)  # 随机整数
#     random.random(0,1)  # 随机数0-1
#     random.uniform(1)  # 随机小数