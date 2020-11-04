# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : anne yang

def fun_a():
    def fun_b():
        def fun_c():
            name = 'anne'
            print('局部函数定义的变量{}'.format(name))
        return fun_c
    return fun_b

if __name__ == '__main__':
    val = fun_a()
    val1 = val()
    val1()