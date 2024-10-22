from onlineSelPrg.scripts.locators import getWebElement

def NameLoc():
    locName='name'
    value='username'
    print('before webRef')
    webRef=getWebElement(locName,value,'https://online.actitime.com/ssachan/login.do')
    print(webRef)
# NameLoc()

def tagNameLoc():
    locName = 'tagname'
    value = 'username'
    print('before webRef')
    webRef = getWebElement(locName, value, 'https://online.actitime.com/ssachan/login.do')
    print(webRef)
tagNameLoc()