#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-05-19 14:59
# @Author  : Aries
# @Site    : 
# @File    : operation_json.py
# @Software: PyCharm
import json
import os


class OperetionJson:
	def __init__(self):
		json_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		self.json_path = os.path.join(json_path, 'dataconfig', 'login.json')

	def get_value(self, key):
		fb = open(self.json_path)
		data = json.load(fb)
		return data[key]


if __name__ == '__main__':
	print(OperetionJson().get_value('login'))

