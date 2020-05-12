# -*- coding: utf-8 -*-

# 字符串循环
def str_test():
    string = 'anne'
    for char in string:
        print(char, end='')
    print()

# 打印直角三角形
def triangle_test():
    for i in range(0,4):
        for j in range(0, i+1):
            print('*', end='')
        print()

# 比大小
def compare_test(num1, num2):
    if num1 > num2:
        print('too big')
        return False
    elif num1 < num2:
        print('too small')
        return False
    else:
        print('bingo!')
        return True

if __name__ == '__main__':
    # str_test()
    # triangle_test()
    compare_test(22, 22)