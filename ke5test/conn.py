#!/usr/bin/python
# -*- coding: utf-8 -*-
_author__ = 'zhangxingchen'

import pymysql


config = {
	"host":"10.10.23.79",
	"port":3306,
    "user":"xzdh",
    "passwd":"5Fy7ttDgRY",
    "db":"sales",
	"charset":"utf8"
}

# 打开数据库链接
db = pymysql.connect(**config)

# cursor()创建游标对象

conn = db.cursor()

# excute()方法执行sql

sql = "SELECT ID,contract_id FROM t_loan_contract_info;"

try:
	# 执行sql
	conn.execute(sql)
	# 获取所有记录
	results = conn.fetchall()
	for row in results:
		contract_id = row[0]
		contract_sqe = row[1]
		print(row)
	# article = ((row[0],row[1]) for row in results)
	# print(article)
	print(results)

# db.commit()



except:
	print("error")

conn.close()

db.close()

if results:
	print('连接成功')
else:
	print('连接失败')



