#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-05-18 10:03
# @Author  : Aries
# @Site    : 
# @File    : mock_demo.py
# @Software: PyCharm
from unittest.mock import Mock


def mock_test(mock_method, request_data, url, method, response_data):
	mock_method = Mock(return_value=response_data)
	res = mock_method(url, method, request_data)
	return res





