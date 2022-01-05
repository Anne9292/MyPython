#!/usr/bin/python3
# -*- coding:utf-8 -*-


# class MyClass(object):  # 新式类
class MyClass:            # 经典类
    """一个简单的类实例"""
    i = 12345

    def f(self):
        return 'hello world'


if __name__ == '__main__':

    # 实例化类
    x = MyClass()
    # 访问类的属性和方法
    print("MyClass 类的属性i为：", x.i)
    print("MyClass 类的方法f输出为：", x.f())
