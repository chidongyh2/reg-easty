
import random
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pickle
from urllib.request import urlopen
from colored import fg, bg, attr  # pip install colored
from selenium_authenticated_proxy import SeleniumAuthenticatedProxy
import os
# import undetected_chromedriver as uc
class GmailSelenium:
    ref = None
    driver = None
    def __init__(self, index: str, data: str):
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
        self.Phone = self.data[10]
        self.Address = self.data[11]
        self.City = self.data[12]
        self.ZipCode = self.data[13] # mã quốc gia
        self.Dob = self.data[14] # ngày tháng năm sinh
        self.ACHRouting = self.data[15] # mã routing thẻ 
        self.BankAccount = self.data[16] # Mã ngân hàng
        self.CardNumber = self.data[17] # Mã thẻ
        self.CardExpiredDay = self.data[18]
        self.CardExpiredMoth = self.data[18]
        self.CardCCV = self.data[19] # mã vissa
        self.CardName = self.data[20] # Name of Card
        try:self.Status = self.data[21] # Trạng thái
        except:pass
        try:self.CreatedDate = self.data[22] # Created Date
        except:pass
        
    def login(self):
        try:
            self.driver.get("https://accounts.google.com/")
            time.sleep(3)
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
            time.sleep(2)
            try:
                main_page = self.driver.current_window_handle

                self.driver.find_element('xpath','/html/body/div[2]/header/div[4]/nav/ul/li[1]/button').click()
                time.sleep(2)
                print('pass', )
                self.driver.find_element('xpath','//*[@id="join-neu-form"]/div[3]/div[1]/div/button').click()
                print('pass', )
                time.sleep(2)
                #popup sso google
                # changing the handles to access login page
                for handle in self.driver.window_handles:
                    if handle != main_page:
                        login_page = handle
                # change the control to signin page        
                self.driver.switch_to.window(login_page)
                mail =  self.driver.find_element('xpath','//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]/div')
                mail.click()
                time.sleep(5)
                # change control to main page
                self.driver.switch_to.window(main_page)
                return True
            except:
                return False
        except:
            return False

    def registerShopEasty(self):
        self.driver.get("https://www.etsy.com/your/shops/y5ffeazxftjipy4t/onboarding/screener/welcome")
        time.sleep(3)
        self.driver.find_element('xpath',"/html/body/main/div/div/div/div[3]/div/div[2]/div/div/a").click()
        #pass info
        try:
            time.sleep(0.5)
            self.driver.find_element('xpath',"/html/body/main/div/div/div/div[3]/div/div[2]/div/div/fieldset/div[1]/div/input").click()
            time.sleep(0.5)
            self.driver.find_element('xpath',"/html/body/main/div/div/div/div[3]/div/div[2]/div/div/div/div/a[1]").click()
            time.sleep(0.5)
            self.driver.find_element('xpath',"/html/body/main/div/div/div/div[3]/div/div[2]/div/div/fieldset/div/div[1]/div").click()
            time.sleep(0.5)
            self.driver.find_element('xpath',"/html/body/main/div/div/div/div[3]/div/div[2]/div/div/fieldset/div/div[2]/div").click()
            time.sleep(0.5)
            self.driver.find_element('xpath',"/html/body/main/div/div/div/div[3]/div/div[2]/div/div/div/div/a[2]").click()
        except:
            pass
        #pass info
        try:
            self.driver.get("https://www.etsy.com/your/shops/me/onboarding/preferences")
            time.sleep(0.5)
            self.driver.find_element('xpath',"/html/body/div[4]/div[3]/div[4]/div/div[1]/button").click()
            time.sleep(0.5)
            # enter name

            nameShop = self.driver.find_element('xpath',"/html/body/div[4]/div[2]/div/div/div[3]/div/div/div[2]/div/div/input")
            nameShop.send_keys(f"{self.FirstName} {self.LastName} Shop")
            self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[3]/div/div[1]/div/div/div[2]/button[2]").click()
            #stock your photo shop
            uploadImages = self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/form/input[2]")
            uploadImages.send_keys(os.getcwd() + "/tests/sample_files/Figure1.tif")
            time.sleep(1)
            titleShop = self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/form/input[2]")
            titleShop.send_keys(f"{self.FirstName} {self.LastName} Shop")
            
            #options select
            select1 = Select(self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[6]/div[4]/div/div/fieldset/div[2]/div/div[1]/div/div/div/select"))
            select1.select_by_index(2)         
            select1 = Select(self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[6]/div[4]/div/div/fieldset/div[2]/div/div[2]/div/div/div/select"))
            select1.select_by_index(2)          
            select1 = Select(self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[6]/div[4]/div/div/fieldset/div[2]/div/div[3]/div/div/div/select"))
            select1.select_by_index(2)  
            #xem lại không đúng
            category = self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[6]/div[11]/div/div/div/div/div/div[2]/div/div/div/input")
            category.send_keys(f"Fashion, Souvenir, Modern, Trending")

            descriptionShop = self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[6]/div[18]/div/div/div/div[2]/div[1]/div/textarea")
            descriptionShop.send_keys(f"{self.FirstName} {self.LastName} Shop")

            price = self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[8]/div/div/div/div[1]/div/div[1]/div/div/div/div[3]/div/div[1]/div/div[1]/input")
            price.send_keys(15)

            zipCode = self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[12]/div/div/div[1]/div/div/div[1]/div[3]/div/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div/div[1]/input")
            zipCode.send_keys(self.ZipCode)

            processTime = Select(self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[12]/div/div/div[1]/div/div/div[1]/div[3]/div/div[2]/div[1]/div[2]/div/div[1]/div[3]/div/div[2]/div/div[1]/select"))
            processTime.select_by_index(2)  

            #height uweight
            weight1 = self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[12]/div/div/div[2]/div/div[1]/div/fieldset/div[2]/div/div[1]/div/input")
            weight1.send_keys(self.ZipCode)
            weight2 = self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[12]/div/div/div[2]/div/div[1]/div/fieldset/div[2]/div/div[2]/div/input")
            weight2.send_keys(self.ZipCode)
            height1 = self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[12]/div/div/div[2]/div/div[2]/div/fieldset/div[2]/div/div[1]/div/input")
            height1.send_keys(random.randrange(80, 100))
            height2 = self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[12]/div/div/div[2]/div/div[2]/div/fieldset/div[2]/div/div[2]/div/input")
            weight2.send_keys(random.randrange(50, 80))
            height3 = self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[12]/div/div/div[2]/div/div[2]/div/fieldset/div[2]/div/div[3]/div/input")
            height3.send_keys(random.randrange(120, 160))
            self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[3]/div/div[1]/div/div/div[2]/button[2]").click()
            time.sleep(5)
        except:
            pass

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
        self.driver = webdriver.Chrome(options=options)
        #self.driver.delete_all_cookies()
        time.sleep(3)
        checkLogin = self.login() 
        if checkLogin == True:
            self.ref.show.emit(self.index, 18, f"Login gmail thành công")
            loginEasty = self.loginEasty()
            if loginEasty == True:
                self.ref.show.emit(self.index, 18, f"Login easty thành công")
                registerShop = self.registerShopEasty()
            else:
                self.ref.show.emit(self.index, 18, f"Login easty thành công")
            #self.ref.checksuccess.emit(True, self.index, self.mail, self.password)
            

        if checkLogin == False:
            self.ref.show.emit(self.index, 18, f"Login gmail thất bại")
            #self.ref.checksuccess.emit(False, self.index, self.mail, self.password)  
        #protected account
        self.driver.quit()
