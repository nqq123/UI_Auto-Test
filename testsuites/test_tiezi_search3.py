from testsuites.base_testcase import  base_testcase
from pageobjects.tiezi_indexpage import *
import time
import unittest

class test_tiezi_search3(base_testcase):
   def test_tiezi(self):


       pu = PutongLogin(self.driver)
       pu.putongfun("123456", "123456")

       time.sleep(5)

       tz=Tz(self.driver)
       tz.tz("李白")
       time.sleep(5)

       assert "李白" in self.driver.title

       logout = TuiChu(self.driver)
       logout.tuichu()