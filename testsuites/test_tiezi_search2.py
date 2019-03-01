from testsuites.base_testcase import base_testcase
from pageobjects.tiezi_indexpage import *
import time
import unittest

class test_tiezi_search2(base_testcase):
   def test_tiezi(self):
      index=IndexPage(self.driver)
      index.Login("admin","admin")
      time.sleep(5)

      delete=Delete(self.driver)
      delete.delete()
      time.sleep(5)

      guanli=GuanLi(self.driver)
      guanli.guanli("在线等李白")
      time.sleep(5)

      putong=Putong(self.driver)
      putong.putong("123456","123456")
      time.sleep(5)

      ft = Ft(self.driver)
      ft.ft("nbjefnvos", "gvwesdvdgbkhkhkhkhhkhffytfufuo")
      time.sleep(5)
      ht = Ht(self.driver)
      ht.ht("dbeWBhiuhihhhhhhuhkhkhkk")
      time.sleep(10)



      logout = TuiChu(self.driver)
      logout.tuichu()
