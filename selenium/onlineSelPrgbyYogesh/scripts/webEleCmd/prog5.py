from selenium import webdriver
# from onlineSelPrg.setting import chromepath,actiTimeUrl
import time
import json
filePath=r"C:\Users\sarthak sachan\PycharmProjects\online_selenium\onlineSelPrg\scripts\index.html"

def cssSelMatch():
    driver = webdriver.Chrome(executable_path=r"C:\Users\sarthak sachan\PycharmProjects\online_selenium\onlineSelPrg\drivers\chromedriver.exe")
    driver.maximize_window()
    driver.get(url=filePath)
    time.sleep(4)
    pattern = "ul li:first-child"
    pattern="ul#parent>li:last-child"
    pattern="ul#parent>li:nth-child(2)"
    webEleRef= driver.find_element_by_css_selector(pattern)
    print("web element ref",webEleRef)
    myString=str(webEleRef)


    with open("WebEleRef.txt","w") as json_file:
        json.dump(myString,json_file)
    driver.close()

# cssSelMatch()




