from selenium import webdriver
import time
from settings import chromepath,qspider

driver=webdriver.Chrome(executable_path=chromepath)
driver.get('https://in.yahoo.com/')
# time.sleep(4)
# f=open('link.xl','w')
#
# _xpath='//ul[@id="header-nav-bar"]/li/a'
# links = driver.find_elements_by_xpath(_xpath)
# for link in links:
#     text=link.text
#     url=link.get_attribute("href")
#     print(f"{text:<20} {url:<40}",file=f)
#     print("*"*100,file=f)
# driver.close()

#ACTIONS CLASS WIHT EAXAMPLE OF HOVERING WEB PAGE
from selenium.webdriver.common.action_chains import ActionChains
# driver.get("F:\selenium\Sandeep_Sir\scripts\HTML FILES\Hovarable.html")
# time.sleep(1)
actions=ActionChains(driver)
# about=driver.find_element_by_xpath('//a[text()="About"]')
# actions.move_to_element(about).perform()
# time.sleep(1)
# driver.close()
# menus=["About","Blog","Projects","Contact"]
# for menu in menus:
#     actions = ActionChains(driver)
#     xpth=f'//div[@id="mySidenav"]/a[text()="{menu}"]'
#     ref=driver.find_element_by_xpath(xpth)
#     actions.move_to_element(ref).perform()
#     time.sleep(1)
# driver.close()

# from selenium.webdriver.common.keys import Keys
# driver.get(qspider)
time.sleep(4)
# ele1='//a[text()="Gallery "]'
# ele2='//a[text()="Recruitment Drive"]'
# actions=ActionChains(driver)
# ref1=driver.find_element_by_xpath(ele1)
# actions.move_to_element(ref1).perform()
# time.sleep(1)
# ref2=driver.find_element_by_xpath(ele2)
# actions.move_to_element(ref2).perform()
# driver.close()

# Keys
for _ in range(0,5):
    actions.send_keys("\ue00f").perform()
    time.sleep(1)
for _ in range(0,5):
    actions.send_keys("'\ue00e'").perform()
    time.sleep(1)
