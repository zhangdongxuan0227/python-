#!/usr/bin/python
# -*- coding: utf-8 -*-
_author__ = 'zhangxingchen'

import requests
import urllib3
import re


# c = "ffff"
# a = 1234
# b = "ffffff"

urllib3.disable_warnings()

#登录的页面
url = " https://testerhome.com/account/sign_in"

#登录参数
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
	AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"}

r1 = requests.get(url, headers=headers, verify=False)

#添加前的cookies
print(r1.cookies)

c = requests.cookies.RequestsCookieJar()


# print(os.getcwd())

c.set("user_id", "MTMyNDg%3D--4f3fade13e5d77bc66a580934d005f387383e511")

c.set("_homeland_session", "JYBys45bePD17XT8kE5eULju0ZCPXZ1ERAiyaqeNc8wl3qFOt%2FQOtWpwped1b0AdS%2FrIMD42TkqlgZ1ILXQu0UmqvPbUUf0V3kTgv1vKCW6tW%2FaSPpQlO45nf%2BeZ9lQw8cJZeriEToiUxEWoERkx%2FtfYPT%2B%2F8mxQlM6sBGBKtK4SUdaE%2\
FuewBViAbolIKBTKP%2F%2Fe1dDfrxM5aonbG%2BdMsuaiSZbMEBFDAlXTZaD0ZUJHj9OiAqn1xlkq6%2BGD49BOn%2Fa5MZUCelIROJ3u6RqoL4m5gKGtdiyOK61nG5g%3D--aQ2bAIICjsdp3NPz--GAwvAHAYvl%2BP5o8EqnX%2Fvg%3D%3D")

print("********添加后的cookies********")

print(r1.cookies)

# 访问登录之后的请求
url2 = "https://testerhome.com/topics/12286"


h1 = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"
}

r2 = requests.get(url2, verify=False, cookies=c, headers=h1)

content1 = r2.text


print(r2.status_code)
print(content1)


#提取title 利用正则
#  <title>携程对火车车型种类的搜索有误 · TesterHome</title>
title = re.findall(r'<title>(.*?)</title>', content1)

t1 =title[0]
if t1.index("携程") > -1:
	print("存在")
else:
	print("不存在")

if "携程" in t1:
	print("绕过登录成功")

else:
	print("登录失败")