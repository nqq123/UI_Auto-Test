from testsuites.base_testcase import  base_testcase
from pageobjects.tiezi_indexpage import *
import time
import unittest

class test_tiezi_search1(base_testcase):
   def test_tiezi(self):
      index=IndexPage(self.driver)
      # index.get("http://127.0.0.1/forum.php")
      index.Login("admin","admin")
      time.sleep(5)
      fatie=FaTie(self.driver)
      fatie.fatie("nbjefnvos","gvwesdvd")
      time.sleep(5)
      huitie=HuiTie(self.driver)
      huitie.huitie("dbeWB")
      time.sleep(10)

      logout=TuiChu(self.driver)
      logout.tuichu()


if __name__=="__main__":
   # html_report = r"e:\Discuz\report\result.html"
   # fp = open(html_report, 'wb')
   # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="测试报告", description="用例执行情况")
   # runner.run(unittest.main())
   unittest.main()
