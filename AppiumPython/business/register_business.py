#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/7 0007 14:48
# @Author  : Aries
# @Site    : 
# @File    : register_business.py
# @Software: PyCharm
from handle.register_handle import RegisterHandle
from appium import webdriver


# 执行操作业务
class RegisterBusiness:

	def __init__(self, i):
		self.register_h = RegisterHandle(i)

	def user_base(self, name, pwd):
		self.register_h.jump_user()
		self.register_h.click_login()
		self.register_h.jump_login()
		self.register_h.send_name(name)
		self.register_h.send_pass(pwd)
		self.register_h.login_button()

	def login_success(self, name, pwd):
		self.user_base(name, pwd)
		if self.register_h.get_login_assertion('login_success') is not None:
			print('登录成功')
			return 1
		else:
			print('登录异常')
			return 0

	def login_error(self, name, pwd):
		self.user_base(name, pwd)
		if self.register_h.get_login_assertion('login_error') is not None:
			print('登录失败')
			return 1
		else:
			print('登录异常')
			return 0


