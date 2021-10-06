#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-11-12 19:18
# filename: MyPython-类装饰器

class TestClass(object):
    def __init__(self, func):
        print('inside my {}'.format(func.__name__))
        self._func = func

    def __call__(self):
        print('class decorator starting...')
        self._func()
        print('class decorator ending...')


@TestClass  # 类装饰器，会优先执行所有@TestClass的__init__()魔法函数，然后再调用__call__()
def func():
    print('func_1 running...')


@TestClass
def func_2():
    print('func_2 running...')


if __name__ == '__main__':
    func()
