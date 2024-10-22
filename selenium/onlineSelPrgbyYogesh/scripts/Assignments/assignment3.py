from selenium import webdriver
from onlineSelPrg.setting import chromepath
def assign3():
    driver=webdriver.Chrome(executable_path=chromepath)
    driver.get(url=r"C:\Users\sarthak sachan\PycharmProjects\online_selenium\onlineSelPrg\scripts\index3.html")
    driver.maximize_window()
    IndexRef=driver.find_elements_by_css_selector("p#sarthak>a")
    print(IndexRef)
    attrName="href"
    dict={}
    for i in range(len(IndexRef)):
        dict.setdefault(attrName+ str(i+1),IndexRef[i].get_attribute(attrName))
    print(dict)
    driver.close()
# assign3()

def assign4_1():     #first and last check
    driver=webdriver.Chrome(executable_path=chromepath)
    driver.get(url=r"C:\Users\sarthak sachan\PycharmProjects\online_selenium\onlineSelPrg\scripts\index4.html")
    driver.maximize_window()
    pattern="form fieldset input "
    indexREf=driver.find_elements_by_css_selector(pattern)
    print(indexREf)
    dictdata={}
    for i in range(len(indexREf)):
        def check(i):
            if indexREf[i].is_selected():
                return "Checked"
            else:
                return "Not Checked"
        dictdata.setdefault(str(i+1),check(i))
    print(dictdata)
# assign4_1()


def assign4_2():    #evenposition check
    driver=webdriver.Chrome(executable_path=chromepath)
    driver.get(url=r"C:\Users\sarthak sachan\PycharmProjects\online_selenium\onlineSelPrg\scripts\index4.html")
    driver.maximize_window()
    pattern="form fieldset input "
    indexREf=driver.find_elements_by_css_selector(pattern)
    print(indexREf)
    dictdata={}
    for i in range(len(indexREf)):
        if i%2==1:
            def check(i):
                if indexREf[i].is_selected():
                    return "Checked"
                else:
                    return "Not Checked"
            dictdata.setdefault(str(i+1),check(i))
    print(dictdata)
# assign4_2()


def assign4_3():    #oddposition check
    driver=webdriver.Chrome(executable_path=chromepath)
    driver.get(url=r"C:\Users\sarthak sachan\PycharmProjects\online_selenium\onlineSelPrg\scripts\index4.html")
    driver.maximize_window()
    pattern="form fieldset input "
    indexREf=driver.find_elements_by_css_selector(pattern)
    print(indexREf)
    dictdata={}
    for i in range(len(indexREf)):
        if i%2==0:
            def check(i):
                if indexREf[i].is_selected():
                    return "Checked"
                else:
                    return "Not Checked"
            dictdata.setdefault(str(i+1),check(i))
    print(dictdata)
assign4_3()