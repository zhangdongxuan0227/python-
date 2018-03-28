#!/usr/bin/python
# -*- coding: utf-8 -*-
_author__ = 'zhangxingchen'


import smtplib
from email.mime.text import MIMEText


print(dir(MIMEText.__setitem__))


def func(a, b, c=0, *args, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


func(1,2,3,'a','b',x=99,)



c = sum([i for i in range(1,101)])

print(c)

print("hello world！")