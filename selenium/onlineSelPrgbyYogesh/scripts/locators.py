from selenium import webdriver
from selenium.webdriver.common.by import By
from onlineSelPrg.setting import chromepath,actiTimeUrl

def getLocator(loc):
    loc=loc.lower()
    if loc=='id':
        return By.ID
    elif loc=='classname':
        return By.CLASS_NAME
    elif loc=='name':
        return By.NAME
    elif loc=='tagname':
        return By.TAG_NAME
    elif loc=='linktext':
        return By.LINK_TEXT
    elif loc=='plink':
        return By.PARTIAL_LINK_TEXT
    elif loc=='cssselector':
        return By.CSS_SELECTOR
    elif loc=='xpath':
        return By.XPATH
    else:
        return None



def getWebElement(loc,value):
    driver = webdriver.Chrome(executable_path=chromepath)
    driver.maximize_window()
    driver.get(url=actiTimeUrl)
    print('Url Enterned!!')
    loc=getLocator(loc)
    if loc!=None:
        webEleRef=driver.find_element(loc,value)
        # webEleRef = driver.find_element_by_tag_name(value)
        # driver.close()
    return webEleRef

# result=getWebElement('id','username')
# print(result)

