#!/usr/bin/python
# -*- coding: utf-8 -*-
_author__ = 'zhangxingchen'

import unittest
import time


class Test(unittest.TestCase):

	# def Add(self):
	# 	a = 2
	# 	b = 3
	# 	c = a + b
	# 	self.assertEqual(c, 5, "sucessful")
	#
	# def Multi(self):
	# 	a = 2
	# 	b = 3
	# 	c = 10
	# 	self.assertEqual(c, 6, "error")

	@classmethod
	def setUpClass(cls):
		print("setUpClass初始化操作：用例开始前只执行一次")
		print("\n")

	def setUp(self):
		print("start")

	def tearDown(self):
		time.sleep(1)

	def test_01(self):
		print("执行测试用例01")

	@unittest.skip
	def test_03(self):
		print("执行测试用例03")

	def test_02(self):
		print("执行测试用例02")

	def addinfor(self):
		print("执行测试用例04")


if __name__ == '__main__':
	unittest.main()
