#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : anne yang

a = lambda x, y: x + y
print(a(1, 2))

def fun_a(x, y):
    sum = x + y
    return sum
print(fun_a(1, 2))

def factorial_fun(n):
    if n == 1:
        return n
    return n * factorial_fun(n-1)
print(factorial_fun(5))

def factorial_fun1(n):
    assert n >= 0, 'n不能小于0'
    if n <= 1:
        return n
    return factorial_fun1(n-1) + factorial_fun1(n-2)
print(factorial_fun1(4))