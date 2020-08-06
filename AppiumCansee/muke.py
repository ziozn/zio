#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-06-29 9:33
# @Author  : Aries
# @Site    : 
# @File    : muke.py
# @Software: PyCharm
from appium import webdriver
import unittest


class muke(unittest.TestCase):
	def test_webview(self):
		caps = {
			'platformName': 'android',
			'deviceName': '127.0.0.1:62025',
			"platformVersion": "5.1.1",
			'appPackage': 'cn.com.open.mooc',
			'appActivety': 'com.imooc.component.imoocmain.index.MCMainActivity',
			'dontStopAppOnReset': True,
			'noReset': True
		}
		capabilities = {
			"platformName": "Android",
			"automationName": "UiAutomator2",
			"platformVersion": "5.1.1",
			"deviceName": 'ddd',
			# "app": "C:\\Users\\Administrator\\Downloads\\mukewang_7280.apk",
			"appActivity": "com.imooc.component.imoocmain.index.MCMainActivity"
		}
		driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
		driver.implicitly_wait(5)


if __name__ == '__main__':
	muke().test_webview()




