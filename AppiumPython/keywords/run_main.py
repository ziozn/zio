#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 0017 10:04
# @Author  : Aries
# @Site    : 
# @File    : run_main.py
# @Software: PyCharm
from keywords.get_data import GetData
from keywords.action_method import ActionMethod
from util.server import Server


class RunMain:
	def __init__(self):
		self.data = GetData()
		Server().main()
		self.action_metmod = ActionMethod()

	def run_metmod(self):
		lines = self.data.get_case_lines()
		for i in range(1, lines):
			# 操作方法代称
			handle_step = self.data.get_handle_step(i)
			# 被操作的ini文件元素名称
			element_key = self.data.get_element_key(i)
			# 被操作的数据，比如账号密码
			handle_value = self.data.get_handle_value(i)
			# 预期元素的ini名称
			expect_key = self.data.get_expect_element(i)
			# 预期步骤的名称
			expect_step = self.data.get_expect_handle(i)

			# 拿到操作方法对象
			excute_method = getattr(self.action_metmod, handle_step)

			if handle_value != '':
				excute_method(element_key, handle_value)
			else:
				excute_method(element_key)

			if expect_step != '':
				expect_result = getattr(self.action_metmod, expect_step)
				expect_result(expect_key)

			if expect_key != '':
				expect_result = getattr(self.action_metmod, expect_key)
				expect_result()


if __name__ == '__main__':
	RunMain().run_metmod()


