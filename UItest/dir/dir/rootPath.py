#!/usr/bin/python
# -*- coding: utf-8 -*-
_author__ = 'zhangxingchen'
import os


def getCurPath1():
	cur_path = os.path.dirname(os.path.realpath(__file__))
	return cur_path


def getCurPath2():
	cur_path = os.getcwd()
	return cur_path

'''os.path.dirname获取的__file__所在脚本的路径,
	1. os.path.dirname()：去掉脚本的文件名，返回目录。

	2. os.path.dirname(os,path.realname(__file__))：指的是，获得你刚才所引用的模块 所在的绝对路径，__file__为内置属性。
	
	3. os.getcwd 获取外层调用的路径
'''
print('func1----' + getCurPath1())
print('func2----' + getCurPath2())