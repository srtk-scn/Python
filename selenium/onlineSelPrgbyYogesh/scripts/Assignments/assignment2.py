from selenium import webdriver
from onlineSelPrg.setting import chromepath,actiTimeUrl
import time

def writeData(data):
    fileObj= open("../webEleCmd/pythonSel.txt", "w")
    fileObj.write(data)
    fileObj.close()


def webElementText():
    driver= webdriver.Chrome(executable_path=chromepath)
    driver.maximize_window()
    driver.get(url=r"https://www.google.com/")
    time.sleep(2)
    driver.find_element_by_name("q").send_keys("python")
    time.sleep(3)
    pattern='ul[role="listbox"]>li>div>div[role="option"] div:first-child span'
    webEleRef=driver.find_elements_by_css_selector(pattern)      #element(.is_displyed and is_enabled and is_selected works on it) VS elements(returns a list of having all the refrence elements)
    print("web element refernece is ",webEleRef)
    print(type(webEleRef),len(webEleRef))
    listData=[]
    dictData={}
    for i in range(len(webEleRef)):         #    for i in webEleRef:
        listData.append(webEleRef[i].text)        #      listData.append(i.text)
        dictData.setdefault(webEleRef[i].tag_name+str(i),webEleRef[i].text)
    print(listData)
    print(dictData)
    writeData(str(dictData))
    # writeData(str(listData))
    driver.close()
webElementText()