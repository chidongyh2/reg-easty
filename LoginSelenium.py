
import random
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import pickle
from urllib.request import urlopen
from colored import fg, bg, attr  # pip install colored
from selenium_authenticated_proxy import SeleniumAuthenticatedProxy
import os
import random, string, datetime
import pathlib
# import undetected_chromedriver as uc
class LoginSelenium:
    ref = None
    driver = None
    def __init__(self, index: str, data):
        super().__init__()
        self.data = data.split("|")
        self.index = index
        self.Proxy = self.data[0]
        self.ProxyPort = self.data[1]
        self.ProxyUser = self.data[2]
        self.ProxyPassword = self.data[3]
        self.Email = self.data[4]
        self.Password = self.data[5]
        self.FirstName = self.data[6]
        self.LastName = self.data[7]
        self.SSN = self.data[8]  #ma số định danh
        self.DL = self.data[9]  #driver licence nunber
        self.Address = self.data[10]
        self.City = self.data[11]
        self.State = self.data[12] # mã quốc gia
        self.ZipCode = self.data[13] # mã quốc gia
        self.Phone = self.data[14] # ngày tháng năm sinh
        self.Dob = self.data[15] # mã routing thẻ 
        self.ACHRouting = self.data[16] # mã routing thẻ 
        self.BankAccount = self.data[17] # Mã ngân hàng
        self.CardNumber = self.data[18] # Mã thẻ
        self.CardExpiredDay = self.data[19]
        self.CardExpiredMoth = self.data[20]
        self.CardCCV = self.data[21] # mã vissa
        #self.CardName = self.data[23] # Name of Card
        try:self.Status = self.data[22] # Trạng thái
        except:pass
        try:self.CreatedDate = self.data[23] # Created Date
        except:pass
        
    def login(self):
        try:
            self.driver.get("https://accounts.google.com/")
            time.sleep(5)
            self.driver.find_element('xpath', '//input[@type="email"]').send_keys(self.Email)
            try:
                    self.driver.find_element('xpath', '//*[@id="identifierNext"]').click()
            except:
                pass

            time.sleep(5)
            self.driver.find_element('xpath', '//input[@type="password"]').send_keys(self.Password)
            try:
                    self.driver.find_element('xpath','//*[@id="passwordNext"]').click()
            except:
                pass
            time.sleep(5)
            try:
                if self.driver.find_element("id",'email') or self.driver.find_element("id", 'pass'):
                    return False
            except:
                return True
        except:
            return False
    
    def loginEasty(self):
        try:
            self.driver.get("https://www.etsy.com/")
            time.sleep(3)
            try:
                main_page = self.driver.current_window_handle
    
                self.driver.find_element('xpath','/html/body/div[2]/header/div[4]/nav/ul/li[1]/button').click()
                time.sleep(8)
                try:
                    self.driver.find_element('xpath','//*[@id="join-neu-form"]/div[3]/div[1]/div/button').click()
                except:
                    self.driver.find_element('xpath','/html/body/main/div/div/div/div/div[2]/form/div[3]/div[1]/div/button').click()
                #popup sso google
                # changing the handles to access login page
                for handle in self.driver.window_handles:
                    if handle != main_page:
                        login_page = handle
                # change the control to signin page        
                self.driver.switch_to.window(login_page)
                mail =  self.driver.find_element('xpath','//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]/div')
                mail.click()
                time.sleep(6)
                # change control to main page
                self.driver.switch_to.window(main_page)
                return True
            except:
                return False
        except:
            return False

    def __SetProxy(self, options):
        try:
            # Initialize SeleniumAuthenticatedProxy
            proxy_helper = SeleniumAuthenticatedProxy(proxy_url=f"http://{self.ProxyUser}:{self.ProxyPassword}@{self.Proxy}:{self.ProxyPort}")
            proxy_helper.enrich_chrome_options(options)
        except:
            self.ref.show.emit(self.index, 22, f"Lỗi proxy")

    def get_cookies(self):
        self.driver.get('https://www.google.com')
        time.sleep(1)
        return self.driver.get_cookies()
    
    def openEsty(self):
        options = webdriver.ChromeOptions()
        self.__SetProxy(options)
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches",["enable logging"])
        options.add_experimental_option("excludeSwitches", ["enable automation"])
        options.add_argument("--disable-popup-blocking")
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        options.add_experimental_option("prefs",prefs)
        self.driver = webdriver.Chrome(options=options)
        #self.driver.delete_all_cookies()
        time.sleep(3)
    
    def run(self):
        options = webdriver.ChromeOptions()
        self.__SetProxy(options)
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches",["enable logging"])
        options.add_experimental_option("excludeSwitches", ["enable automation"])
        options.add_argument("--disable-popup-blocking")
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        options.add_experimental_option("prefs",prefs)
        self.driver = webdriver.Chrome(options=options)
        #self.driver.delete_all_cookies()
        time.sleep(3)
        checkLogin = self.login()
        if checkLogin == True:
            self.loginEasty()
