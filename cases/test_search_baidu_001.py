import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.config import Config
from baseCase.base_case import BaseCase


class TestBaiDu(BaseCase):

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def setUp(self):
        self.log.error("测试输出日志")
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.driver.get(self.URL)


    def tearDown(self):
        self.driver.quit()

    def test_search_0(self):
        self.log.error("测试输出日志")
        self.driver.find_element(*self.locator_kw).send_keys('爱灵1997')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            print(link.text)



    def test_search_1(self):
        self.driver.find_element(*self.locator_kw).send_keys('Python selenium')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            print(link.text)


if __name__ == '__main__':
    unittest.main()
# ————————————————
# 版权声明：本文为CSDN博主「huilan_same」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/huilan_same/article/details/76572428
