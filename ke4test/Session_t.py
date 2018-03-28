#!/usr/bin/python
# -*- coding: utf-8 -*-
_author__ = 'zhangxingchen'


import requests
import urllib3


urllib3.disable_warnings()

#登录的页面
url = " https://testerhome.com/account/sign_in"

#请求头信息
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
	AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"}

#登录参数

data = {"user[login]": "zxcser@163.com", "user[password]": "890227", "user[remember_me]": "0",  "commit": "登录"}

#保持登录会话
s1 = requests.session()


#登录
r1 = s1.post(url, headers=headers, json=data, verify=False)

res = r1.content.decode("utf-8")

print(r1.status_code)

print(res)

url2 = "https://testerhome.com/setting"



