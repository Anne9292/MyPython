#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-11-11 15:42
# filename: MyPython-闭包

import time
import logging
logging.basicConfig(format='%(asctime)s--%(levelname)s: %(message)s',
                    level=logging.DEBUG)

"""
打印日志，计算函数执行时间
方式一：增加日志方法use_logging()
"""
def use_logging(func, a, b, c):
    logging.info('%s is running..........' % func.__name__)
    arg = func(a, b)
    print('{}的计算结果是：{}'.format(func.__name__, arg(c)))


"""
方式二：通过装饰器实现, 多个形参
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
    return func_11   # 返回func_2函数的地址，故可以直接写成arg()进行调用

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

"""
方式二：通过装饰器实现，无形参
"""
def use_logging2(func):
    def wrapper():
        logging.info('%s is running--------' % func.__name__)
        func()
    return wrapper

@use_logging2
def func_3():
    print('this is func_3')

@use_logging2
def func_33():
    print('this is func_33')

if __name__ == '__main__':
    # arg1 = func_1(1, 2)
    # print(arg1(4))
    # arg2 = func_2(1, 2)
    # print(arg2(3))

    # use_logging(func_1, 1, 2, 3)    # 改变了调用方式，必须通过use_logging方法才能调用各个函数，不够优雅

    func_1(1, 2, 3)
    func_2(1, 2, 3)
    # func_3()
    # func_33()