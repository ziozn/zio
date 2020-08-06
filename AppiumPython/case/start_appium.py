#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/27 0027 15:49
# @Author  : Aries
# @Site    : 
# @File    : start_appium.py
# @Software: PyCharm
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as EC

import time

capabilities = {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "platformVersion": "5.1.1",
    "deviceName": "127.0.0.1",
    "app": "C:\\Users\\Administrator\\Downloads\\mukewang_7280.apk",
    "appActivity": "com.imooc.component.imoocmain.index.MCMainActivity"
}


class Slide:

    def __init__(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)

    # 点击
    @staticmethod
    def element_click(emt):
        emt.click()

    # 输入
    @staticmethod
    def element_send(emt, key):
        emt.send_keys(key)

    # 获取屏幕的宽高
    def get_size(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    # 获取左右滑动执行起始坐标点
    def swipe_transverse(self):
        size = self.get_size()
        x1 = size[0] / 10 * 9
        y1 = size[1] / 2
        x = size[0] / 10
        return x1, y1, x, y1

    # 获取上下滑动执行起始坐标点
    def swipe_portrait(self):
        size = self.get_size()
        y1 = size[0] / 10 * 9
        x1 = size[1] / 2
        y2 = size[0] / 100
        return y1, x1, y2, x1

    # 向左滑动
    def swipe_left(self):
        x1, y1, x, y1 = self.swipe_transverse()
        self.driver.swipe(x1, y1, x, y1, 2000)

    # 向右滑动
    def swipe_right(self):
        x1, y1, x, y1 = self.swipe_transverse()
        self.driver.swipe(x, y1, x1, y1, 2000)

    # 向上滑动
    def swipe_up(self):
        y1, x, y2, x = self.swipe_portrait()
        self.driver.swipe(x, y1, x, y2)

    # 向下滑动
    def swipe_down(self):
        y1, x, y2, x = self.swipe_portrait()
        self.driver.swipe(x, y2, x, y1)

    # 查找ID
    def element_id(self, by_id):
        element = self.driver.find_element_by_id(by_id)
        return element

    # 原生定位
    def android_toma(self, text, name):
        uiautomator = 'new UiSelector().className("' + text + '").text("' + name + '")'
        toma = self.driver.find_element_by_android_uiautomator(uiautomator)
        return toma

    # xpath定位
    def element_xpath(self, by_xpath):
        element = self.driver.find_element_by_xpath(by_xpath)
        return element

    # text定位
    def by_text(self, by_text, acd=None):
        element = self.driver.find_element_by_link_text(by_text)
        return element

    # 登录流程
    def login(self, user, paw):
        self.element_click(self.android_toma('android.widget.TextView', '账号'))
        self.element_click(self.element_id('cn.com.open.mooc:id/header_line'))
        time.sleep(2)
        self.element_click(self.element_id('cn.com.open.mooc:id/tvPassLogin'))
        self.element_send(self.element_id('cn.com.open.mooc:id/accountEditChannel2'), user)
        self.element_send(self.element_id('cn.com.open.mooc:id/passwordEditChannel2'), paw)
        self.element_click(self.element_id('cn.com.open.mooc:id/login'))

    # 切换句柄
    def handle(self):
        self.element_click(self.android_toma('android.widget.TextView', '发现'))
        self.element_click(self.android_toma('android.widget.TextView', '想要开挂进阶Java架构师？这份超强（长）学习计划单 请签收！'))
        # webview = self.driver.context
        # print(webview)
        # self.element_click(self.android_toma('android.view.View', '关注'))
        time.sleep(6)
        self.element_click(self.element_id('author_header'))
        time.sleep(6)
        self.element_click(self.element_id('cn.com.open.mooc:id/iv_back'))
        time.sleep(6)
        self.element_click(self.element_id('cn.com.open.mooc:id/iv_close'))

    # 定位提示信息
    def get_tost(self):
        tost_element = ('xpath', '//*[contains(@text, "操作频繁")]')
        print(wdw(self.driver, 10, 1).until(EC.presence_of_element_located(tost_element)))


if __name__ == '__main__':
    Slide = Slide()
    # Slide.get_tost()
    Slide.login('18771917218', 'laobalaoma7272')


# contains:包含
# Slide.element_xpath('//*[contains(@text,"我的学习")]')
# Slide.element_xpath('//android.widget.TextView[@text="我的学习"]')
# /.. 上一层   ；   preceding-sibling::+(兄弟节点)
