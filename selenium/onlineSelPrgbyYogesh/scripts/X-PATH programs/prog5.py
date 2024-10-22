from selenium import webdriver
from onlineSelPrg.setting import flipUrl,chromepath
import time

class Flipkart:
    def Search(self):
        driver=webdriver.Chrome(executable_path=chromepath)
        driver.get(url=flipUrl)
        driver.maximize_window()
        print(driver.title)
        closeBut='//button[@class="_2AkmmA _29YdH8"]'
        Ref='//input[@placeholder="Search for products, brands and more"]'
        driver.find_element_by_xpath(closeBut).click()
        driver.find_element_by_xpath(Ref).send_keys("trimmer")
        time.sleep(2)
        print(driver.title)
        driver.close()


    def LogIn(self):
        driver = webdriver.Chrome(executable_path=chromepath)
        driver.get(url=flipUrl)
        driver.maximize_window()
        print(driver.title)
        Email='//input[@class="_2zrpKA _1dBPDZ"]'
        pasRef='//input[@type="password"]'
        loginRef='//button[@class="_2AkmmA _1LctnI _7UHT_c"]'
        loginRef = '//div[@class="_2VTdOs _1_qmw3"]'
        driver.find_element_by_xpath(Email).send_keys('sarthak786sachan11@gmail.com')
        driver.find_element_by_xpath(pasRef).send_keys('sarthak@123')
        # driver.find_element_by_xpath(loginRef).click()
        driver.find_element_by_xpath(loginRef).submit()
        time.sleep(2)
        print(driver.title)
        driver.close()

obj=Flipkart()
# obj.Search()
obj.LogIn()
