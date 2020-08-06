#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-05-25 11:51
# @Author  : Aries
# @Site    : 
# @File    : common.py
# @Software: PyCharm
import json
from data.get_data import GetData


def is_contain(str_one, str_two):
	flag = None
	if str_one in str_two:
		flag = True
	else:
		flag = False
	return flag


