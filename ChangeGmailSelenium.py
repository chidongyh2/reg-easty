
import random
import time
#from selenium import webdriver
from urllib.request import urlopen
from colored import fg, bg, attr  # pip install colored
import os
import random, string
from seleniumwire import webdriver
# import undetected_chromedriver as uc
class ChangeGmailSelenium:
    ref = None
    driver = None
    def __init__(self, index: str, data: str, runType: str, hiddenBrowser, changeInfoMail, changePassword, changePasswordType, password, changeMail, changeMailType, mailKP):
        super().__init__()
        self.data = data.split("|")
        self.runType = runType
        self.hiddenBrowser = hiddenBrowser
        self.changeInfoMail = changeInfoMail
        self.index = index
        self.Proxy = self.data[0]
        self.ProxyPort = self.data[1]
        self.ProxyUser = self.data[2]
        self.ProxyPassword = self.data[3]
        self.Email = self.data[4]
        self.Password = self.data[5]
        self.EmailKP = self.data[6]
        self.changeInfoMail = changeInfoMail
        self.changePassword = changePassword
        self.changePasswordType = changePasswordType
        self.newPassword = password
        self.changeMail = changeMail
        self.changeMailType = changeMailType
        self.newmailKP = mailKP

    def login(self):
        try:
            self.driver.get("https://accounts.google.com/")
            time.sleep(8)
            self.driver.find_element('xpath', '//input[@type="email"]').send_keys(self.Email)
            try:
                    self.driver.find_element('xpath', '//*[@id="identifierNext"]').click()
            except:
                pass

            time.sleep(8)
            self.driver.find_element('xpath', '//input[@type="password"]').send_keys(self.Password)
            try:
                    self.driver.find_element('xpath','//*[@id="passwordNext"]').click()
            except:
                pass
            time.sleep(15)
            try:
                if self.driver.find_element("id",'email') or self.driver.find_element("id", 'pass'):
                    return False
            except:
                return True
        except:
            return False

    def changePasswordFunc(self):
        try:
            self.driver.get("https://myaccount.google.com/signinoptions/password")
            time.sleep(8)
            self.driver.find_element('name', 'password').send_keys(self.newPassword)
            time.sleep(1)
            self.driver.find_element('name', 'confirmation_password').send_keys(self.newPassword)
            time.sleep(1)
            self.driver.find_element('xpath','/html/body/c-wiz/div/div[2]/div[2]/c-wiz/div/div[4]/form/div/div[2]/div/div/button').click()
            time.sleep(15)
            try:
                if  self.driver.find_element("name", 'password'):
                    return False
            except:
                return True
        except:
            return False

    def changeMailFunc(self):
        try:
            self.driver.get("https://myaccount.google.com/recovery/email")
            time.sleep(8)
            self.driver.find_element('id', 'i5').send_keys(self.newmailKP)
            try:
                    self.driver.find_element('xpath', '/html/body/c-wiz/div/div[2]/div[2]/c-wiz/div[1]/div[4]/div/form/div/div[2]/div[2]').click()
            except:
                pass
            time.sleep(15)
            try:
                if self.driver.find_element('id', 'i5'):
                    return False
            except:
                return True
        except:
            return False

    def randomword(self, length):
        letters = string.ascii_lowercase
        return str(''.join(random.choice(letters) for i in range(length))).upper()
            
    def run(self):
        options = webdriver.ChromeOptions()
        #self.__SetProxy(options)
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
        time.sleep(3)
        checkLogin = self.login()
        changePassWord = False
        changeMail = False
        if checkLogin == True:
            self.ref.show.emit(self.index, 26, f"Login gmail thành công")
            if self.changePassword == True:
                changePassWord = self.changePasswordFunc()
                if changePassWord == True:
                    self.ref.show.emit(self.index, 26, f"Login gmail thành công")    

            if self.changeMail == True:
                changeMail = self.changeMailFunc()
                if changeMail == True:
                    self.ref.show.emit(self.index, 26, f"Login gmail thành công")    

            self.ref.checksuccess.emit(True, self.index, f"{changePassWord}|{changeMail}")  

        if checkLogin == False:
            self.ref.show.emit(self.index, 26, f"Login gmail thất bại")
            self.ref.checksuccess.emit(False, self.index, "register")  
        #protected account
        time.sleep(1)
        if self.hiddenBrowser == True:
            self.driver.quit()