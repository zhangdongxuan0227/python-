#!/usr/bin/python
# -*- coding: utf-8 -*-
_author__ = 'zhangxingchen'

import xlwt

def set_style(name, height, bold=False):
	style = xlwt.XFStyle()

	font = xlwt.Font()
	font.name = name #times NEW roman

	font.bold = bold
	font.colour_index = 4
	font.height = height

	style.font = font

	return style


file = xlwt.Workbook(encoding='utf-8')

table =file.add_sheet('班级信息表',cell_overwrite_ok=True)
row0 = [u'姓名', u'年龄', u'出生日期', u'爱好', u'关系']
column0 = [u'小杰', u'小胖', u'小明', u'大神', u'大仙']

print(len(row0))
for i in range(len(row0)):
	#print(i)

	table.write(0, i, row0[i], set_style('Times New Roman', 220, True))

for i in range(0, len(column0)):
	table.write(i + 1, 0, column0[i], set_style('Times New Roman', 220))


table.write(2, 3, '1989-02-24')
table.write_merge(4, 4, 2, 4, u'暂无') #合并列单元格
table.write_merge(1, 2, 4, 4, u'好朋友') #合并行单元格

file.save('filetest.xls')


