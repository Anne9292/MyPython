#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : anne yang

def xarg(arg_x):
    arg_x = 10
    print('函数体内：{}'.format(arg_x))

def sarg(arg_s):
    arg_s.append([2, 4, 5])
    print('函数体内：{}'.format(arg_s))

if __name__ == '__main__':
    arg_s = 2
    xarg(arg_s)
    print('函数体外：{}'.format(arg_s))
    arg_s1 = [1, 2, 3]
    sarg(arg_s1)
    print('函数体外：{}'.format(arg_s1))