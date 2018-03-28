#!/usr/bin/python
# -*- coding: utf-8 -*-
_author__ = 'zhangxingchen'

class Sampler():
	def __enter__(self):
		print("enter")
		return "OK"

	def __exit__(self, exc_type, exc_val, exc_tb):
		print("exc_type", exc_type)
		print("exc_val", exc_val)
		print("exc_tb", exc_tb)
		print("exit")


	def dowrong(self):
		a = 10/0
		return a+10
def samplertest():
	return Sampler()

with samplertest() as samp1:
	print("sampler", samp1)


with Sampler() as r:
	r.dowrong()

