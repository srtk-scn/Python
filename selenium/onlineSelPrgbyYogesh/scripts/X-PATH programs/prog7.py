import time
from selenium import webdriver
from onlineSelPrg.setting import chromepath,demoshop
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path=chromepath)
driver.get(demoshop)
driver.find_element_by_link_text("Books").click()
# ref=driver.find_element_by_xpath('//select[@id="products-orderby"]')
# print(ref)
# s=Select(ref)
# s.select_by_visible_text("Price: High to Low")
# ref=driver.find_element_by_xpath('//select[@id="products-orderby"]')
# print(ref)
# s=Select(ref)
# s.select_by_visible_text("Name: Z to A")
#
# driver.quit()
element=driver.find_element_by_name('q')
element.send_keys("Computer")
print(element)
driver.refresh()
time.sleep(2)
element=driver.find_element_by_name('q')
element.send_keys("iphone")
print(element)
driver.quit()