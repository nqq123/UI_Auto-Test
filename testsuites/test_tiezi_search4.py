from testsuites.base_testcase import  base_testcase
from pageobjects.tiezi_indexpage import *
import time
import unittest

class test_tiezi_search4(base_testcase):
   def test_tiezi(self):
      pu = PutongLogin(self.driver)
      pu.putongfun("123456", "123456")
      time.sleep(5)

      tp=Tp(self.driver)
      tp.tp("bkjbdkbk","bkjhkh","hkhkhkhh")
      time.sleep(5)
