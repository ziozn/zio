#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/3 0003 14:38
# @Author  : Aries
# @Site    : 
# @File    : register_page.py
# @Software: PyCharm
from util.find_element import FindElement


# 元素层
class RegisterPage:
	def __init__(self, i):
		self.fd = FindElement(i)

	# 获取个人信息界面元素
	def get_jump_account(self):
		return self.fd.get_element('jump_account')

	# 获取登录界面元素
	def get_click_login(self):
		return self.fd.get_element('click_login')

	# 获取账号密码登录页面元素
	def get_jump_login(self):
		return self.fd.get_element('jump_login')

	# 获取账号
	def get_user_name(self):
		return self.fd.get_element('user_name')

	# 获取密码
	def get_pass_word(self):
		return self.fd.get_element('pass_word')

	# 获取登录按钮
	def get_login_button(self):
		return self.fd.get_element('login_button')

	# 获取登录成功的断言
	def login_success(self):
		return self.fd.get_element('login_success')

	# 获取登录失败的断言
	def login_error(self):
		return self.fd.get_element('login_error')

	# 获取登录失败的断言
	def login_error2(self):
		return self.fd.get_element('login_error2')


