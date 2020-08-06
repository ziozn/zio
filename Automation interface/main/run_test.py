#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-05-22 15:22
# @Author  : Aries
# @Site    : 
# @File    : run_test.py
# @Software: PyCharm
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common import is_contain


class RunTest:
	def __init__(self):
		self.run_method = RunMethod()
		self.data = GetData()

	def go_on_run(self):
		res = None
		rows_count = self.data.get_case_lines()
		for i in range(1, rows_count):
			url = self.data.get_request_url(i)
			method = self.data.get_request_method(i)
			is_run = self.data.get_is_run(i)
			data = self.data.get_data_for_json(i)
			expect = self.data.get_expect_data(i)
			header = self.data.is_header(i)
			if is_run:
				res = self.run_method.run_main(url, method, data, header)
				if is_contain(expect, res):
					self.data.write_result(i, '测试通过')
				else:
					self.data.write_result(i, '测试失败')
		return res


if __name__ == '__main__':
	RunTest().go_on_run()












