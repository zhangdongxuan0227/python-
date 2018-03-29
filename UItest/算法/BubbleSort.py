#!/usr/bin/python
# -*- coding: utf-8 -*-
_author__ = 'zhangxingchen'

mylist = [8, 9, 78, 25, 10, 100]


def BubbleSort(data):
	count = 0
	for i in range(len(data)):
		for j in range(len(data) - i - 1):
			if data[j] > data[j + 1]:
				tmp = data[j]
				data[j] = data[j + 1]
				data[j + 1] = tmp
			print(data)
			count += 1
	# print(data)

	print("循环次数:", count)

BubbleSort(mylist)