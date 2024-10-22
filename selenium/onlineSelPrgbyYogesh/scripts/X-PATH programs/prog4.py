#relative path catagories examples

from selenium import webdriver
from onlineSelPrg.setting import chromepath,actiTimeUrl,demoshop
import time


class Demo:
    def DemoSearchRelpath(self):
        driver=webdriver.Chrome(executable_path=chromepath)
        driver.get(url=demoshop)
        driver.maximize_window()
        print(driver.title)
        searchBoxRef='//input[@id="small-searchterms"]'
        searchBtnRef='//input[@value="Search"]'
        driver.find_element_by_xpath(searchBoxRef).send_keys("books")
        driver.find_element_by_xpath(searchBtnRef).click()

        time.sleep(2)
        print(driver.title)
        driver.close()

    def DemoLoginRelpath(self):
        driver = webdriver.Chrome(executable_path=chromepath)
        driver.get(url='http://demowebshop.tricentis.com/login')
        driver.maximize_window()
        print(driver.title)
        emailRef='//input[@name="Email"]'
        PassRaf='//input[@name="Password"]'
        loginRef='//input[@value="Log in"]'
        driver.find_element_by_xpath(emailRef).send_keys("sarthak786sachan11@gmail.com")
        driver.find_element_by_xpath(PassRaf).send_keys("Sss@123")
        time.sleep(2)
        driver.find_element_by_xpath(loginRef).click()
        time.sleep(2)
        print(driver.title)

obj=Demo()
# obj.DemoSearchRelpath()
obj.DemoLoginRelpath()