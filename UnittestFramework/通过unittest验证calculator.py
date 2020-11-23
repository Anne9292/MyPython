#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-11-22 14:50
# filename: PyCharm-常用模块

import unittest
from calculator import Calculator

class TestCase(object):

    def setUp(self):
        print('test start...')
        self.result = Calculator(10, 5)

    def teardown(self):
        print('test end...')

class TestCalculator(object):
    def test_001_sum(self):
        pass
