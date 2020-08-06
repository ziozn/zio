#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 0016 15:37
# @Author  : Aries
# @Site    : 
# @File    : get_data.py
# @Software: PyCharm
from util.opera_excel import ExcelUtil


class GetData:
	def __init__(self):
		self.opera_excel = ExcelUtil()

	def get_case_lines(self):
		"""
		:return:返回excel 的行数
		"""
		lines = self.opera_excel.get_lines()
		return lines

	def get_handle_step(self, row):
		"""
		:return:返回操作步骤里面的操作方法名字
		"""
		method_name = self.opera_excel.get_col_value(row, 3)
		return method_name

	def get_element_key(self, row):
		"""
		:return:返回被操作的元素名
		"""
		element_key = self.opera_excel.get_col_value(row, 4)
		if element_key == ' ':
			return None
		return element_key

	def get_handle_value(self, row):
		"""
		:return:返回被操作的元素值
		"""
		handle_value = self.opera_excel.get_col_value(row, 5)
		if handle_value == ' ':
			return None
		return handle_value

	def get_expect_element(self, row):
		"""
		:return:返回预期结果元素element
		"""
		expect_element = self.opera_excel.get_col_value(row, 6)
		if expect_element == '':
			return None
		return expect_element

	def get_expect_handle(self, row):
		"""
		:return:返回预期步骤名称
		"""
		expect_handle = self.opera_excel.get_col_value(row, 7)
		if expect_handle == '':
			return None
		return expect_handle




