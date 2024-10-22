from selenium import webdriver
from onlineSelPrg.setting import chromepath,actiTimeUrl
driver=webdriver.Chrome(executable_path=chromepath)

import time

def usingCSS_attribute_selector():
    driver = webdriver.Chrome(executable_path=chromepath)
    driver.maximize_window()
    driver.get(actiTimeUrl)
    time.sleep(4)
    pattern1='input[name="username"]'    #attribute selector
    pattern2='input[class="textField"][placeholder="Username"]'#multiple (attribute)css selecter
    pattern3='input[class="textField"][placeholder="Username"][id="username"]' #attribute selector
    webEleRef=driver.find_element_by_css_selector(pattern3)
    print('web elemant reference is', webEleRef)
    driver.close()
# usingCSS_attribute_selector()


def usingCSS_id_selector():
    driver = webdriver.Chrome(executable_path=chromepath)
    driver.maximize_window()
    driver.get(actiTimeUrl)
    time.sleep(4)
    pattern3 = 'input#username'  # id selector
    webEleRef = driver.find_element_by_css_selector(pattern3)
    print('web elemant reference is', webEleRef)
    driver.close()
# usingCSS_id_selector()


def usingCSS_class_selector():
    driver = webdriver.Chrome(executable_path=chromepath)
    driver.maximize_window()
    driver.get(actiTimeUrl)
    time.sleep(4)
    pattern1 = 'div.atLogoImg'  # class selector
    pattern2='input.textField.pwdfield'
    webEleRef = driver.find_element_by_css_selector(pattern2)
    print('web elemant reference is', webEleRef)
    driver.close()
# usingCSS_class_selector()


def usingCSS_parentChild_selector():
    driver = webdriver.Chrome(executable_path=chromepath)
    driver.maximize_window()
    driver.get(url=r"C:\Users\sarthak sachan\PycharmProjects\online_selenium\onlineSelPrg\scripts\index.html")
    time.sleep(4)
    pattern1='ul#parent>li.webSub'
    pattern='ul#parent>li.webSub>ul>li#js'
    webEleRef = driver.find_element_by_css_selector(pattern)
    print('web elemant reference is', webEleRef)
    driver.close()
# usingCSS_parentChild_selector()


def usingCSS_Next_Sibling_selector():
    driver = webdriver.Chrome(executable_path=chromepath)
    driver.maximize_window()
    # driver.get(url=r"C:\Users\sarthak sachan\PycharmProjects\online_selenium\onlineSelPrg\scripts\index.html")
    driver.get(url=actiTimeUrl)
    time.sleep(4)
    # SYNTAXX=> element+adjacent element
    # pattern='ul#parent>li.webSub>ul>li+li'
    pattern='table.whiteBoxWithLogoTable>tbody>tr+tr'
    webEleRef = driver.find_element_by_css_selector(pattern)
    print('web elemant reference is', webEleRef)
    driver.close()
# usingCSS_Next_Sibling_selector()


def usingCSS_StringMatching_selector():
    """SYNTAXX>           example= 'PYTHON SELENIUM'
    1.  ^   match a PREFIX         ''
    2.  $   match a SUFFIX
    3.  *   match a SUBSTRING    """
    driver = webdriver.Chrome(executable_path=chromepath)
    driver.maximize_window()
    # driver.get(url=r"C:\Users\sarthak sachan\PycharmProjects\online_selenium\onlineSelPrg\scripts\index.html")
    driver.get(url=actiTimeUrl)
    time.sleep(4)
    # pattern="input[name*='username']"
    pattern="input[name$='name']"
    # pattern="input[name^='user']"
    webEleRef = driver.find_element_by_css_selector(pattern)
    print('web elemant reference is', webEleRef)
    driver.close()
# usingCSS_StringMatching_selector()


def usingCSS_specificChild_selector():
#SYNTAXX=>1.  first child             ul[name='subject'] li : first_child()
#2.          last child               ul[name='subject'] li : last_child()
#3.          nth child                ul[name='subject'] li : nth_child(n)         n= specific number
    driver = webdriver.Chrome(executable_path=chromepath)
    driver.maximize_window()
    driver.get(url=r"C:\Users\sarthak sachan\PycharmProjects\online_selenium\onlineSelPrg\scripts\index.html")
    time.sleep(4)
    # pattern="ul li:first-child"       #space is a used for all the descendends while > is used for direct one step down child
    # pattern="ul#parent>li:nth-child(2)"
    pattern="ul#parent>li:last-child"
    webEleRef = drive6r.find_element_by_css_selector(pattern)
    print('web elemant reference is', webEleRef)
    driver.close()
usingCSS_specificChild_selector()





