# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : anne yang

# 可变参数
def fun_a(*args, **kwargs):
    print("a={0}, b={1}".format(arg, kwargs))
    print(type(arg), type(kwargs))

if __name__ == '__main__':
    fun_a(10)
    fun_a(age=20)
    fun_a(10, 20, name="zhang san", age=15)
