#! /usr/bin/env python
# -*- coding:utf-8 -*-

'''
	anne practice binary search
'''
__author__ = 'anne yang'

from functools import reduce

# 方法1
print(sum(range(1, 101)))

# 方法2
print(reduce(lambda a, b: a + b, range(1, 101)))

# 方法3
sum = 0
for i in range(1, 101):
    sum += i
    i += 1
print(sum)


# 二分查找法
def binary_search(v, a):
    first = 0
    last = len(a) - 1
    while first <= last:
        mid = (first + last) // 2
        if a[mid] < v:
            first = mid + 1
        elif a[mid] > v:
            last = mid - 1
        else:
            return mid + 1
    return n + 1


res = binary_search(2, [1, 2, 2, 4, 6])
print(res)
