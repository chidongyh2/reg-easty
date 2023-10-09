
import random
import time
#from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pickle
from urllib.request import urlopen
from colored import fg, bg, attr  # pip install colored
from selenium_authenticated_proxy import SeleniumAuthenticatedProxy
import os
import random, string, datetime
from seleniumwire import webdriver
# import undetected_chromedriver as uc
class VerifyBankSelenium:
    ref = None
    driver = None
    def __init__(self, index: str, data: str, hiddenBrowser = False, code = None):
        super().__init__()
        self.hiddenBrowser = hiddenBrowser
        self.code = code
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
            time.sleep(8)
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
            time.sleep(5)
            try:
                main_page = self.driver.current_window_handle
    
                self.driver.find_element('xpath','/html/body/div[2]/header/div[4]/nav/ul/li[1]/button').click()
                time.sleep(15)
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
                time.sleep(15)
                # change control to main page
                self.driver.switch_to.window(main_page)
                return True
            except:
                return False
        except:
            return False

    def verifyBank(self):
        self.driver.get("https://www.etsy.com/your/shops/me/onboarding/payments")
        time.sleep(5)
        try:
            #check passs if name created
            self.driver.find_element('xpath','//*[@id="content"]/div[3]/div[4]/div/div[1]/button').click()
            time.sleep(3)
            self.driver.find_element('xpath','//*[@id="content"]/div[3]/div[4]/div/div[1]/button').click()
            time.sleep(3)
            self.driver.find_element('xpath','//*[@id="content"]/div[3]/div[3]/div/div[1]/div/a[1]').click()
            time.sleep(3)
            time.sleep(1)
            self.driver.find_element('xpath','//*[@id="content"]/div[3]/div[4]/div/div[1]/button').click()
            time.sleep(5)
        except:
            pass
        try:
            self.driver.execute_script("window.scrollTo(0, 800)")
            #enter deposit code
            if self.driver.find_element('xpath','//*[@id="content"]/div[16]/div/div/div[2]/div[7]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[2]/p/button'):
                self.driver.find_element('xpath','//*[@id="content"]/div[16]/div/div/div[2]/div[7]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div[2]/p/button').click()
                time.sleep(2)
                self.driver.switch_to.frame(self.driver.find_element("id", "plaid-link-iframe-1"))
                self.driver.find_element('id','nonce-input').send_keys(self.code)
                time.sleep(2)
                self.driver.find_element('id','aut-button-button_one_tap').click()
                time.sleep(5)
        except:
            pass
        try:
            #setup billing
            self.driver.find_element('xpath','/html/body/div[6]/div/div[1]/div/button').click()
            time.sleep(1)
            self.driver.find_element('id','billing-cc-num').send_keys(self.CardNumber)
            month = Select(self.driver.find_element('xpath','//*[@id="content"]/div[2]/div/div/div[6]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div[1]/div[5]/div[1]/div/select'))
            month.select_by_value(str(int(self.CardExpiredDay)))
            year = Select(self.driver.find_element('xpath','//*[@id="content"]/div[2]/div/div/div[6]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div[1]/div[5]/div[2]/div/select'))
            year.select_by_value(f"20{str(self.CardExpiredMoth)}") 
            self.driver.find_element('id','billing-cc-ccv').send_keys(self.CardCCV)
            self.driver.find_element('id','billing-name').send_keys(f"{self.FirstName} {self.LastName}")
            country2 = Select(self.driver.find_element('xpath','//*[@id="content"]/div[2]/div/div/div[6]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div[1]/select'))
            country2.select_by_visible_text("United States") 
            address = self.driver.find_element('xpath','//*[@id="content"]/div[2]/div/div/div[6]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div[2]/div[3]/div/input')
            address.send_keys(self.Address)
            zipCode = self.driver.find_element('xpath','//*[@id="content"]/div[2]/div/div/div[6]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div[2]/div[5]/div[1]/input')
            zipCode.send_keys(self.ZipCode)
            city = self.driver.find_element('xpath','//*[@id="content"]/div[2]/div/div/div[6]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div[2]/div[5]/div[2]/input')
            city.send_keys(self.City)
            state = Select(self.driver.find_element('xpath','//*[@id="content"]/div[2]/div/div/div[6]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div[2]/div[6]/div/div/div[1]/select'))
            state.select_by_value(self.State)
            phoneCode = self.driver.find_element('xpath','//*[@id="content"]/div[2]/div/div/div[6]/div[2]/div[2]/div[1]/div/div/div/div/div/div/div[2]/div[7]/div/input')
            phoneCode.send_keys(self.Phone)
            time.sleep(1)
            self.driver.find_element('xpath','//*[@id="content"]/div[3]/div[4]/div/div[1]/button').click()
            time.sleep(5)
        except:
            pass

        try:
            self.driver.find_element('xpath','//*[@id="content"]/div[2]/div/div/div[7]/div/div/div[1]/div/div/div/div/div/button').click()
            time.sleep(3)
            self.driver.find_element('xpath','//*[@id="content"]/div[2]/div/div/div[7]/div/div/div[1]/div/div/div/div/div/div/div/div/button[3]').click()
            self.driver.find_element('xpath','//*[@id="content"]/div[2]/div/div/div[7]/div/div/div[2]/div/div[1]/button').click()
            return True
        except:pass

    def randomword(self, length):
        letters = string.ascii_lowercase
        return str(''.join(random.choice(letters) for i in range(length))).upper()


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
    
    def run(self):
        options = webdriver.ChromeOptions()
        self.__SetProxy(options)
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches",["enable logging"])
        options.add_experimental_option("excludeSwitches", ["enable automation"])
        options_seleniumWire = {
            'proxy': {
                'https': f'https://{self.ProxyUser}:{self.ProxyPassword}@{self.Proxy}:{self.ProxyPort}',
                'http': f'http://{self.ProxyUser}:{self.ProxyPassword}@{self.Proxy}:{self.ProxyPort}',
                'verify_ssl': False,
            }
        }
        self.driver = webdriver.Chrome(options=options, seleniumwire_options=options_seleniumWire)
        #self.driver.delete_all_cookies()
        time.sleep(5)
        checkLogin = self.login() 
        if checkLogin == True:
            self.ref.show.emit(self.index, 19, f"Login gmail thành công")
            loginEasty = self.loginEasty()
            if loginEasty == True:
                self.ref.show.emit(self.index, 19, f"Login easty thành công")
                time.sleep(5)
                verify = self.verifyBank()
                if verify == True:
                    self.ref.show.emit(self.index, 19, f"Verify Bank success !")
                    self.ref.checksuccess.emit(True, self.index, "verify")
                else: 
                    self.ref.show.emit(self.index, 19, f"Verify Bank error !")
                    self.ref.checksuccess.emit(False, self.index, "verify")
            else:
                self.ref.show.emit(self.index, 19, f"Login easty lỗi")
                self.ref.checksuccess.emit(False, self.index, "verify")

        if checkLogin == False:
            self.ref.show.emit(self.index, 19, f"Login gmail thất bại")
            self.ref.checksuccess.emit(False, self.index, "verify")
        time.sleep(10)
        if self.hiddenBrowser == True:
            self.driver.quit()