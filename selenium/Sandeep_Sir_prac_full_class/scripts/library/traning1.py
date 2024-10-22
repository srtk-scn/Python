#DEPENDENT AND INDEPENDENT TYPES OF XPATH

"""EXANPLE--   IF WE ARE GOING TO QSPIDER APPLICATION WHERE SARCHES OF SHOW BATCHES LINK THERE ARE MANY LINKS TO CLICK
LINK ARE DEPENDENT ON THE WITH SOME SOME SPECIFIC BATCHES SO IF IN FUTURE IF DEVELOPER MIGHT INSERT SOME MORE BATCHES AND WE ARE SEARCHES INDEPENDLY BY INDEXING
 MIGHT NOT GET THAT SPECIFIC BATCH INFORMATION ******     SO WE HAVE TO MAKE DEPENDENT OF SHOW BATCHES TO SOME SPECIFIC COURSE SO IN FUTURE WE ARE NOT GET ANY ERROR"""

import time
from settings import chromepath
from selenium import webdriver
driver=webdriver.Chrome(executable_path=chromepath)
driver.get("http://www.qspiders.com/courses")
time.sleep(3)
# l=driver.find_elements_by_xpath('//a[text()="Show batches"]')
# closeX='//button[text()="Close"]'
# for i in range(len(l)):
#     l[i].click()
#     time.sleep(3)
#     driver.find_element_by_xpath(closeX).click()
# # xpath='(//a[text()="Show batches"])[5]'            # if we want to click only one element independently
# # driver.find_element_by_xpath(xpath).click()
# time.sleep(1)
# driver.close()





_xpath='//span[text()=" Python - Selenium"]/../..//a[text()="Show batches"]' #now show link batch is attached to the python selenium course so that in future it will identify even if developer changes its position
driver.find_element_by_xpath(_xpath).click()
time.sleep(2)
driver.close()

