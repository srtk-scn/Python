from selenium import webdriver
from onlineSelPrg.setting import chromepath
def assign5_1():
    driver=webdriver.Chrome(executable_path=chromepath)
    driver.get(url=r"C:\Users\sarthak sachan\PycharmProjects\online_selenium\onlineSelPrg\scripts\index5.html")
    driver.maximize_window()
    pattern='table[border="5px"] tbody tr td#price'
    ref=driver.find_elements_by_css_selector(pattern)
    total=0
    for i in ref:
        p=int(i.text)
        total+=p
    print("total price of all the listed items is", total)
    driver.close()
# assign5_1()

def assign5_2():
    driver=webdriver.Chrome(executable_path=chromepath)
    driver.get(url=r"C:\Users\sarthak sachan\PycharmProjects\online_selenium\onlineSelPrg\scripts\index5.html")
    driver.maximize_window()
    pattern='table[border="5px"] tbody tr td#price'
    ref=driver.find_elements_by_css_selector(pattern)
    dictdata={}
    for i in ref:
        # dictdata.setdefault(i.get_attribute("value"),i.text)
    print(dictdata)
    driver.close()
assign5_2()