#!/usr/bin/python
# -*- coding: utf-8 -*-
_author__ = 'zhangxingchen'

import requests

import re

from pprint import pprint


def list12306():

	url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9050"

	r = requests.get(url, verify=False)

#print(r.content)
#print(r.text)
	station_name = dict(re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', r.text))

	pprint(dict(station_name), indent=4)
	pprint(station_name.keys())
	pprint(station_name.values())

if __name__ == '__main__':
	list12306()