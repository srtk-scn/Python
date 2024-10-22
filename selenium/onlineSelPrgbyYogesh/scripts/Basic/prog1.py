from selenium import webdriver
from onlineSelPrg.setting import chromepath,actiTimeUrl
import time

def enterAndClick():
    driver=webdriver.Chrome(executable_path=chromepath)
    driver.maximize_window()
    driver.get(actiTimeUrl)
    time.sleep(4)
    # webEleRef= driver.find_element_by_id('username')
    # webEleRef.send_keys("admin")
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_css_selector("input.textField.textField.pwdfield").send_keys("manager")
    print("username and password enterned")
    time.sleep(4)
    driver.find_element_by_css_selector("a#loginButton").click()
    time.sleep(2)
    driver.close()
# enterAndClick()

def EnterAndClick():
    driver = webdriver.Chrome(executable_path=chromepath)
    driver.maximize_window()
    driver.get(url="https://www.google.com/")
    time.sleep(4)
    driver.find_element_by_name("q").send_keys("python")
    time.sleep(2)
    # webEleRef=driver.find_element_by_css_selector("ul[role='listbox'] li")
    webEleRef = driver.find_elements_by_css_selector("ul[role='listbox'] li")
    print(webEleRef)
    print(type(webEleRef),"........", len(webEleRef))
    driver.close()
EnterAndClick()