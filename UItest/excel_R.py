#!/usr/bin/python
# -*- coding: utf-8 -*-
_author__ = 'zhangxingchen'

import xlrd

data = xlrd.open_workbook("C:\\Users\\Administrator\\Desktop\\优房贷.xlsx")


table = data.sheet_by_index(0)

nrows = table.nrows

ncols =table.ncols
for i in range(nrows):
	rowValue = table.row_values(i)
	for item in rowValue:
		print(item)










# table = data.sheets()[0]             #通过索引顺序获取
# table = data.sheet_by_index(0)       #通过索引顺序获取
# table = data.sheet_by_name(u'Sheet1') #通过名称获取
#
# print(table.row(1))
# print(table.row_values(1))  #行
#
# print(table.col_values(2))  #列
#
#
# print(table.ncols)
#
# print(table.nrows)

# table.col_values(i)
#
#
# nrows = table.nrows
# ncols = table.ncols




# for i in range(table.nrows):
# 	print(table.row_values(i))
#
#
# cell_A1 = table.cell(0, 0).value
# cell_C4 = table.cell(0, 5).value
#
# #print(cell_A1)
#
# print(cell_C4)
#
# cell_A2 = table.cell(1,22).value
#
# datestr = xlrd.xldate_as_tuple(cell_A2,0)
#
# print(datestr)
#
# datestr2 = xlrd.xldate_as_datetime(cell_A2,0)
#
# print(datestr2)



