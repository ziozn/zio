#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/15 0015 16:04
# @Author  : Aries
# @Site    : 
# @File    : base_driver.py
# @Software: PyCharm
from appium import webdriver
from util.write_user_command import WriteUserCommand


class BaseDriver:

	def __init__(self):
		self.write_file = WriteUserCommand()

	def android_driver(self, i):
		# devices_name
		# port
		devices = self.write_file.get_value('user_info_' + str(i), 'deviceName')
		port = self.write_file.get_value('user_info_' + str(i), 'port')
		capabilities = {
			"platformName": "Android",
			"automationName": "UiAutomator2",
			"platformVersion": "5.1.1",
			"deviceName": devices,
			"app": "C:\\Users\\Administrator\\Downloads\\mukewang_7280.apk",
			"appActivity": "com.imooc.component.imoocmain.index.MCMainActivity"
		}
		driver = webdriver.Remote('http://127.0.0.1:' + port + '/wd/hub', capabilities)
		driver.implicitly_wait(3)
		return driver



