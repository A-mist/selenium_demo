'''
    关键字驱动类
'''
import time

from selenium import webdriver


def oppen_browser(type_):
    try:
        driver = getattr(webdriver, type_)()
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver


class Key:
    # 构造函数
    def __init__(self, type_):
        self.driver = oppen_browser(type_)
        self.driver.implicitly_wait(5)

    # 访问url
    def oppen(self, url):
        self.driver.get(url)

    # 定位元素
    def locate(self, name, value):
        return self.driver.find_element(name, value)

    # 点击
    def click(self, name, value):
        self.locate(name, value).click()

    # 输入
    def input(self, name, value, txt):
        self.locate(name, value).send_keys(txt)

    # 强制等待
    def sleep(self, time_):
        time.sleep(time_)

    # 释放浏览器
    def quit(self):
        self.driver.quit()

    #