# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : anne yang

def fun_a():
    name = 'yang'
    def fun_b():
        # 若局部函数中定义有与所在函数中定义的同名变量，会发生“遮蔽”问题，导致局部函数的同名变量失效
        nonlocal name   # 避免遮蔽情况发生
        print(name)
        name = 'anne'
        print('局部函数定义的变量{}'.format(name))
    return fun_b

if __name__ == '__main__':
    val = fun_a()
    val()