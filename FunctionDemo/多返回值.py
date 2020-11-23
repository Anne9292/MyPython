#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : anne yang

sum = 10
def add(val1, val2):
    global sum
    sum = val1 + val2
    print(locals())
    return val1, val2, sum

for key, value in dict(globals()).items():
    print(key, value)


if __name__ == '__main__':
    x, y, z = add(10, 20)
    print(x, y, z)
    print(locals())