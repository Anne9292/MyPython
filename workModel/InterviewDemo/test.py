#! /usr/bin/env python
# -*- coding:utf-8 -*-

'''
    anne practice request model
'''
__author__ = 'anne yang'

from functools import reduce

# 方法1
print(sum(range(1, 101)))

# 方法2
print(reduce(lambda a, b: a+b, range(1, 101)))

# 方法3

sum = 0
for i in range(1, 101):
    sum += i
    i += 1
print(sum)