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

	# 进入拨号界面
	def jump_dial(self):
		self.Register_p.get_sphy().click()

	# 输入会议号码
	def send_number(self, value):
		self.Register_p.get_number().send_keys(value)

	# 点击拨号按钮进入会议
	def button_dial(self):
		self.Register_p.get_call_submit().click()

	# 输入sip地址
	def send_sip(self, value):
		self.Register_p.get_url().send_keys(value)

	# 输入注册周期
	def send_cycle(self, value):
		self.Register_p.get_zq().send_keys(value)

	# 输入登录用户名
	def send_yhm(self, value):
		self.Register_p.get_yhm().send_keys(value)

	# 输入验证名
	def send_yzm(self, value):
		self.Register_p.get_yzm().send_keys(value)

	# 输入密码
	def send_mm(self, value):
		self.Register_p.get_pwd().send_keys(value)

	# 点击url下拉框
	def click_checkbox(self):
		self.Register_p.get_ipList().click()

	# 选择TCP协议
	def click_TCP(self):
		self.Register_p.get_tcp().click()

	# 点击登录按钮
	def click_login(self):
		self.Register_p.get_submit().click()

	# 获取首次成功断言
	def login_success(self):
		if self.Register_p.get_bb() is not None:
			print('登录成功')
			return 1
		else:
			print('拨号失败')
			return 0

	# 获取拨号成功的断言
	def call_success(self):
		if self.Register_p.get_sphy() is None:
			print('拨号成功')
			return 1
		else:
			print('拨号失败')
			return 0
