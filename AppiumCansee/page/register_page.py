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

	# 获取登录URL
	def get_url(self):
		return self.fd.get_element('login_domain')

	# 获取登录周期
	def get_zq(self):
		return self.fd.get_element('login_expire')

	# 获取登录用户名
	def get_yhm(self):
		return self.fd.get_element('login_username')

	# 获取登录验证名
	def get_yzm(self):
		return self.fd.get_element('login_authName')

	# 获取登录密码
	def get_pwd(self):
		return self.fd.get_element('login_passwd')

	# 获取下拉列表
	def get_ipList(self):
		return self.fd.get_element('login_treaty')

	# 获取TCP元素
	def get_tcp(self):
		return self.fd.get_element('login_TCP')

	# 获取提交按钮
	def get_submit(self):
		return self.fd.get_element('login_submit')

	# 获取视频会议图标
	def get_sphy(self):
		return self.fd.get_element('cansee_call')

	# 获取通讯录
	def get_txl(self):
		return self.fd.get_element('cansee_mail')

	# 获取版本信息
	def get_bb(self):
		return self.fd.get_element('cansee_Version')

	# 打开设置界面
	def get_show(self):
		return self.fd.get_element('main_show_iv')

	# 获取设置界面
	def get_setting(self):
		return self.fd.get_element('main_setting_ll')

	# 获取最近会议界面
	def get_zjhy(self):
		return self.fd.get_element('main_contact_ll')

	# 获取设备设置
	def get_sbsz(self):
		return self.fd.get_element('device_rl')

	# 获取sip注册按钮
	def get_sip(self):
		return self.fd.get_element('sip_rl')

	# 获取通话设置
	def get_thsz(self):
		return self.fd.get_element('rate_rl')

	# 获取sip的输入框
	def get_sipId(self):
		return self.fd.get_element('sip_domain')

	# 获取注册周期
	def get_zczq(self):
		return self.fd.get_element('sip_expire')

	# 获取登录账号
	def get_user(self):
		return self.fd.get_element('sip_username')

	# 获取验证名称
	def get_userName(self):
		return self.fd.get_element('sip_authName')

	# 获取获取密码框
	def get_password(self):
		return self.fd.get_element('sip_passWd')

	# 获取注册确定按钮
	def get_sip_submit(self):
		return self.fd.get_element('submit')

	# 获取会议室号码输入框
	def get_number(self):
		return self.fd.get_element('call_number')

	# 获取拨号按钮
	def get_call_submit(self):
		return self.fd.get_element('call_submit')

	# 获取闭麦按钮
	def get_Closed_wheat(self):
		return self.fd.get_element('Closed_wheat')

	# 获取参数设置号码
	def get_menu_setting(self):
		return self.fd.get_element('all_menu_setting')

	# 获取入会人信息
	def get_attendees(self):
		return self.fd.get_element('login_authName')

	# 获取分屏按钮
	def get_fenPing(self):
		return self.fd.get_element('all_menu_fenPing')

