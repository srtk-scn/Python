from selenium import webdriver
from onlineSelPrg.setting import chromepath,actiTimeUrl
import time

def webEleIsDisplayed():
    driver=webdriver.Chrome(executable_path=chromepath)
    driver.maximize_window()
    driver.get(url=actiTimeUrl)
    time.sleep(4)
    webEleRef=driver.find_element_by_link_text("Forgot your password?")
    print(webEleRef)
    if webEleRef.is_displayed():
        print("web element is displayed")
    else:
        print('web element is not displayed')
    driver.close()
# webEleIsDisplayed()

def verification():
    driver = webdriver.Chrome(executable_path=chromepath)
    driver.maximize_window()
    driver.get(url=actiTimeUrl)
    time.sleep(4)
    webEleRef = driver.find_element_by_id("keepLoggedInCheckBox")
    # result=webEleRef.is_enabled()
    # result = webEleRef.is_displayed()
    result = webEleRef.is_selected()
    if result:
        print('web element is displayed/enabled/selected')
    else:
        print('web element is not displayed/enabled/selected')
    time.sleep(5)
    driver.close()
# verification()

def webEleIsEnabled():
    driver=webdriver.Chrome(executable_path=chromepath)
    driver.maximize_window()
    driver.get(r"C:\Users\sarthak sachan\PycharmProjects\online_selenium\onlineSelPrg\scripts\index.html")
    time.sleep(4)
    webEleRef=driver.find_element_by_css_selector("input[type='text']")
    print(webEleRef)
    if webEleRef.is_displayed():
        print("web element is displayed")
    else:
        print('web element is not displayed')
    driver.close()
webEleIsEnabled()