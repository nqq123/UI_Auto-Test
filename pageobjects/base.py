import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC
from framework.logger import Logger
logger=Logger(logger="BasePage").getlog()#参数 logger="BasePage"
class BasePage(object):
    def __init__(self,driver):
        self.driver=driver
    def back(self):
        self.driver.back()
    def forward(self):
        self.driver.forward()
    def get(self,url):
        self.driver.get(url)
    def quit_browser(self):
        pass
    def find_element(self,*loc):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
        return self.driver.find_element(*loc)
    def sendkeys(self,text,*loc):
        e1=self.find_element(*loc)
        e1.clear()
        e1.send_keys(text)
    def click(self,*loc):
        e1=self.find_element(*loc)
        e1.click()
    def clear(self,*element):
        e1=self.find_element(*element)
        e1.click()
    def closed(self):
        self.driver.quit()
    def jh(self):
        self.driver.switch_to.window(self.driver.current_window_handle)
    def switch_to(self,*element):
        e1=self.find_element(*element)
        self.driver.switch_to.frame(e1)
    def chang_window(self):
        window_list=self.driver.window_handles
        self.driver.switch_to.window(window_list[len(window_list)-1])

    def iframe(self):
        self.driver.switch_to.frame(0)

    def text(self,*element):
        e1 = self.find_element(*element)
        return e1.text
