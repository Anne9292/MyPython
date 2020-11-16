#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-11-16 11:15
# filename: MyPython-九九乘法表

def calculate():

    for i in range(1, 10):
        for j in range(1, i+1):
            res = i * j
            print('{}*{}={}'.format(i, j, res), end='\t')
        print()

if __name__ == '__main__':
    calculate()