import os.path
from configparser import ConfigParser
from selenium import webdriver
from framework.logger import Logger

logger=Logger(logger="BrowserEngine").getlog()

class BrowserEngine(object):
    dir=os.path.dirname(os.path.abspath('.'))
    chrome_driver_path=dir+"/tools/chromedriver.exe"
    ie_driver_path=dir+"/tools/IBDriver.exe"
    firefox_driver_path=dir+"/tools/geckodriver.exe"


    def open_browser(self):#启动浏览器

        config = ConfigParser()  # 读取config文件
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        browser = config.get("browserType", "browserName")
        print(browser)
        # config=ConfigParser()#读取config文件
        url = config.get('testServer', 'URL')
        print(url)
        browser = config.get("browserType", "browserName")
        print(browser)
        config = ConfigParser()
        # 获取配置文件路径
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)

        browser = config.get("browserType", "browserName")
        url = config.get('testServer', 'URL')
        print(url)
        # browser = config.get("browserType", "browserName")
        print(browser)



        logger.info("读取浏览器")
        url = config.get("testServer","URL")
        logger.info('找到URL：%s'%url)
        if browser=="Firefox":
            self.driver=webdriver.Firefox(self.firefox_driver_path)
            logger.info("火狐")
        elif browser=="Chrome":
             self.driver=webdriver.Chrome(self.chrome_driver_path)
             logger.info("谷歌")
        else:
            self.driver=webdriver.Ie(self.ie_driver_path)
            logger.info("IE")


        self.driver.get(url)
        logger.info("打开浏览器%s"%url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(9)
        return self.driver
    def quit_browser(self):
        logger.info("关闭")
        self.driver.quit()


