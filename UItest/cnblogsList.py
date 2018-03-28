#!/usr/bin/python
# -*- coding: utf-8 -*-
_author__ = 'zhangxingchen'

import requests

from bs4 import BeautifulSoup

import os

# 获取翻页的文章列表
urls = ["http://www.cnblogs.com/AngesZhu/default.html?page={}".format(str(i)) for i in range(1, 8)]

print(urls)


# r = requests.get(url).text

# print(r.text)


def get_title(urls, data=None):
	web_data = requests.get(urls)
	soup = BeautifulSoup(web_data.text, "html.parser")
	titles = soup.select(".postTitle2")
	for title in titles:
		data = {
			'title': title.get_text()
		}
		print(data)


for titles in urls:
	get_title(titles)

