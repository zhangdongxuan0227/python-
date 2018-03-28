#!/usr/bin/python
# -*- coding: utf-8 -*-
_author__ = 'zhangxingchen'

import requests
from bs4 import BeautifulSoup

import os
url = "http://699pic.com/sousuo-218808-13-1-0-0-0.html"

r =requests.get(url)

print(r.content)


soup = BeautifulSoup(r.content, "html.parser")
images = soup.find_all(class_= 'lazy')


curPath = os.path.dirname(os.path.realpath(__file__))
print(curPath)

print(os.path.realpath(__file__))

# for i in images:
#     try:
#     #print(i)
#
#         image_url = i['data-original']
#         title1 = i['title']
#         print(image_url)
#         print(requests.get(image_url).content)
#
#         with open(curPath+'\\'+title1+'.jpg', 'wb') as filename:
#             filename.write(requests.get(image_url).content)
#
#     except Exception as msg:
#         print(msg)


