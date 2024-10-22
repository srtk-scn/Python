from selenium import webdriver
import time
from settings import chromepath
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path=chromepath)
# driver.get('F:\selenium\Sandeep_Sir\scripts\HTML FILES\custom_select.html')
# time.sleep(4)
# driver.find_element_by_class_name("select-selected").click()
# driver.find_element_by_xpath('//div[text()="Honda"]').click() #we are not using select class here because this is custom list box not under in option tag
# time.sleep(2)
# driver.close()
driver.get('F:\selenium\Sandeep_Sir_prac_full_class\scripts\HTML FILES\Auto_complete.html')
time.sleep(2)
driver.find_element_by_name("myCountry").send_keys("United")
time.sleep(1)
# driver.find_element_by_xpath("//div[text()=' States of America']").click()
actions=ActionChains(driver)
# actions.send_keys(Keys.ARROW_DOWN).perform()
# time.sleep(1)
# actions.send_keys(Keys.ARROW_DOWN).perform()
# time.sleep(1)
# actions.send_keys(Keys.ARROW_DOWN).perform()
# time.sleep(1)
for _ in range(3):
    actions.send_keys(Keys.ARROW_DOWN).perform()
    time.sleep(1)

actions.send_keys(Keys.ENTER).perform()
time.sleep(2)
driver.close()