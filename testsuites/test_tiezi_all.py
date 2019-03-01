import unittest
import HTMLTestRunner
import os
from testsuites.test_tiezi_search import  test_tiezi_search1
from testsuites.test_tiezi_search2 import test_tiezi_search2
from testsuites.test_tiezi_search3 import test_tiezi_search3
from testsuites.test_tiezi_search4 import test_tiezi_search4




#设置报告文件保存路径
dir=os.path.dirname(os.path.realpath(__file__))
reporter_path=os.path.join(dir,"reporter")
if not os.path.exists(reporter_path): os.mkdir(reporter_path)

#构造测试套件
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(test_tiezi_search1))
suite.addTest(unittest.makeSuite(test_tiezi_search2))
suite.addTest(unittest.makeSuite(test_tiezi_search3))
suite.addTest(unittest.makeSuite(test_tiezi_search4))



if __name__=="__main__":

    #打开一个文件夹，将result写入此file中
    html_reporter=reporter_path+r'\result.html'
    fp=open(html_reporter,"wb")
    #初始化一个HTMLTestRunner实例对象，用来生成报告
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试报告",description="用例实例情况")
    runner.run(suite)


