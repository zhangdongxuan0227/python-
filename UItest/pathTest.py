#!/usr/bin/python
# -*- coding: utf-8 -*-
_author__ = 'zhangxingchen'
import os
from ke6 import unit

# 该文件所在位置：D:\第1层\第2层\第3层\第4层\第5层\test11.py

path1 = os.path.dirname(__file__)
print(path1)  # 获取当前运行脚本的绝对路径

path2 = os.path.dirname(os.path.dirname(__file__))  #
print(path2)  # 获取当前运行脚本的绝对路径（去掉最后一个路径）

path3 = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print(path3)  # 获取当前运行脚本的绝对路径（去掉最后2个路径）

path4 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
print(path4)  # 获取当前运行脚本的绝对路径（去掉最后3个路径）

path5 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
print(path5)  # 获取当前运行脚本的绝对路径（去掉最后4个路径）

path6 = os.__file__  # 获取os所在的目录
print(path6)