from selenium import webdriver
from onlineSelPrg.setting import chromepath,actiTimeUrl
import time

def elementAttri():
    driver=webdriver.Chrome(executable_path=chromepath)
    driver.maximize_window()
    driver.get(url=actiTimeUrl)
    webRefUsernameTF=driver.find_element_by_id('username')
    attrName="placeholder"
    attrValue=webRefUsernameTF.get_attribute(attrName)
    print(attrName,"==",attrValue)
    driver.close()
# elementAttri()


def elementLocSIzeReact():
    driver=webdriver.Chrome(executable_path=chromepath)
    driver.maximize_window()
    driver.get(url=actiTimeUrl)
    webRefUsernameTF=driver.find_element_by_id('username')
    result=webRefUsernameTF.location      #{'x': 729, 'y': 283}
    result2=webRefUsernameTF.size        #{'height': 32, 'width': 214}
    result3=webRefUsernameTF.rect       #{'height': 32, 'width': 214, 'x': 729.2000122070312, 'y': 283.3999938964844}
    print(result, type(result))
    print(result.get("y"))
    print(result["x"])
    print(result2)
    print(result3)
# elementLocSIzeReact()


def elementCSSattrValue():
    driver=webdriver.Chrome(executable_path=chromepath)
    driver.maximize_window()
    driver.get(url=actiTimeUrl)
    webRefUsernameTF = driver.find_element_by_id('username')
    result=webRefUsernameTF.value_of_css_property("padding-bottom")
    print("result" , result)
elementCSSattrValue()



