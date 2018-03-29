#!/usr/bin/python
# -*- coding: utf-8 -*-
_author__ = 'zhangxingchen'

def ChooseSort(lists):
	#获取长度
	l = len(lists)
	for i in range(0, l-1):

# 默认设置最小值得index为当前值
		smallest = i
# 用当先最小index的值分别与后面的值进行比较,以便获取最小index
		for j in range(i + 1, l):
# 如果找到比当前值小的index,则进行两值交换
			if myList[j] < myList[smallest]:
				tmp = myList[j]
				myList[j] = myList[smallest]
				myList[smallest] = tmp
# 打印每一轮比较好的列表
	print("Round ", i, ": ", lists)


myList = [6, 4, 5, 0, 2]
print("Selected Sort: ")
ChooseSort(myList)
