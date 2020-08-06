#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 0020 15:25
# @Author  : Aries
# @Site    : 读取/运行CMD命令
# @File    : dos_cmd.py
# @Software: PyCharm
import os


class DosCmd:

	def excute_cmd_result(self, command):
		result_list = []
		result = os.popen(command).readlines()
		for i in result:
			if i == '\n':
				continue
			result_list.append(i.strip('\n'))
		return result_list

	def excute_cmd(self, command):
		os.system(command)




