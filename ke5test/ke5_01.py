#!/usr/bin/python
# -*- coding: utf-8 -*-


_author__ = 'zhangxingchen'

import json
import time
from selenium.webdriver.chrome.webdriver import WebDriver

a = "nihao sb"
print(end="你说啥")

print("字符串是：%s" % a, end="")

print("再说你试试")

a = {"a": "12345",
     "b": 1,
     "c": ['1', 'zxc'],
     "d": {"aa": "123",
           "bb": 123456}
     }

print(a)

a["b"] = 20
print(a)

a["f"] = 222
print(a)

del a["a"]
print(a)



print(type(a))

json1 = json.dumps(a) #字典转json格式
print(json1)

print(type(json1))


load2 = json.loads(json1) #json转字典 dict{}

print(load2)
print(type(load2))


for i in json1:
	print(i,end="")

print(len(json1))

print(json1[0:5])


