#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/7 0007 14:48
# @Author  : Aries
# @Site    : 
# @File    : register_business.py
# @Software: PyCharm
from handle.register_handle import RegisterHandle


# 执行拨号操作业务
class RegisterBusiness:

	def __init__(self, i):
		self.register_h = RegisterHandle(i)

	def user_base(self, number):
		self.register_h.jump_dial()
		self.register_h.send_number(number)
		self.register_h.button_dial()

	def login_success(self, number):
		self.user_base(number)
		if self.register_h.call_success() is not None:
			print('拨号成功')
			return 1
		else:
			print('拨号异常')
			return 0

	# def login_error(self, number):
	# 	self.user_base(number)
	# 	if self.register_h.call_success() is not None:
	# 		print('登录失败')
	# 		return 1
	# 	else:
	# 		print('登录异常')
	# 		return 0


