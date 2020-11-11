# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : anne yang

class Animals(object):
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def eat(self):
        name = 'cat'
        category = 'roof'
        print('真的是动物呀', name, category)

if __name__ == '__main__':
    dog = Animals('la', 'ee')
    dog.eat()