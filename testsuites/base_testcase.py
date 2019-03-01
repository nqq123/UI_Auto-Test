import unittest
from selenium import webdriver
from framework.browser_engine import BrowserEngine


class base_testcase(unittest.TestCase):
    def setUp(self):
        self.browserengine=BrowserEngine()
        self.driver = self.browserengine.open_browser()

        # self.driver=webdriver.Chrome("../tools/chromedriver.exe")
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(5)

    def tearDown(self):
        self.browserengine.quit_browser()
        print("结束")
