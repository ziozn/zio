#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 0025 9:52
# @Author  : Aries
# @Site    : 
# @File    : envirinment.py
# @Software: PyCharm

from selenium import webdriver


def before_all(context):
    context.driver = webdriver.Chrome()


def after_all(context):
    context.driver.close()
