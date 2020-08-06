#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-04-28 17:29
# @Author  : Aries
# @Site    : 
# @File    : demo.py
# @Software: PyCharm
import requests
import json


class RunMain:

	@staticmethod
	def send_post(url, data):
		res = requests.post(url, data=data).json()
		return json.dumps(res, indent=2, sort_keys=True)

	@staticmethod
	def send_get(url, data):
		res = requests.get(url, data=data).json()
		return json.dumps(res, indent=2, sort_keys=True)

	def run_main(self, url, method, data=None):
		res = None
		if method == 'GET':
			res = self.send_get(url, data)
		else:
			res = self.send_post(url, data)
		res = json.loads(res)
		return res


if __name__ == '__main__':
	data1 = {
		'username': 'ziop111',
		'password': '123456'
	}
	url1 = 'http://127.0.0.1:8000/jump/'
	print(type(RunMain().run_main(url1, 'POST', data1)))

