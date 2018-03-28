#!/usr/bin/python
# -*- coding: utf-8 -*-
_author__ = 'zhangxingchen'

import re
import requests

from bs4 import BeautifulSoup

import os
#获取翻页的文章列表
url = ["http://www.cnblogs.com/andashu/default.html?page={}".format(str(i)) for i in range(1, 8)]

print(url)

url1 = "http://www.cnblogs.com/andashu/default.html?page=1"
r = requests.get(url1).text
m = BeautifulSoup(r, "html.parser")

titles = m.select(".postTitle2")
#print(m.select(".postTitle2"))

res = r'>(.+?)</a>'

for i in titles:
	data = {
		'title':i.get_text()
	}


	print(data)

