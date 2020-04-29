# !/usr/bin/env python3
# _*_ coding: utf-8 _*_

'a test module'
__author__ = 'anne yang'

def study(course='chinese', teacher='anne'):
    print("course name: " + course)
    print("【%s】teacher is: %s" % (course, teacher))

def grade(a, b):
    sum = a + b
    print(sum)
    return sum   # 返回对象可以赋值给变量，或者直接使用

def test():
    return [1, '多返回值', 3.14]

#
def discount(price, rate):
    final_price = price * rate
    old_price = 50  # 这里想修改全局变量
    print("这里想打印全局变量old_price：", old_price)
    return final_price

# 计算圆的面积
def area_of_circle(x):
    area = 3.14 * pow(x,2)
    print("半径为%.2f的圆面积为：%.2f" % (x, area))


if __name__ == '__main__':
    study('english', 'tony')
    study()
    study(course='math', teacher='johnny')
    grade(1, 2)
    test()   # 不会返回任何值
    old_price = float(input("请输入原价："))
    rate = float(input("请输入折扣："))
    new_price = discount(old_price, rate)
    print("现在全局变量old_price：", old_price)
    print("打折后价格为：", new_price)
    area_of_circle(3)