#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-04-29 14:43
# @Author  : Aries
# @Site    : 
# @File    : test_method.py
# @Software: PyCharm
import unittest
from util.mock_demo import mock_test
from base.demo import RunMain
import HTMLTestRunner
import os


class TestMethod(unittest.TestCase):

	@classmethod
	def setUpClass(cls) -> None:
		print('类前方法')

	@classmethod
	def tearDownClass(cls) -> None:
		print('类后方法')

	def setUp(self) -> None:
		self.run = RunMain()

	def tearDown(self) -> None:
		print('test--->tearDown')

	def test_01(self):
		data1 = {
			'username': 'ziop111',
			'password': '123456'
		}
		url1 = 'http://127.0.0.1:8000/jump/'
		res = mock_test(self.run.run_main, data1, url1, "POST", data1)
		self.assertEqual(res['username'], 'ziop111', '测试成功')
		print(res)

	def test_02(self):
		data1 = {
			'username': 'ziop222',
			'password': '12345'
		}
		url1 = 'http://127.0.0.1:8000/jump/'
		res = mock_test(self.run.run_main, data1, url1, "POST", data1)
		# res = self.run.run_main(url1, 'POST', data1)
		self.assertEqual(res['username'], 'ziop222', '测试成功')
		print(res)


if __name__ == '__main__':
	case_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	case_path = os.path.join(case_path, 'report', 'first_case.html')
	fp = open(case_path, 'wb')
	# unittest.main()
	suite = unittest.TestSuite()
	# suite.addTest(TestMethod('test_01'))
	suite.addTest(TestMethod('test_02'))
	# unittest.TextTestRunner().run(suite)
	runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='this is test')
	runner.run(suite)



