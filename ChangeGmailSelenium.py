
import random
import time
from selenium import webdriver
from urllib.request import urlopen
from colored import fg, bg, attr  # pip install colored
import os
import random, string
#from seleniumwire import webdriver
import requests
# import undetected_chromedriver as uc
class ChangeGmailSelenium:
    ref = None
    driver = None
    def __init__(self, index: str, proxyType: str, proxyKey: str, data: str, runType: str, hiddenBrowser, changeInfoMail, changePassword, changePasswordType, password, changeMail, changeMailType, mailKP):
        super().__init__()
        self.proxyType = proxyType
        self.proxyKey = proxyKey
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
        self.FirstName = self.data[7]
        self.LastName = self.data[8]
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
                try:
                    if self.driver.find_element("xpath", '//*[@id="headingText"]/span').text == "Verify it’s you":
                        try:
                            if self.driver.find_element("xpath", '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/section/div/div/div/ul/li[4]'):
                                self.driver.find_element("xpath", '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/section/div/div/div/ul/li[3]').click()
                                time.sleep(5)
                                self.driver.find_element('id', 'knowledge-preregistered-email-response').send_keys(self.EmailKP)
                                time.sleep(1)
                                self.driver.find_element('xpath', '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
                                time.sleep(8)
                                try:
                                    if self.driver.find_element('id', 'knowledge-preregistered-email-response'):
                                        return False
                                except:
                                    return True
                        except: pass # case có cả fone
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
            self.driver.find_element('id', 'i5').clear()
            time.sleep(1)
            self.driver.find_element('id', 'i5').send_keys(self.newmailKP)
            time.sleep(2)
            try:
                    self.driver.find_element('xpath', '/html/body/c-wiz/div/div[2]/div[2]/c-wiz/div[1]/div[4]/div/form/div/div[2]/div[2]').click()
            except:
                pass
            time.sleep(15)
            try:
                if self.driver.find_element('xpath', '//*[@id="yDmH0d"]/div[13]/div[2]/div/div[2]/div[2]/button'):
                    return True
            except:
                return False
        except:
            return False

    def changeMailInfo(self):
        #change name
        try:
            self.driver.get("https://myaccount.google.com/profile/name")
            time.sleep(8)
            main_page = self.driver.current_window_handle
            try:
                self.driver.switch_to.frame(self.driver.find_element("name", "callout"))
                time.sleep(1)
                if self.driver.find_element('xpath','/html/body/div/c-wiz/div/div/c-wiz/div/div/div[1]/button'):
                    self.driver.find_element('xpath','/html/body/div/c-wiz/div/div/c-wiz/div/div/div[1]/button').click()
                    self.driver.switch_to.window(main_page)
            except:pass
            self.driver.find_element('xpath','/html/body/c-wiz/div/div[2]/div[2]/c-wiz/div[2]/div/div/div[1]/div[1]/div[2]/button').click()
            time.sleep(3)
            try:
                self.driver.switch_to.frame(self.driver.find_element("name", "callout"))
                time.sleep(1)
                if self.driver.find_element('xpath','/html/body/div/c-wiz/div/div/c-wiz/div/div/div[1]/button'):
                    self.driver.find_element('xpath','/html/body/div/c-wiz/div/div/c-wiz/div/div/div[1]/button').click()
                    self.driver.switch_to.window(main_page)
                    time.sleep(2)
            except:pass
            self.driver.find_element('xpath','/html/body/c-wiz/div/div[2]/div[2]/c-wiz/div[2]/div/div/span[1]/div/div/label/input').clear()
            self.driver.find_element('xpath','/html/body/c-wiz/div/div[2]/div[2]/c-wiz/div[2]/div/div/span[2]/div/div/label/input').clear()
            self.driver.find_element('xpath','/html/body/c-wiz/div/div[2]/div[2]/c-wiz/div[2]/div/div/span[1]/div/div/label/input').send_keys(self.FirstName)
            self.driver.find_element('xpath','/html/body/c-wiz/div/div[2]/div[2]/c-wiz/div[2]/div/div/span[2]/div/div/label/input').send_keys(self.LastName)
            time.sleep(3)
            self.driver.find_element('xpath',"/html/body/c-wiz/div/div[2]/div[2]/c-wiz/div[2]/div/div/div[3]/div[2]/div/div/button").click()
            time.sleep(10)
            txt = self.driver.find_element('xpath', '/html/body/c-wiz/div/div[2]/div[2]/c-wiz/div[2]/div/div/div[1]/div[1]/div[1]/div[2]').text
            if txt == f"{self.FirstName} {self.LastName}":
                return True
            else:
                return False
        except:
            return False
        
    def randomword(self, length):
        letters = string.ascii_lowercase
        return str(''.join(random.choice(letters) for i in range(length))).upper()

    def GetProxy(self):
        print("self.proxyType", self.proxyType)
        if self.proxyType == "Tinsoft":
            while True:
                ip = requests.get(f"http://proxy.tinsoftsv.com/api/changeProxy.php?key={self.proxyKey}&location=0").json()
                print(ip)
                if ip["success"]:
                    return ip["proxy"]
                else:
                    if "wrong key!" in str(ip):
                        return "KEYEXPIRED"
                    for ll in range(ip["next_change"], -1, -1):
                        time.sleep(1) 
        elif self.proxyType == "TMProxy":
            while True:
                ip = requests.post(f"https://tmproxy.com/api/proxy/get-new-proxy", data='{"api_key": "%s","id_location": 0}'%self.proxyKey).json()
                if ip["code"] == 0:
                    return ip["data"]["https"]
                elif ip["code"] == 6:
                    return "KEYEXPIRED"
                else:  
                    for ll in range(ip["data"]["next_request"], -1, -1):
                        time.sleep(1)
        elif self.proxyType == "ShopLike":
            while True:
                ip = requests.get(f"http://proxy.shoplike.vn/Api/getNewProxy?access_token={self.proxyKey}&location=&provider=").json()
                print(ip)
                if ip["status"] == "success":
                    return ip["data"]["proxy"]
                else:  
                    if "Key khong ton tai hoac da het han" in str(ip):
                        return "KEYEXPIRED"
                    if "Het proxy, thu lai sau" in str(ip):
                        for t in range(60, -1, -1):
                            time.sleep(1)
                        continue
                    for ll in range(int(ip["nextChange"]), -1, -1):
                        time.sleep(1)
            
    def run(self):
        options = webdriver.ChromeOptions()
        #self.__SetProxy(options)
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches",["enable logging"])
        options.add_experimental_option("excludeSwitches", ["enable automation"])
        ip = self.GetProxy()
        options.add_argument(f"--proxy-server={ip}")
        self.driver = webdriver.Chrome(options=options)
        time.sleep(3)
        checkLogin = self.login()
        changePassWord = False
        changeMail = False
        if checkLogin == True:
            self.ref.show.emit(self.index, 6, f"Login gmail thành công")
            if self.changeInfoMail == True:
                changeinfo = self.changeMailInfo()
                if changeinfo == False:
                    self.ref.show.emit(self.index, 6, f"Change info mail thất bại vui Lòng kiểm tra lại !")
                else:
                    self.ref.show.emit(self.index, 6, f"Change info mail thành công !")
            if self.changePassword == True:
                changePassWord = self.changePasswordFunc()
                if changePassWord == True:
                    self.ref.show.emit(self.index, 6, f"Change pass thành công")    

            if self.changeMail == True:
                changeMail = self.changeMailFunc()
                if changeMail == True:
                    self.ref.show.emit(self.index, 6, f"Change gmail thành công")    

            self.ref.checksuccess.emit(True, self.index, f"{str(changePassWord)}|{str(changeMail)}")  
        else:
            self.ref.show.emit(self.index, 6, f"Login gmail thất bại")
            self.ref.checksuccess.emit(False, self.index, "register")  
        self.ref.checksuccess.emit(True, self.index, f"True|{str(changeMail)}")  
        #protected account
        time.sleep(1)
        if self.hiddenBrowser == True:
            self.driver.quit()