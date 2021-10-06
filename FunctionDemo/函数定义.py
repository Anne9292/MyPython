#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""a test module"""
__author__ = 'anne yang'

import math


def my_abs(x):
    # 方法1：
    try:
        if x >= 0:
            return x
        else:
            return -x
    except TypeError as e:
        print('输入值类型错误啦：' + str(e))

    # # 方法2：
    # if not isinstance(x, (int, float)):
    #     raise TypeError('错误的数据类型')
    # if x >= 0:
    #     return x
    # else:
    #     return -x


def quadratic(a, b, c):
    # 解一元二次方程ax^2 + bx + c = 0
    try:
        arg1 = b * b - 4 * a * c
        if arg1 < 0:
            return '无实根!'
        elif arg1 == 0:
            x = -b / (2 * a)
            return x
        else:
            x1 = (-b + math.sqrt(arg1)) / (2 * a)
            x2 = (-b - math.sqrt(arg1)) / (2 * a)
            return x1, x2

    except TypeError as e:
        print('只能输入浮点数或整数！！' + str(e))


if __name__ == '__main__':
    # print(my_abs(0))
    # print(my_abs(5))
    # print(my_abs(-6))
    # print(my_abs('anne'))

    print(quadratic(1, 2, 3))
    print(quadratic('a', 'b', 3))
    print('quadratic(2, 3, 1) = ', quadratic(2, 3, 1))
    print('quadratic(1, 3, -4) = ', quadratic(1, 3, -4))
    if quadratic(2, 3, 1) != (-0.5, -1.0):
        print('测是失败！')
    elif quadratic(1, 3, -4) != (1.0, -4.0):
        print('测试失败！')
    else:
        print('测试成功！')
