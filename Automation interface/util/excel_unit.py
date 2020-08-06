#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-05-19 14:21
# @Author  : Aries
# @Site    : 
# @File    : excel_unit.py
# @Software: PyCharm
import xlrd
from xlutils.copy import copy


class OperationExcel:
	def __init__(self, excel_path=None, index=None):
		if excel_path is None:
			self.excel_path = 'C:\\Users\\Administrator\\PycharmProjects\\Automation interface\\dataconfig\\demo_excel.xls'
		else:
			self.excel_path = excel_path
		if index is None:
			index = 0
		# 整个表格
		self.data = xlrd.open_workbook(self.excel_path)
		self.table = self.data.sheets()[index]

	# 获取excel数据
	def get_data(self):
		result = []
		if self.get_lines() is None:
			return None
		for i in range(self.get_lines()):
			col = self.table.row_values(i)
			col[0] = str(int(col[0]))
			result.append(col)
		return result

	# 获取Excel行数
	def get_lines(self):
		rows = self.table.nrows
		if rows >= 1:
			return rows
		return None

	# 获取单元格的数据
	def get_col_value(self, row, col):
		if self.get_lines() > row:
			data = self.table.cell(row, col).value
			if isinstance(data, float):
				data = str(int(data))
			return data
		return None

	# 写入数据
	def write_value(self, row, col, value):
		read_value = xlrd.open_workbook(self.excel_path)
		write_data = copy(read_value)
		write_data.get_sheet(0).write(row, col, value)
		write_data.save(self.excel_path)

	# 根据对应的caseid,找到对应内容的行
	def get_rows_data(self, case_id):
		row_num = self.get_row_num(case_id)
		rows_data = self.get_row_values(row_num)
		return rows_data

	# 根据对应的caseid找到对应的行号
	def get_row_num(self, case_id):
		num = 0
		clols_data = self.get_cols_data()
		for col_data in clols_data:
			if case_id in col_data:
				return num
			num += 1

	# 根据行号找到该行的内容
	def get_row_values(self, row):
		return self.table.row_values(row)

	# 获取某一列的内容
	def get_cols_data(self, col_id=None):
		if col_id is not None:
			cols = self.table.col_values(col_id)
		else:
			cols = self.table.col_values(0)
		return cols


if __name__ == '__main__':
	pass


