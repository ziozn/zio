#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/7 0007 10:10
# @Author  : Aries
# @Site    : 
# @File    : register_handle.py
# @Software: PyCharm
from page.register_page import RegisterPage


# 操作元素页面
class RegisterHandle:

	def __init__(self, i):
		self.Register_p = RegisterPage(i)

	# 跳转到个人信息界面
	def jump_user(self):
		self.Register_p.get_jump_account().click()

	# 跳转到登录界面
	def click_login(self):
		self.Register_p.get_click_login().click()

	# 跳转到账号密码登录
	def jump_login(self):
		self.Register_p.get_jump_login().click()

	# 请输入账号
	def send_name(self, name):
		self.Register_p.get_user_name().send_keys(name)

	# 请输入密码
	def send_pass(self, pwd):
		self.Register_p.get_pass_word().send_keys(pwd)

	# 点击登录按钮
	def login_button(self):
		self.Register_p.get_login_button().click()

	# 获取登录元素断言
	def get_login_assertion(self, info):
		if info == 'login_success':
			text = self.Register_p.login_success().text
		else:
			text = '登录失败'
		return text

