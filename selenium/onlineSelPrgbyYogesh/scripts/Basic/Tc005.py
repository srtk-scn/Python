from selenium import webdriver
from onlineSelPrg.setting import chromepath
driver=webdriver.Chrome(executable_path=chromepath)
from onlineSelPrg.scripts.locators import getWebElement
def IdLoc():
    locName = "id"
    value = "username"
    print('before web element')
    webEleRef = getWebElement(locName, value)
    print(webEleRef)
# IdLoc()

def NameLoc():
    locName="name"
    value="username"
    print('before web element')
    webEleRef=getWebElement(locName,value)
    print(webEleRef)
# NameLoc()
# driver.quit()

def classNameLoc():
    locName = "classname"
    value = "textField"
    print('before web element')
    webEleRef = getWebElement(locName, value)
    print(webEleRef)
classNameLoc()



def TagNameLoc():
    locName = 'tagname'
    value = "input"
    print('before web element')
    webEleRef = getWebElement(locName, value)
    print(webEleRef)
# TagNameLoc()


def linkTextLoc():
    locName = 'linktext'
    value = "Forgot your password?"
    print('before web element')
    webEleRef = getWebElement(locName, value)
    print(webEleRef)
# linkTextLoc()

def ParlinkTextLoc():
    locName = 'plink'
    value = "Forgot"
    print('before web element')
    webEleRef = getWebElement(locName, value)
    print(webEleRef)
# ParlinkTextLoc()