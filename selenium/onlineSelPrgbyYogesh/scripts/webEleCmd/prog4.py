from selenium import webdriver
from onlineSelPrg.setting import chromepath,actiTimeUrl

def webEleText1():
    driver=webdriver.Chrome(executable_path=chromepath)
    driver.maximize_window()
    driver.get(url=actiTimeUrl)
    webEleRef=driver.find_element_by_id("username")
    result=webEleRef.text
    print('text of the link is', result)
    driver.close()
# webEleText1()

def webEleText2():
    driver=webdriver.Chrome(executable_path=chromepath)
    driver.maximize_window()
    driver.get(url=actiTimeUrl)
    webEleRef=driver.find_element_by_partial_link_text('Forgot your')
    result=webEleRef.text
    print('text of the link is', result)
    driver.close()
# webEleText2()


def webEleTagname1():
    driver=webdriver.Chrome(executable_path=chromepath)
    driver.maximize_window()
    driver.get(url=actiTimeUrl)
    webEleRef=driver.find_element_by_partial_link_text('Forgot your')
    result=webEleRef.tag_name
    print('text of the link is', result)
    driver.close()
webEleTagname1()

def webEleTagname2():
    driver=webdriver.Chrome(executable_path=chromepath)
    driver.maximize_window()
    driver.get(url=actiTimeUrl)
    webEleRef=driver.find_element_by_id("username")
    result=webEleRef.tag_name
    print('text of the link is', result)
    driver.close()
# webEleTagname2()