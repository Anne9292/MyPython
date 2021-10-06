# -*- coding:utf-8 -*-

# 递归实现
def fn(n):
    assert n >= 0, "n < 0，不符合条件"
    if n <= 1:
        return n
    return fn(n - 1) + fn(n - 2)


# 递推实现
def fn1(n):
    a, b = 0, 1
    for i in range(n + 1):
        a, b = b, a + b
        # print('a是：', a)
        # print('b是：', b)
    return a


if __name__ == '__main__':

    for i in range(4):
        print(fn1(i))
