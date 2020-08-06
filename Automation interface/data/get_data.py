#!/usr/bin/env pythonr
# -*- coding: utf-8 -*-
# @Time    : 2020-05-20 9:30
# @Author  : Aries
# @Site    : 
# @File    : get_data.py
# @Software: PyCharm
from util.excel_unit import OperationExcel
from data import data_config
from util.operation_json import OperetionJson


class GetData:
	def __init__(self):
		self.opera_excel = OperationExcel()

	# 获取行数，也就是case的个数
	def get_case_lines(self):
		return self.opera_excel.get_lines()

	# 获取是否执行
	def get_is_run(self, row):
		col = data_config.get_run()
		run_model = self.opera_excel.get_col_value(row, col)
		if run_model == 'yes':
			return True
		else:
			return False

	# 是否携带header
	def is_header(self, row):
		col = data_config.get_header()
		header = self.opera_excel.get_col_value(row, col)
		if header == "yes":
			return data_config.get_header_value()
		else:
			return None

	# 获取请求方式
	def get_request_method(self, row):
		col = data_config.get_run_way()
		request_method = self.opera_excel.get_col_value(row, col)
		return request_method

	# 获取url
	def get_request_url(self, row):
		col = data_config.get_url()
		url = self.opera_excel.get_col_value(row, col)
		return url

	# 获取请求数据
	def get_request_data(self, row):
		col = data_config.get_data()
		data = self.opera_excel.get_col_value(row, col)
		if data is None:
			return None
		return data

	# 通过关键字拿到data数据
	def get_data_for_json(self, row):
		opera_json = OperetionJson()
		data = self.get_request_data(row)
		if data is None:
			return None
		request_data = opera_json.get_value(data)
		return request_data

	# 获取预期结果
	def get_expect_data(self, row):
		col = data_config.get_expect()
		expect = self.opera_excel.get_col_value(row, col)
		if expect is None:
			return None
		return expect

	# 写入实际结果
	def write_result(self, row, value):
		col = data_config.get_result()
		self.opera_excel.write_value(row, col, value)

	# 获取依赖数据的key
	def get_depend_key(self, row):
		col = data_config.get_data_depend()
		depend_key = self.opera_excel.get_col_value(row, col)
		return depend_key

	# 判断是否有case依赖
	def is_depend(self, row):
		col = data_config.get_field_depend()
		depend_case_id = self.opera_excel.get_col_value(row, col)
		return depend_case_id

	# 获取数据依赖字段







