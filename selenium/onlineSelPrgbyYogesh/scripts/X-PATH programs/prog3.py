#relative path catagories examples

from selenium import webdriver
from onlineSelPrg.setting import chromepath,actiTimeUrl
import time


class Actitime:
    def Relpath(self):
        driver=webdriver.Chrome(executable_path=chromepath)
        driver.get(url=actiTimeUrl)
        driver.maximize_window()
        print(driver.title)
        UserRef='//input[@placeholder="Username"]'
        PassRef='//input[@type="password"][@placeholder="Password"]'
        PassRef = '//input[@class="textField pwdfield"]'
        loginRef="//a[@id='loginButton']"
        driver.find_element_by_xpath(UserRef).send_keys("admin")
        driver.find_element_by_xpath(PassRef).send_keys("manager")
        driver.find_element_by_xpath(loginRef).click()
        time.sleep(2)
        print(driver.title)
        driver.close()
obj=Actitime()
obj.Relpath()