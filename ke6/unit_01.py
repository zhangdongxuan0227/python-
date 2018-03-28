#!/usr/bin/python
# -*- coding: utf-8 -*-
_author__ = 'zhangxingchen'


import unittest

class Test(unittest.TestCase):

	def setUp(self):
		self.num = input("输入数字：")
		self.num = int(self.num)

	def test_case1(self):
		print(self.num)
		self.assertEqual(self.num, 10, msg='Your input is not 10')

	def test_case2(self):
		print(self.num)
		self.assertEqual(self.num, 20, msg='Your input is not 20')

	@unittest.skip('暂时跳过用例3的测试')
	def test_case3(self):
		print(self.num)
		self.assertEqual(self.num, 30, msg='Your input is not 30')

	def tearDown(self):
		print("test end")

if __name__ == '__main__':
	unittest.main()