#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-05-22 14:21
# @Author  : Aries
# @Site    : 
# @File    : runmethod.py
# @Software: PyCharm
import requests
import json


class RunMethod:
	@staticmethod
	def post_main(url, data, header=None):
		res = None
		if header is not None:
			res = requests.post(url=url, data=data, headers=header)
		else:
			res = requests.post(url=url, data=data)
		return res.json()

	@staticmethod
	def get_main(url, header, data=None):
		res = None
		if header is not None:
			res = requests.get(url=url, data=data, headers=header).json()
		else:
			res = requests.get(url=url, data=data).json()
		return res

	def run_main(self, url, method, data=None, header=None):
		res = None
		if method == 'POST':
			res = self.post_main(url, data, header)
		else:
			res = self.get_main(url, header, data)
		return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)

















