from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time
class IndexPage(BasePage):

    index_page_username=(By.NAME,'username')
    index_page_pwd=(By.NAME,'password')
    index_page_login=(By.CSS_SELECTOR,'button em')

    def Login(self,username,pwd):
        self.sendkeys(username,*self.index_page_username)
        self.sendkeys(pwd,*self.index_page_pwd)
        self.click(*self.index_page_login)
#发帖部分
class FaTie(BasePage):
    fatie_page_button = (By.ID, "newspecial")  # 发帖
    index_page_mrbk = (By.CSS_SELECTOR, '.fl_icn a')  # 默认版块
    fatie_page_title =(By.NAME,'subject')#标题
    iframe=(By.TAG_NAME,'iframe')
    fatie_page_content=(By.TAG_NAME,'body')#发帖内容
    fabiao_button=(By.NAME,'topicsubmit')

    def fatie(self,title,content):
        self.jh()
        self.click(*self.index_page_mrbk)
        self.jh()
        self.click(*self.fatie_page_button)
        self.jh()
        self.sendkeys(title,*self.fatie_page_title)
        self.switch_to(*self.iframe)
        self.sendkeys(content,*self.fatie_page_content)
        self.jh()
        self.click(*self.fabiao_button)
#回帖部分
class HuiTie(BasePage):
    huitie_button=(By.ID,'post_reply')
    huitie_content=(By.ID,'postmessage')
    huitie_fabiao=(By.ID,'postsubmit')#发表回复
    def huitie(self,text):
        self.click(*self.huitie_button)
        self.sendkeys(text,*self.huitie_content)
        self.jh()
        self.click(*self.huitie_fabiao)
#删除部分
class Delete(BasePage):
    delete_page_mrbk=(By.CSS_SELECTOR,".fl_icn a")
    delete_but=(By.CSS_SELECTOR,".o input")#前面方块
    delete_but1=(By.LINK_TEXT,"删除")
    delete_but2=(By.ID,"modsubmit")

    def delete(self):
         self.jh()
         self.click(*self.delete_page_mrbk)
         self.click(*self.delete_but)
         self.click(*self.delete_but1)
         self.click(*self.delete_but2)

#退出部分
class TuiChu(BasePage):
    tuichu_button=(By.LINK_TEXT,'退出')
    def tuichu(self):
        self.jh()
        self.click(*self.tuichu_button)

#管理中心
class GuanLi(BasePage):
    guanlizhongxin=(By.LINK_TEXT,"管理中心")
    luntan=(By.LINK_TEXT,"论坛")
    xinbankuai=(By.LINK_TEXT,"添加新版块")
    mingchen=(By.NAME,"newforum[1][]")
    tijiao=(By.ID,"submit_editsubmit")
    zdsy = (By.LINK_TEXT, "站点首页")
    tc=(By.LINK_TEXT,"退出")

    def guanli(self,text):
        time.sleep(5)
        self.click(*self.guanlizhongxin)
        self.chang_window()
        time.sleep(6)
        self.click(*self.luntan)
        self.iframe()
        self.click(*self.xinbankuai)
        self.sendkeys(text, *self.mingchen)
        self.click(*self.tijiao)
        self.chang_window()
        self.click(*self.zdsy)
        self.chang_window()
        self.click(*self.tc)
#普通用户登陆
class Putong(BasePage):
    yhm=(By.ID,"ls_username")
    mm=(By.NAME,"password")
    index_page_login = (By.CSS_SELECTOR, 'button em')
    aaa = (By.LINK_TEXT, "在线等李白")

    def putong(self,name,pwd):
        self.sendkeys(name,*self.yhm)
        self.sendkeys(pwd,*self.mm)
        self.click(*self.index_page_login)
        self.click(*self.aaa)
        self.jh()
class Ft(BasePage):
    ft_page_button = (By.ID, "newspecial")  # 发帖
    ft_page_title =(By.NAME,'subject')#标题
    iframe=(By.TAG_NAME,'iframe')
    ft_page_content=(By.TAG_NAME,'body')#发帖内容
    fabiao_button=(By.NAME,'topicsubmit')

    def ft(self,title,content):
        self.jh()

        self.click(*self.ft_page_button)
        self.jh()
        self.sendkeys(title,*self.ft_page_title)
        self.switch_to(*self.iframe)
        self.sendkeys(content,*self.ft_page_content)
        self.jh()
        self.click(*self.fabiao_button)
#回帖部分
class Ht(BasePage):
    ht_button=(By.ID,'post_reply')
    ht_content=(By.ID,'postmessage')
    ht_fabiao=(By.ID,'postsubmit')#发表回复
    def ht(self,text):
        self.click(*self.ht_button)
        self.sendkeys(text,*self.ht_content)
        self.jh()
        self.click(*self.ht_fabiao)

class PutongLogin(BasePage):
    yhm=(By.ID,"ls_username")
    mm=(By.NAME,"password")
    index_page_login = (By.CSS_SELECTOR, 'button em')


    def putongfun(self,name,pwd):
        self.sendkeys(name,*self.yhm)
        self.sendkeys(pwd,*self.mm)
        self.click(*self.index_page_login)
        self.jh()

#搜索帖子
class Tz(BasePage):
    sstz=(By.ID,"scbar_txt")
    ss=(By.CSS_SELECTOR,".scbar_btn_td button")
    lb=(By.CSS_SELECTOR,".xs3 a")

    def tz(self,text):
        self.click(*self.sstz)
        self.sendkeys(text,*self.sstz)
        self.click(*self.ss)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.click(*self.lb)
        self.driver.switch_to.window(self.driver.window_handles[2])
#发起投票
class Tp(BasePage):
    fatie_page_button = (By.ID, "newspecial")  # 发帖
    index_page_mrbk = (By.CSS_SELECTOR, '.fl_icn a')  # 默认版块
    fqtp_button=(By.LINK_TEXT,"发起投票")
    ssk=(By.ID,"subject")
    kk1=(By.XPATH,"//*[@id='pollm_c_1']/p[1]/input")
    KK2=(By.XPATH,"//*[@id='pollm_c_1']/p[2]/input")
    fqtp_button2=(By.ID,"postsubmit")
    tp_button1=(By.ID,"option_1")
    tp_button2=(By.ID,"pollsubmit")
    zhuti=(By.ID,"thread_subject")
    xuanxianag1=(By.XPATH,'//label[@for="option_1"]')
    xuanxianag2= (By.XPATH, '//label[@for="option_2"]')
    bili1=(By.CSS_SELECTOR,".pcht :nth-child(4) :nth-child(2)")
    bili2=(By.CSS_SELECTOR,".pcht :nth-child(2) :nth-child(2)")

    def tp(self,title1,content1,content2):
        self.jh()
        self.click(*self.index_page_mrbk)
        self.jh()
        self.click(*self.fatie_page_button)
        self.click(*self.fqtp_button)
        self.jh()
        self.sendkeys(title1,*self.ssk)
        self.sendkeys(content1, *self.kk1)
        self.sendkeys(content2, *self.KK2)
        self.click(*self.fqtp_button2)
        self.jh()
        self.click(*self.tp_button1)
        self.click(*self.tp_button2)
        zt=self.text(*self.zhuti)
        xx1=self.text(*self.xuanxianag1)
        xx2=self.text(*self.xuanxianag2)
        bl1=self.text(*self.bili1)
        bl2=self.text(*self.bili2)

        print("主题名称：",zt,"选项:",xx1,xx2,"比例：",bl1,bl2)





