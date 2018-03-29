#!/usr/bin/python
# -*- coding: utf-8 -*-
_author__ = 'zhangxingchen'

def QucikSort(lists, start , end):
	if start < end:
		i, j = start, end

		#基数
		key = lists[i]

		while i < j:
			while (i < j) and (lists[j] > key):
				j = j - 1
			lists[i] = lists[j]

			while (i < j) and (lists[i] < key):
				i = i + 1
			lists[j] = lists[i]

		lists[i] = key
		#递归
		QucikSort(lists, start, i-1)
		QucikSort(lists, j+1, end)

	return lists

mylist = [80, 25, 56, 41, 19, 99, 38]

print("排序后：")

QucikSort(mylist, 0 ,len(mylist)-1)

print(mylist)


