from util.read_ini import ReadIni
from util.base_driver import BaseDriver


# 字符串分割定位方式工具类
class FindElement:

    def __init__(self, i):
        self.driver = BaseDriver().android_driver(i)

    def get_element(self, key, text=None):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        if len(data.split('>')) > 2:
            text = data.split('>')[2]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'xpath':
                return self.driver.find_element_by_xpath(value)
            elif by == 'className':
                return self.driver.find_element_by_class_name(value)
            elif by == 'uiautomator':
                uiautomator = 'new UiSelector().className("' + value + '").text("' + text + '")'
                return self.driver.find_element_by_android_uiautomator(uiautomator)
        except:
            return None

