
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
class GmailSelenium:
    ref = None
    driver = None
    def __init__(self, index: str, data: str, hiddenBrowser = False, changeInfoMail = False):
        super().__init__()
        self.data = data.split("|")
        self.hiddenBrowser = hiddenBrowser
        self.changeInfoMail = changeInfoMail
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
    
    def changeMailInfo(self):
        #change name
        try:
            self.driver.get("https://myaccount.google.com/profile/name")
            time.sleep(3)
            self.driver.find_element('xpath','/html/body/c-wiz/div/div[2]/div[2]/c-wiz/div[2]/div/div/div[1]/div[1]/div[2]/button').click()
            time.sleep(3)
            self.driver.find_element('xpath','/html/body/c-wiz/div/div[2]/div[2]/c-wiz/div[2]/div/div/span[1]/div/div/label/input').clear()
            self.driver.find_element('xpath','/html/body/c-wiz/div/div[2]/div[2]/c-wiz/div[2]/div/div/span[2]/div/div/label/input').clear()
            self.driver.find_element('xpath','/html/body/c-wiz/div/div[2]/div[2]/c-wiz/div[2]/div/div/span[1]/div/div/label/input').send_keys(self.FirstName)
            self.driver.find_element('xpath','/html/body/c-wiz/div/div[2]/div[2]/c-wiz/div[2]/div/div/span[2]/div/div/label/input').send_keys(self.LastName)
            self.driver.find_element('xpath',"/html/body/c-wiz/div/div[2]/div[2]/c-wiz/div[2]/div/div/div[3]/div[2]/div/div/button").click()
            time.sleep(2)
            txt = self.driver.find_element('xpath', '/html/body/c-wiz/div/div[2]/div[2]/c-wiz/div[2]/div/div/div[1]/div[1]/div[1]/div[2]').text
            if txt == f"{self.FirstName} {self.LastName}":
                return True
            else:
                return False
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

    def randomword(self, length):
        letters = string.ascii_lowercase
        return str(''.join(random.choice(letters) for i in range(length))).upper()

    def registerShopEasty(self):
        self.driver.get("https://www.etsy.com/your/shops/me/onboarding/preferences")
        time.sleep(3)
        try:
            #check passs if name created
            self.driver.find_element('xpath','/html/body/div[4]/div[3]/div[4]/div/div[1]/button').click()
            time.sleep(3)
            self.driver.find_element('xpath','//*[@id="content"]/div[3]/div[4]/div/div[1]/button').click()
            time.sleep(3)
            self.driver.find_element('xpath','/html/body/div[4]/div[3]/div[3]/div/div[1]/div/a[1]').click()
            time.sleep(3)
        except:
            pass
        #pass welcom
        try:
            self.driver.find_element('xpath','/html/body/main/div/div/div/div[3]/div/div[2]/div/div/a').click()
            time.sleep(3)
        except:
            pass
        #pass info
        try:
            self.driver.execute_script("arguments[0].click();", self.driver.find_element('id',"getting_started"))
            time.sleep(3)
            self.driver.find_element('xpath',"/html/body/main/div/div/div/div[3]/div/div[2]/div/div/div/div/a[1]").click()
            time.sleep(2)
            self.driver.find_element('xpath',"/html/body/main/div/div/div/div[3]/div/div[2]/div/div/fieldset/div/div[1]/div").click()
            time.sleep(2)
            self.driver.find_element('xpath',"/html/body/main/div/div/div/div[3]/div/div[2]/div/div/fieldset/div/div[2]/div").click()
            time.sleep(2)
            self.driver.find_element('xpath',"/html/body/main/div/div/div/div[3]/div/div[2]/div/div/div/div/a[2]").click()
            time.sleep(3)
        except:
            print("error get started")
            pass
        time.sleep(3)
        #start your shop
        try:
            self.driver.find_element('xpath',"/html/body/main/div/div/div/div[3]/div/div[2]/div/div/div/a").click()
            time.sleep(3)
        except:
            print("error start your shop")
            pass
        time.sleep(3)   
        try:
            self.driver.find_element('xpath',"/html/body/div[4]/div[3]/div[4]/div/div[1]/button").click()
            time.sleep(3)
        except:
            print("error start your shop 2")
            pass

        #pass info
        try:
            nameShop = self.driver.find_element('id',"onboarding-shop-name-input")
            nameShop.send_keys(f"{self.LastName}{self.randomword(3)}")
            time.sleep(2)
            self.driver.find_element('xpath','//*[@id="content"]/div[3]/div[4]/div/div[1]/button').click()
            time.sleep(2)
        except:
            print("error pass name")
            pass

        #pass bank info first
       #pass bank info
        try:
            if self.driver.find_element('xpath',"/html/body/div[4]/div[16]/div/div/div[2]/div[3]/div/div/div[1]/div/h5").text.strip() == "Getting paid on Etsy":
                time.sleep(2)
                #select country
                country1 = Select(self.driver.find_element('xpath',"/html/body/div[4]/div[16]/div/div/div[2]/div[3]/div/div/div[2]/div[3]/select"))
                country1.select_by_visible_text("United States") 
                country2 = Select(self.driver.find_element('xpath',"/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/div[2]/div[2]/div/select"))
                country2.select_by_visible_text("United States") 
                
                fistName = self.driver.find_element('xpath',"/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/div[3]/div[2]/div/input")
                fistName.send_keys(self.FirstName)
                lastName = self.driver.find_element('xpath',"/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/div[4]/div[2]/div/input")
                lastName.send_keys(self.LastName)
                date = None
                try:
                    if len(self.Dob) == 4:
                        date = datetime.date(int(f"19{self.Dob[2:4]}" if int(self.Dob[2:4]) > 30 else f"20{self.Dob[2:4]}"), int(self.Dob[:1]), int(self.Dob[1:2]))
                    if len(self.Dob) == 5:         
                        date = datetime.date(int(f"19{self.Dob[3:5]}" if int(self.Dob[3:5]) > 30 else f"20{self.Dob[3:5]}"),  int(self.Dob[:1]), int(self.Dob[1:3]))
                    if len(self.Dob) == 6:         
                        date = datetime.date(int(f"19{self.Dob[4:6]}" if int(self.Dob[4:6]) > 30 else f"20{self.Dob[4:6]}"), int(self.Dob[:2]), int(self.Dob[2:4]))
                except:
                    return False
                month = Select(self.driver.find_element('xpath',"/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/fieldset[1]/div[2]/div[1]/select"))
                month.select_by_value(str(date.month))
                day = Select(self.driver.find_element('xpath',"/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/fieldset[1]/div[2]/div[2]/select"))
                day.select_by_value(str(date.day) if len(str(date.day)) > 1 else f"0{str(date.day)}") 
                year = Select(self.driver.find_element('xpath',"/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/fieldset[1]/div[2]/div[3]/select"))
                year.select_by_value(str(date.year)) 
            
                ssn = self.driver.find_element('id','identity-individual-ssn')
                ssn.send_keys(self.SSN)
                #stress
                time.sleep(1)
                number = self.driver.find_element('xpath','/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/fieldset[2]/div/div[2]/div[2]/div[1]/input')
                number.send_keys(self.Phone)
                address = self.driver.find_element('xpath','/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/fieldset[2]/div/div[2]/div[2]/div[2]/input')
                address.send_keys(self.Address)
                address2 = self.driver.find_element('xpath','/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/fieldset[2]/div/div[2]/div[3]/div/input')
                address2.send_keys(self.Address)
                zipCode = self.driver.find_element('xpath',"/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/fieldset[2]/div/div[2]/div[4]/div[1]/input")
                zipCode.send_keys(self.ZipCode)
                time.sleep(1)
                city = self.driver.find_element('xpath',"/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/fieldset[2]/div/div[2]/div[4]/div[2]/input")
                city.send_keys(self.City)
                print(self.State)
                state = Select(self.driver.find_element('xpath',"/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/fieldset[2]/div/div[2]/div[5]/div/div/div[1]/select"))
                state.select_by_value(str(self.State).upper())
                time.sleep(1)
                phoneCode = self.driver.find_element('xpath','/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/fieldset[2]/div/div[2]/div[6]/div/input')
                phoneCode.send_keys(self.Phone)
                try:
                    self.driver.execute_script("arguments[0].click();", self.driver.find_element('id','dg-radios-neu__radio-2--small'))
                    time.sleep(3)
                    print('passs radio')
                except: pass
                try:
                    if self.driver.find_element('xpath','//*[@id="questions-overlay"]/div[2]'):
                        self.driver.find_element('xpath','/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/h5').click()
                except:pass
                self.driver.execute_script("window.scrollTo(0, 1800)")
                t = 0
                while t <= 3:
                    t += 1
                    time.sleep(2)
                    try:
                        self.driver.find_element('xpath','//*[@id="plaid-render-wrapper"]/button').click()
                        try:
                            if self.driver.find_element('xpath','//*[@id="questions-overlay"]/div[2]'):
                                self.driver.find_element('xpath','/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/h5').click()
                        except:pass
                    except:
                        pass
                time.sleep(10)
                try:
                    if self.driver.find_element('xpath','//*[@id="questions-overlay"]/div[2]'):
                        self.driver.find_element('xpath','/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/h5').click()
                except:pass
                time.sleep(3)
                self.driver.switch_to.frame(self.driver.find_element("id", "plaid-link-iframe-3"))
                time.sleep(5)
                self.driver.find_element('id','aut-button').click()
                #pass info bank
                try:
                    time.sleep(3)
                    print("dzo hgere")
                    try:
                        #add bank manual
                        self.driver.execute_script("arguments[0].click();", self.driver.find_element('id','flow-type-manual'))
                        self.driver.find_element('id','aut-button').click()
                    except:pass
                    time.sleep(3)
                    #Routing
                    self.driver.find_element('id','device-input').send_keys(self.ACHRouting)
                    self.driver.find_element('id','aut-button').click()
                    time.sleep(3)
                    #Account Number
                    self.driver.find_element('id','account-number-input').send_keys(self.BankAccount)
                    self.driver.find_element('id','account-number-confirmation').send_keys(self.BankAccount)
                    self.driver.find_element('id','aut-button').click()
                    time.sleep(3)
                    #Enter name
                    self.driver.find_element('id','name-input').send_keys(f"{self.FirstName} {self.LastName}")
                    self.driver.find_element('id','aut-button').click()
                    time.sleep(3)
                    #checking
                    self.driver.execute_script("arguments[0].click();", self.driver.find_element('id','account-type-checking'))
                    self.driver.find_element('id','aut-button').click()
                    time.sleep(3)
                    #checking
                    self.driver.find_element('id','aut-button').click()
                    time.sleep(3)
                    self.driver.find_element('id','aut-button').click()
                    time.sleep(5)
                except:pass
                #end bank infoo
                try:
                    self.driver.find_element('xpath','/html/body/reach-portal/div[3]/div/div/div/div[1]/div/span/main/div[2]/button').click()
                    time.sleep(3)
                except:pass
                try:
                    if self.driver.find_element('xpath','//*[@id="questions-overlay"]/div[2]'):
                        self.driver.find_element('xpath','/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/h5').click()
                except:pass
                try:
                    self.driver.find_element('xpath','/html/body/reach-portal/div[3]/div/div/div/div[1]/div/span/main/div[2]/button').click()
                    time.sleep(3)
                except:pass
                try:
                    time.sleep(3)  
                    self.driver.find_element('xpath','/html/body/div[6]/div/div[1]/div/button').click()
                except:pass
                time.sleep(3)
        except:
            print("except info first")
            pass
        # stock your photo shop
        try:
            #stock your photo shop
            uploadImages = self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/form/input[2]")
            #print('uploadImages')
            #random images 
            images = os.listdir('source-images')
            imageName = images[random.randrange(0, len(images))]
            imagePath = fr"{os.getcwd()}\source-images\{imageName}"
            uploadImages.send_keys(imagePath)
            time.sleep(1)
            titleShop = self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[6]/div[2]/div/div/div/div[2]/div/div/input")
            titleShop.send_keys(f"{self.FirstName} {self.LastName} Shop")
            print('pass titile')
            #options select
            select1 = Select(self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[6]/div[4]/div/div/fieldset/div[2]/div/div[1]/div/div/div/select"))
            select1.select_by_index(2)     
            time.sleep(1)    
            select1 = Select(self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[6]/div[4]/div/div/fieldset/div[2]/div/div[2]/div/div/div/select"))
            select1.select_by_index(2) 
            time.sleep(1)         
            select1 = Select(self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[6]/div[4]/div/div/fieldset/div[2]/div/div[3]/div/div/div/select"))
            select1.select_by_index(2)  
            time.sleep(1)
            print('pass select suggestion')
            #xem lại không đúng
            category = self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[6]/div[11]/div/div/div/div/div/div[2]/div/div/div/input")
            category.click()
            category.send_keys(f"Fashion")
            time.sleep(4)
            self.driver.find_element('xpath', "/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[6]/div[11]/div/div/div/div/div[1]/div[2]/div/div[2]/div/ul").click()
            #
            print('pass categories')
            descriptionShop = self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[6]/div[18]/div/div/div/div[2]/div[1]/div/textarea")
            descriptionShop.send_keys(f"{self.FirstName} {self.LastName} Shop")
            print('pass descriptionShop')
            time.sleep(1)
            try:
                self.driver.execute_script("arguments[0].click();", self.driver.find_element('id','unlinked-profile'))
            except:
                pass
                    
            price = self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[8]/div/div/div/div[1]/div/div[1]/div/div/div/div[3]/div/div[1]/div/div[1]/input")
            price.send_keys(random.randrange(10, 50))
            time.sleep(1)
            #shipping
            shippingPrice = Select(self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[12]/div/div/div[1]/div/div/div[1]/div[3]/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/select"))
            shippingPrice.select_by_index(1) 
            time.sleep(1.5)
            zipCode = self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[12]/div/div/div[1]/div/div/div[1]/div[3]/div/div[2]/div/div[2]/div/div[1]/div[3]/div[2]/div/div[1]/input")
            zipCode.click()
            zipCode.send_keys(self.ZipCode)
            time.sleep(1)
            processTime = Select(self.driver.find_element('id',"processing_time_select"))
            processTime.select_by_index(3) 
            shipping1 = Select(self.driver.find_element('id',"consolidated_shipping_service_0"))
            shipping1.select_by_index(2) 
            shipping2 = Select(self.driver.find_element('id',"consolidated_shipping_service_1"))
            shipping2.select_by_index(2) 
            #self.driver.execute_script("arguments[0].click();", self.driver.find_element('xpath','/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[12]/div/div/div[1]/div/div/div[1]/div[3]/div/div[2]/div/div[2]/div/div[1]/div[5]/div/div[2]/div[1]/label/input'))
            #height uweight
            weight1 = self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[12]/div/div/div[2]/div/div[1]/div/fieldset/div[2]/div/div[1]/div/input")
            weight1.send_keys(random.randrange(80, 100))
            height1 = self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[12]/div/div/div[2]/div/div[2]/div/fieldset/div[2]/div/div[1]/div/input")
            height1.send_keys(random.randrange(1200, 1800))
            height2 = self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[12]/div/div/div[2]/div/div[2]/div/fieldset/div[2]/div/div[2]/div/input")
            height2.send_keys(random.randrange(50, 80))
            height3 = self.driver.find_element('xpath',"/html/body/div[4]/div[2]/section/div/div[4]/div/div/div/div[2]/div/div/div/div[12]/div/div/div[2]/div/div[2]/div/fieldset/div[2]/div/div[3]/div/input")
            height3.send_keys(random.randrange(120, 160))
            self.driver.find_element('xpath','//*[@id="page-region"]/div/div/div[3]/div/div[1]/div/div/div[2]/button[2]').click()
            time.sleep(5)
            try:
                os.remove(imagePath)
            except: pass
            try:
                self.driver.find_element('xpath','/html/body/div[4]/div[3]/div[3]/div/div[1]/div/a[1]').click()
            except:pass
            time.sleep(2)
        except:
            print("except stock your photo shop")
            pass
        #pass bank info
        try:
            if self.driver.find_element('xpath',"/html/body/div[4]/div[16]/div/div/div[2]/div[3]/div/div/div[1]/div/h5").text.strip() == "Getting paid on Etsy":
                time.sleep(2)
                #select country
                country1 = Select(self.driver.find_element('xpath',"/html/body/div[4]/div[16]/div/div/div[2]/div[3]/div/div/div[2]/div[3]/select"))
                country1.select_by_visible_text("United States") 
                country2 = Select(self.driver.find_element('xpath',"/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/div[2]/div[2]/div/select"))
                country2.select_by_visible_text("United States") 
                
                fistName = self.driver.find_element('xpath',"/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/div[3]/div[2]/div/input")
                fistName.send_keys(self.FirstName)
                lastName = self.driver.find_element('xpath',"/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/div[4]/div[2]/div/input")
                lastName.send_keys(self.LastName)
                date = None
                try:
                    if len(self.Dob) == 4:
                        date = datetime.date(int(f"19{self.Dob[2:4]}" if int(self.Dob[2:4]) > 30 else f"20{self.Dob[2:4]}"), int(self.Dob[:1]), int(self.Dob[1:2]))
                    if len(self.Dob) == 5:         
                        date = datetime.date(int(f"19{self.Dob[3:5]}" if int(self.Dob[3:5]) > 30 else f"20{self.Dob[3:5]}"),  int(self.Dob[:1]), int(self.Dob[1:3]))
                    if len(self.Dob) == 6:         
                        date = datetime.date(int(f"19{self.Dob[4:6]}" if int(self.Dob[4:6]) > 30 else f"20{self.Dob[4:6]}"), int(self.Dob[:2]), int(self.Dob[2:4]))
                except:
                    return False
                month = Select(self.driver.find_element('xpath',"/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/fieldset[1]/div[2]/div[1]/select"))
                month.select_by_value(str(date.month))
                day = Select(self.driver.find_element('xpath',"/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/fieldset[1]/div[2]/div[2]/select"))
                day.select_by_value(str(date.day) if len(str(date.day)) > 1 else f"0{str(date.day)}") 
                year = Select(self.driver.find_element('xpath',"/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/fieldset[1]/div[2]/div[3]/select"))
                year.select_by_value(str(date.year)) 
            
                ssn = self.driver.find_element('id','identity-individual-ssn')
                ssn.send_keys(self.SSN)
                #stress
                time.sleep(1)
                number = self.driver.find_element('xpath','/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/fieldset[2]/div/div[2]/div[2]/div[1]/input')
                number.send_keys(self.Phone)
                address = self.driver.find_element('xpath','/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/fieldset[2]/div/div[2]/div[2]/div[2]/input')
                address.send_keys(self.Address)
                address2 = self.driver.find_element('xpath','/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/fieldset[2]/div/div[2]/div[3]/div/input')
                address2.send_keys(self.Address)
                zipCode = self.driver.find_element('xpath',"/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/fieldset[2]/div/div[2]/div[4]/div[1]/input")
                zipCode.send_keys(self.ZipCode)
                time.sleep(1)
                city = self.driver.find_element('xpath',"/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/fieldset[2]/div/div[2]/div[4]/div[2]/input")
                city.send_keys(self.City)
                print(self.State)
                state = Select(self.driver.find_element('xpath',"/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/fieldset[2]/div/div[2]/div[5]/div/div/div[1]/select"))
                state.select_by_value(str(self.State).upper())
                time.sleep(1)
                phoneCode = self.driver.find_element('xpath','/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/fieldset[2]/div/div[2]/div[6]/div/input')
                phoneCode.send_keys(self.Phone)
                try:
                    self.driver.execute_script("arguments[0].click();", self.driver.find_element('id','dg-radios-neu__radio-2--small'))
                    time.sleep(3)
                    print('passs radio')
                except: pass
                try:
                    if self.driver.find_element('xpath','//*[@id="questions-overlay"]/div[2]'):
                        self.driver.find_element('xpath','/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/h5').click()
                except:pass
                self.driver.execute_script("window.scrollTo(0, 1800)")
                t = 0
                while t <= 3:
                    t += 1
                    time.sleep(2)
                    try:
                        self.driver.find_element('xpath','//*[@id="plaid-render-wrapper"]/button').click()
                        try:
                            if self.driver.find_element('xpath','//*[@id="questions-overlay"]/div[2]'):
                                self.driver.find_element('xpath','/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/h5').click()
                        except:pass
                    except:
                        pass
                time.sleep(10)
                try:
                    if self.driver.find_element('xpath','//*[@id="questions-overlay"]/div[2]'):
                        self.driver.find_element('xpath','/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/h5').click()
                except:pass
                time.sleep(3)
                self.driver.switch_to.frame(self.driver.find_element("id", "plaid-link-iframe-3"))
                time.sleep(5)
                self.driver.find_element('id','aut-button').click()
                #pass info bank
                try:
                    time.sleep(3)
                    print("dzo hgere")
                    try:
                        #add bank manual
                        self.driver.execute_script("arguments[0].click();", self.driver.find_element('id','flow-type-manual'))
                        self.driver.find_element('id','aut-button').click()
                    except:pass
                    time.sleep(3)
                    #Routing
                    self.driver.find_element('id','device-input').send_keys(self.ACHRouting)
                    self.driver.find_element('id','aut-button').click()
                    time.sleep(3)
                    #Account Number
                    self.driver.find_element('id','account-number-input').send_keys(self.BankAccount)
                    self.driver.find_element('id','account-number-confirmation').send_keys(self.BankAccount)
                    self.driver.find_element('id','aut-button').click()
                    time.sleep(3)
                    #Enter name
                    self.driver.find_element('id','name-input').send_keys(f"{self.FirstName} {self.LastName}")
                    self.driver.find_element('id','aut-button').click()
                    time.sleep(3)
                    #checking
                    self.driver.execute_script("arguments[0].click();", self.driver.find_element('id','account-type-checking'))
                    self.driver.find_element('id','aut-button').click()
                    time.sleep(3)
                    #checking
                    self.driver.find_element('id','aut-button').click()
                    time.sleep(3)
                    self.driver.find_element('id','aut-button').click()
                    time.sleep(5)
                except:pass
                #end bank infoo
                try:
                    self.driver.find_element('xpath','/html/body/reach-portal/div[3]/div/div/div/div[1]/div/span/main/div[2]/button').click()
                    time.sleep(3)
                except:pass
                try:
                    if self.driver.find_element('xpath','//*[@id="questions-overlay"]/div[2]'):
                        self.driver.find_element('xpath','/html/body/div[4]/div[16]/div/div/div[2]/div[5]/div[2]/div[1]/h5').click()
                except:pass
                try:
                    self.driver.find_element('xpath','/html/body/reach-portal/div[3]/div/div/div/div[1]/div/span/main/div[2]/button').click()
                    time.sleep(3)
                except:pass
                try:
                    time.sleep(3)  
                    self.driver.find_element('xpath','/html/body/div[6]/div/div[1]/div/button').click()
                except:pass
                time.sleep(3)
        except:
            print("except info two")
            pass
        #bypass ID upload
        try:
            time.sleep(3)
            if self.driver.find_element('xpath',"/html/body/div[4]/div[15]/div/div/div/div[2]/div[2]/div/form/div[2]/h2").text.strip() == "Verify your ID":
                self.driver.execute_script("window.scrollTo(0, 1800)")
                national = Select(self.driver.find_element('xpath',"/html/body/div[4]/div[15]/div/div/div/div[2]/div[2]/div/form/div[2]/div[1]/div[1]/div/select"))
                national.select_by_visible_text("United States") 
                type = Select(self.driver.find_element('xpath',"/html/body/div[4]/div[15]/div/div/div/div[2]/div[2]/div/form/div[2]/div[1]/div[2]/div/select"))
                type.select_by_value("Passport") 
                            #stock your photo shop
                uploadImages = self.driver.find_element('name',"secure-document-attachment")
                #print('uploadImages')
                uploadImages.send_keys(os.getcwd() + f"/source-ids/{self.SSN}.png")
                time.sleep(5)
                self.driver.find_element('xpath',"/html/body/div[4]/div[15]/div/div/div/div[2]/div[2]/div/form/div[2]/div[2]/button").click()
                time.sleep(70)
                print("qua 0")
                try:
                    self.driver.find_element('xpath','/html/body/div[4]/div[17]/div/div[1]/div/button').click()
                except:pass
                time.sleep(10)
                print("qua 1 ")
                #step check radio question and continute banking (check banking)
                try:
                    self.driver.get("https://www.etsy.com/your/shops/me/onboarding/payments")
                    time.sleep(5)
                    self.driver.execute_script("window.scrollTo(0, 800)")
                    time.sleep(1)
                    try:
                        self.driver.find_element('xpath','/html/body/div[4]/div[16]/div/div/div[2]/div[7]/div[2]/div[1]/div[2]/button').click()
                    except:
                        pass
                    time.sleep(8)
                    print("today")
                    try:
                        try:
                            if self.driver.find_element("id", "plaid-link-iframe-3"):
                                self.driver.switch_to.frame(self.driver.find_element("id", "plaid-link-iframe-3"))
                        except:
                            self.driver.switch_to.frame(self.driver.find_element("id", "plaid-link-iframe-1"))
                    except:pass
                    
                    self.driver.find_element('id','aut-button').click()
                    time.sleep(1)
                    #add bank manual
                    self.driver.execute_script("arguments[0].click();", self.driver.find_element('id','flow-type-manual'))
                    self.driver.find_element('id','aut-button').click()
                    time.sleep(1)
                    #Routing
                    self.driver.find_element('id','device-input').send_keys(self.ACHRouting)
                    self.driver.find_element('id','aut-button').click()
                    time.sleep(1)
                    #Account Number
                    self.driver.find_element('id','account-number-input').send_keys(self.BankAccount)
                    self.driver.find_element('id','account-number-confirmation').send_keys(self.BankAccount)
                    self.driver.find_element('id','aut-button').click()
                    time.sleep(1)
                    #Enter name
                    self.driver.find_element('id','name-input').send_keys(f"{self.FirstName} {self.LastName}")
                    self.driver.find_element('id','aut-button').click()
                    time.sleep(1)
                    #checking
                    self.driver.execute_script("arguments[0].click();", self.driver.find_element('id','account-type-checking'))
                    self.driver.find_element('id','aut-button').click()
                    time.sleep(1)
                    #checking
                    self.driver.find_element('id','aut-button').click()
                    time.sleep(3)
                    self.driver.find_element('id','aut-button').click()
                    time.sleep(5)
                    return True
                except:
                    print("exxcep step check radio question and continute")
                    return False
        except:
            print("except bypass ID upload")
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
        options.add_argument("--disable-popup-blocking")
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        options.add_experimental_option("prefs",prefs)
        self.driver = webdriver.Chrome(options=options)
        #self.driver.delete_all_cookies()
        time.sleep(3)
        checkLogin = self.login()
        if checkLogin == True:
            self.ref.show.emit(self.index, 19, f"Login gmail thành công")
            if self.changeInfoMail == True:
                changeinfo = self.changeMailInfo()
                if changeinfo == False:
                    self.ref.show.emit(self.index, 19, f"Change info mail thất bại vui Lòng kiểm tra lại !")
                else:self.ref.show.emit(self.index, 19, f"Change info mail thành công !")
            loginEasty = self.loginEasty()
            if loginEasty == True:
                self.ref.show.emit(self.index, 19, f"Login easty thành công")
                time.sleep(5)
                registerShop = self.registerShopEasty()
                if registerShop == True:
                    self.ref.show.emit(self.index, 19, f"Đăng ký tài khoản esty thành công")
                    self.ref.show.emit(self.index, 17, datetime.datetime.now())
                    self.ref.checksuccess.emit(True, self.index, "register")

                else: 
                    self.ref.show.emit(self.index, 19, f"Đăng ký tài khoản không thành công vui lòng kiểm tra lại")
                    self.ref.checksuccess.emit(False, self.index, "register")
            else:
                self.ref.show.emit(self.index, 19, f"Login easty thất bại")
                self.ref.checksuccess.emit(False, self.index, "register")


        if checkLogin == False:
            self.ref.show.emit(self.index, 19, f"Login gmail thất bại")
            self.ref.checksuccess.emit(False, self.index, "register")  
        #protected account
        time.sleep(10)
        if self.hiddenBrowser == True:
            self.driver.quit()