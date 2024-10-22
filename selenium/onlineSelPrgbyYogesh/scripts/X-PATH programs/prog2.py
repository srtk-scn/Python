#relative path examples

from selenium import webdriver
from onlineSelPrg.setting import chromepath,actiTimeUrl
import time
htmlFilePath=r"http://demowebshop.tricentis.com/"

def absPath5():
    driver=webdriver.Chrome(executable_path=chromepath)
    driver.get(url=htmlFilePath)
    driver.maximize_window()
    time.sleep(2)
    relpath="//a"
    webRef=driver.find_elements_by_xpath(relpath)
    for i in webRef:
        print(i.get_attribute("href"))
    time.sleep(4)
    driver.close()
# absPath5()

def absPath6():
    driver=webdriver.Chrome(executable_path=chromepath)
    driver.get(url=htmlFilePath)
    driver.maximize_window()
    time.sleep(2)
    relpath="//a"
    webRef=driver.find_elements_by_xpath(relpath)
    listdata=[]
    for i in webRef:
        listdata.append(i.get_attribute("href"))
    print(listdata)
    print(len(listdata))
    driver.close()
# absPath6()



def absPath7():
    driver=webdriver.Chrome(executable_path=chromepath)
    driver.get(url=htmlFilePath)
    driver.maximize_window()
    time.sleep(2)
    relpath="//ul//li//a"
    webRef=driver.find_elements_by_xpath(relpath)
    listdata=[]
    for i in webRef:
        listdata.append(i.get_attribute("href"))
    print(len(listdata))
    driver.close()
absPath7()
