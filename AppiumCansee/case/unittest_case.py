#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/13 0013 11:07
# @Author  : Aries
# @Site    : 
# @File    : unittest_case.py
# @Software: PyCharm
from business.register_business import RegisterBusiness
from business.login_business import LoginBusiness
import time
import multiprocessing
from util.server import Server
import unittest
import os
import HTMLTestRunner
from util.write_user_command import WriteUserCommand


class ParameTestCase(unittest.TestCase):
	def __init__(self, methodName='runTest', parame=None):
		super(ParameTestCase, self).__init__(methodName)
		global parames
		parames = parame


class FirstCase(ParameTestCase):

	@classmethod
	def setUpClass(cls):
		cls.login = LoginBusiness(parames)
		# cls.login.login_base('vcse.cansee.net', '300', '610102@cansee.net', '610102', 'ss')
		cls.login = RegisterBusiness(parames)
		print('所有case执行之前执行的' + str(parames))

	@classmethod
	def tearDownClass(cls):
		print('所有case执行之后执行的')

	def setUp(self):
		# self.login = RegisterBusiness(parames)
		print('用例执行之前')

	def tearDown(self):
		time.sleep(5)
		print('用例执行完毕后')

	# 登录成功
	def test_login_success(self):
		print('success开始执行')

		# self.login.login_success()
		self.login.login_success('88886819')

	# result = self.login.login_success('18771917218', 'laobalaoma7272')
	# print(self.assertTrue(result, '执行成功'))

# 登录失败
# def test_login_error(self):
# 	print('error开始执行')
# 	self.login.login_error('777555')

# result = self.login.login_error('18771917218', 'laobalaoma727')
# print(self.assertTrue(result, '执行成功'))


def appium_init():
	server = Server()
	server.main()


def get_count():
	write_user_file = WriteUserCommand()
	conut = write_user_file.get_file_lines()
	return conut


def get_suite(i):
	print(i)
	case_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	case_path = os.path.join(case_path, 'report', 'first_case' + str(i) + '.html')
	f = open(case_path, 'wb+')
	# suite = unittest.TestLoader().loadTestsFromTestCase(FirstCase)
	suite = unittest.TestSuite()
	# suite.addTest(FirstCase('test_login_error', parame=i))
	suite.addTest(FirstCase('test_login_success', parame=i))

	runner = HTMLTestRunner.HTMLTestRunner(stream=f)
	runner.run(suite)


if __name__ == '__main__':
	appium_init()
	# get_suite()
	threads = []
	for i in range(get_count()):
		t = multiprocessing.Process(target=get_suite, args=(i,))
		# t = threading.Thread(target=get_suite, args=(i,))
		threads.append(t)
	for j in threads:
		j.start()
