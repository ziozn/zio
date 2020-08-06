#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 0016 14:34
# @Author  : Aries
# @Site    : 
# @File    : action_method.py
# @Software: PyCharm
from util.find_element import FindElement
from util.base_driver import BaseDriver


class ActionMethod:
    def __init__(self):
        self.driver = BaseDriver().android_driver(0)
        self.get_by_element = FindElement(self.driver)

    def get_element(self, *args):
        element = self.get_by_element.get_element(args[0])
        if element == '':
            return 'element未找到'
        return element

    def input(self, *args):
        element = self.get_element(args[0])
        if element is None:
            return '元素未找到'
        element.send_keys(args[1])

    def on_click(self, *args):
        element = self.get_element(args[0])
        if element is None:
            return '元素未找到'
        element.click()

    # 获取屏幕的宽高
    def get_size(self, *args):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    # 获取左右滑动执行起始坐标点
    def swipe_transverse(self, *args):
        size = self.get_size()
        x1 = size[0] / 10 * 9
        y1 = size[1] / 2
        x = size[0] / 10
        return x1, y1, x, y1

    # 获取上下滑动执行起始坐标点
    def swipe_portrait(self, *args):
        size = self.get_size()
        y1 = size[0] / 10 * 9
        x1 = size[1] / 2
        y2 = size[0] / 100
        return y1, x1, y2, x1

    # 向左滑动
    def swipe_left(self, *args):
        x1, y1, x, y1 = self.swipe_transverse()
        self.driver.swipe(x1, y1, x, y1, 2000)

    # 向右滑动
    def swipe_right(self, *args):
        x1, y1, x, y1 = self.swipe_transverse()
        self.driver.swipe(x, y1, x1, y1, 2000)

    # 向上滑动
    def swipe_up(self, *args):
        y1, x, y2, x = self.swipe_portrait()
        self.driver.swipe(x, y1, x, y2)

    # 向下滑动
    def swipe_down(self, *args):
        y1, x, y2, x = self.swipe_portrait()
        self.driver.swipe(x, y2, x, y1)
