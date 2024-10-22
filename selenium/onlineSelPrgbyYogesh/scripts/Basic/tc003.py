#find_element  and find_element_by_id

#BY class

from selenium import webdriver
from selenium.webdriver.common.by import By
from onlineSelPrg.setting import chromepath,actiTimeUrl,googleurl,appUrl,youTubeUrl,flipUrl
driver=webdriver.Chrome(executable_path=chromepath)
def ID_Loc():
    driver.get(actiTimeUrl)
    driver.maximize_window()
    webEleRef=driver.find_element(By.ID,'username')
    # webEleRef=driver.find_element_by_id('username')
    print('wen element reference', webEleRef)
    driver.close()
# ID_Loc()

def ClassNameLoc():
    driver.get(url=flipUrl)
    driver.maximize_window()
    # webEleRef=driver.find_element(By.CLASS_NAME,"LM6RPg")
    webEleRef=driver.find_element_by_class_name("LM6RPg")
    print('web element reference',webEleRef)
    driver.close()
# ClassNameLoc()

#  below function is self made as assignment
def Genric(url,loc_type,loc_name):
    driver.get(url)
    driver.maximize_window()
    if loc_type[0]=='c' or loc_type=='C':
        WebEleRef=driver.find_element_by_class_name(loc_name)
        print('web element by reference (class)',WebEleRef)
    elif loc_type[0]=='i' or loc_type=='I':
        Web_ele=driver.find_element_by_id(loc_name)
        print('web element by reference (ID)', Web_ele)
    else:
        print('out of syllabus for now')
    driver.close()
# Genric(actiTimeUrl,'id','username')
Genric(flipUrl,'class',"LM6RPg")