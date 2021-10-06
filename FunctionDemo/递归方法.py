#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 循环语句实现1*2*3*4*...*n
def fn1(n):
    results = n
    for i in range(1, n):
        results *= i
    return results


# 递归函数实现1*2*3*4*...*n
def fn2(n):
    if n == 1:
        return 1
    else:
        return n * fn2(n - 1)


# 递归函数实现菲波列契数列
def fn3(n):
    assert n >= 0, 'n不能小于0'
    if n < 2:
        return n
    return fn3(n - 1) + fn3(n - 2)


# 汉诺塔递归
'''
函数名中a、b、c变量的定义：a=操作区；b=缓冲区；c=目标区，n为个数
我们的目的：将 操作区 的数移动到 目标区 里，所以函数执行只有一句话：操作区--->目标区
第一步：将 操作区a 前n-1个数移动到 缓冲区b 里，这时 缓冲区b 就是我们这一步的目标区；所以是move(n-1,a,c,b)
第二步：将 操作区a 的最后一个数移动到 目标区c 里，即move(1, a, b, c)
注意：这时，操作区a的东西已经全部移动到缓冲区b和目标区c里了，操作区a已经为空了。所以缓冲区b就成为了新的操作区（里头有m=n-1个），而之前的操作区a成为了新的缓冲区
第三步: 将a、b交换后再一次执行move函数，即 move(m,b,a,c)，并且此时m=n-1
'''


def move(n, a, b, c):  # a=操作变量，b=缓存变量，c=目标变量，n为个数
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


if __name__ == '__main__':
    # number = int(input("请输入一个整数："))
    # result1 = fn1(number)
    # result2 = fn2(number)
    # print("%d的阶乘是：%d" % (number, result1))
    # print("%d的阶乘是：%d" % (number, result2))
    # move(3,'A','B','C')
    print([fn3(i) for i in range(1, 11)])
