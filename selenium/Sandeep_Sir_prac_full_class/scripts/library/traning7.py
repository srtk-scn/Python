from selenium import webdriver
import time
from settings import chromepath,demoshop
driver=webdriver.Chrome(chromepath)
driver.get(demoshop)
time.sleep(4)
driver.find_element_by_xpath("//a[text()='Facebook']").click()
time.sleep(4)
win_handle=driver.window_handles
print(win_handle)
driver.switch_to.window(win_handle[1])
driver.find_element_by_id("email").send_keys('Hello')
driver.switch_to.window(win_handle[0])
time.sleep(3)
driver.find_element_by_name("q").send_keys("Computer")
driver.find_element_by_xpath('//input[@value="Search"]').click()
time.sleep(2)
driver.quit()