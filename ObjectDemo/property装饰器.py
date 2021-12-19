#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-11-13 10:32
# filename: PythonProjectDemo-property装饰器


# @property装饰：只读属性，将类中的方法转换成属性
class DataSet(object):

    @property
    def method_with_property(self):
        return 'hello property'

    def method_without_property(self):
        return 'hello, without property'


# @score.setter装饰，只读属性，对score方法进行保护
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter  # @property装饰的函数score，要和@score.setter装饰的函数名保持一致
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100！')
        self._score = value


if __name__ == '__main__':
    # test_object = DataSet()
    # print(test_object.method_with_property)     # 加了@property后，可以用调用属性的形式调用方法，后面不需要加()
    # print(test_object.method_without_property())    # 没有加@property，必须使用正常调用方法形式，即后面需要加()

    student = Student()
    student.score = 99
    print(student.score)
