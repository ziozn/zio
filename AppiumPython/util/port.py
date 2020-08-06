#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 0028 9:59
# @Author  : Aries
# @Site    : 
# @File    : port.py
# @Software: PyCharm
from util.dos_cmd import DosCmd


class Port:

	def __init__(self):
		self.dos = DosCmd()

	def port_is_used(self, port_num):
		result = self.dos.excute_cmd_result('netstat -ano | findstr ' + str(port_num))
		if len(result) > 0:
			flag = True
		else:
			flag = False
		return flag

	def create_port_list(self, start_port, device_list):
		"""
		生成可用端口
		:param start_port:
		:param device_list:
		:return:
		"""
		port_list = []
		if device_list is not None:
			while len(port_list) != len(device_list):
				if not self.port_is_used(start_port):
					port_list.append(start_port)
				start_port += 1
			return port_list
		else:
			print('生成可用端口失败')
			return None


if __name__ == '__main__':
	print(Port().create_port_list(4720, [1, 2, 3, 4, 5]))






