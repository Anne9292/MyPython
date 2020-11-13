#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-11-11 15:42
# filename: MyPython-闭包

import time


"""
方式二：通过装饰器-语法糖实现
"""
def log_time(func):
    def f(x, y, z):
        before = time.time()
        res = func(x, y)
        time.sleep(2)
        after = time.time()
        print('函数执行时间：%ds' % (after - before))
        return res(z)
    return f

# 闭包，func_1()是外围函数， func_2()是内嵌函数
@log_time
def func_1(a, b):
    sum = a + b
    def func_11(c):
        result = sum * c
        print('func_11方法被调用')
        return result
    print('func_1被调用')
    return func_11   # 返回func_11函数的地址，故可以直接写成arg()进行调用

@log_time
def func_2(a, b):
    def func_22(c):
        nonlocal a   # 把外部变量a的作用域赋给内嵌函数
        print('func_2的变量a =', a)
        a = 3
        res = a * b - c
        print('func_2计算结果：%d' % res)
        return res
    return func_22


if __name__ == '__main__':

    func_1(1, 2, 3)
    func_2(1, 2, 3)
