#!/usr/bin/python
# -*- coding: utf-8 -*-
_author__ = 'zhangxingchen'
import xlwt


#创建一个workbook对象相当于创建一个 excel文件
book = xlwt.Workbook(encoding='utg-8', style_compression=0)

'''
Workbook类初始化时有encoding和style_compression参数
encoding:设置字符编码，一般要这样设置：w = Workbook(encoding='utf-8')，就可以在excel中输出中文了。
默认是ascii。当然要记得在文件头部添加：
#!/usr/bin/env python
# -*- coding: utf-8 -*-
style_compression:表示是否压缩，不常用。
'''

#创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。
# 在电脑桌面右键新建一个Excel文件，其中就包含sheet1，sheet2，sheet3三张表
sheet = book.add_sheet('test', cell_overwrite_ok=True)

sheet.write(0, 0, 'ip_address')

sheet