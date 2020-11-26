#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: anne
# datetime: 2020-11-26 18:05
# filename: MyPython/testclass_2

import unittest
from calculator import Calculator


class TestCalculator2(unittest.TestCase):

    def setUp(self):
        # print('TestCalculator2 test start...')
        self.result = Calculator(10, 5)   # 类实例化

    def test_001_add(self):
        """Test method add(a, b)"""
        self.assertEqual(self.result.add(), 15, "计算错误！")

    def test_002_minus(self):
        """Test method minus(a, b)"""
        self.assertEqual(self.result.minus(), 5, "计算错误")

    def test_003_multi(self):
        """Test method multi(a, b)"""
        self.assertEqual(self.result.multi(), 50, "计算错误")

    def test_004_divsion(self):
        """Test method divsion(a, b)"""
        self.assertEqual(self.result.divsion(), 2, "计算错误")

    def teardown(self):
        print('test end...')