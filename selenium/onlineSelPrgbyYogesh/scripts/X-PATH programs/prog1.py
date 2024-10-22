from selenium import webdriver
from onlineSelPrg.setting import chromepath,actiTimeUrl
import time
htmlFilePath=r"C:\Users\sarthak sachan\PycharmProjects\online_selenium\onlineSelPrg\scripts\index6.html"

def absPath():
    driver=webdriver.Chrome(executable_path=chromepath)
    driver.get(url=htmlFilePath)
    driver.maximize_window()
    time.sleep(2)
    userName="/html/body/div[1]/input[1]"
    passWord="/html/body/div[1]/input[2]"
    driver.find_element_by_xpath(userName).send_keys("admin")
    driver.find_element_by_xpath(passWord).send_keys("admin123")
    time.sleep(4)
    driver.close()
# absPath()


def absPath1():
    driver=webdriver.Chrome(executable_path=chromepath)
    driver.get(url=htmlFilePath)
    driver.maximize_window()
    time.sleep(2)
    pattern="/html/body/div[1]/input"
    ref=driver.find_elements_by_xpath(pattern)
    print(ref)
    for i in ref:
        print(i.get_attribute("name"))
    ref[0].send_keys("sarthak")
    ref[1].send_keys("sachan")
    time.sleep(4)
    driver.close()
# absPath1()


def absPath2():
    driver=webdriver.Chrome(executable_path=chromepath)
    driver.get(url=htmlFilePath)
    driver.maximize_window()
    time.sleep(2)
    pattern="/html/body/div/input"
    ref=driver.find_elements_by_xpath(pattern)
    print(ref)
    for i in ref:
        print(i.get_attribute("name"))
    ref[0].send_keys("sarthak")
    ref[1].send_keys("sachan")
    ref[2].send_keys("admin")
    ref[3].send_keys("123")
    time.sleep(4)
    driver.close()
# absPath2()


def absPath3():
    driver=webdriver.Chrome(executable_path=chromepath)
    driver.get(url=htmlFilePath)
    driver.maximize_window()
    time.sleep(2)
    pattern="/html/body/div/input"
    ref=driver.find_elements_by_xpath(pattern)
    print(ref)
    data={"username":"ram","password":"12345","firstname":"ram","lastname":"R"}
    for i in ref:
        i.send_keys(data[i.get_attribute("name")])
    for i in range(len(ref)):
        if i%2==0:
            ref[i].clear()
    time.sleep(4)
    driver.close()
# absPath3()

def absPath4():
    driver=webdriver.Chrome(executable_path=chromepath)
    driver.get(url=htmlFilePath)
    driver.maximize_window()
    time.sleep(2)
    pattern="/html/body/div/input"
    ref=driver.find_elements_by_xpath(pattern)
    print(ref)
    data={}
    for i in ref:
        data.setdefault(i.get_attribute("name"),i.get_attribute("value"))
        print(i.location)
        print(i.size)
        print(i.rect)
    print(data)
    driver.close()
# absPath4()