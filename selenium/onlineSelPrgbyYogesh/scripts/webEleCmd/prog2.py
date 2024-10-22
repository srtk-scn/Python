from selenium import webdriver
from onlineSelPrg.setting import chromepath,actiTimeUrl
import time

def webEleCLear():
    driver=webdriver.Chrome(executable_path=chromepath)
    driver.maximize_window()
    driver.get(actiTimeUrl)
    time.sleep(2)
    webEleRef=driver.find_element_by_css_selector("input#username")
    webEleRef.send_keys("admin")
    time.sleep(4)
    webEleRef.clear()
    time.sleep(3)
    driver.close()
# webEleCLear()

def webEleSubmit():
    driver = webdriver.Chrome(executable_path=chromepath)
    driver.maximize_window()
    driver.get(actiTimeUrl)
    time.sleep(2)
    driver.find_element_by_css_selector("input#username").send_keys("sarthak786sachan11@gmail.com")
    print("username enterened")
    driver.find_element_by_css_selector("input.textField.pwdfield").send_keys("sarthak@123")
    print("password enterened")
    time.sleep(4)
    driver.find_element_by_css_selector("a#loginButton").submit()         #submit button should be in form
    time.sleep(3)
    driver.close()
# webEleSubmit()

def webEleSubmitF():
    driver = webdriver.Chrome(executable_path=chromepath)
    driver.maximize_window()
    driver.get(url="https://www.flipkart.com/account/login?ret=/")
    time.sleep(2)
    driver.find_element_by_css_selector("input[class='input[class='_2zrpKA _1dBPDZ']").send_keys("7011785707")
    print("username enterened")
    driver.find_element_by_css_selector("input[class='_2zrpKA _3v41xv _1dBPDZ']").send_keys("sarthak@123")
    print("password enterened")
    time.sleep(4)
    driver.find_element_by_css_selector("button[class='_2AkmmA _1LctnI _7UHT_c']").submit()         #submit button should be in form
    time.sleep(3)
    driver.close()
webEleSubmitF()
