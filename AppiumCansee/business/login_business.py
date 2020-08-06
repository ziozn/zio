#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-07-28 9:50
# @Author  : Aries
# @Site    : 
# @File    : login_business.py
# @Software: PyCharm
from handle.register_handle import RegisterHandle


class LoginBusiness:

	def __init__(self, i):
		self.lb = RegisterHandle(i)

	def login_base(self, sip, zq, yhm, yzm, mm):
		self.lb.send_sip(sip)
		self.lb.send_cycle(zq)
		self.lb.send_yhm(yhm)
		self.lb.send_yzm(yzm)
		self.lb.send_mm(mm)
		self.lb.click_checkbox()
		self.lb.click_TCP()
		self.lb.click_login()

	def login_success(self):
		if self.lb.login_success() is not None:
			print('登录成功')
			return 1
		else:
			print('登录失败')
			return 0




