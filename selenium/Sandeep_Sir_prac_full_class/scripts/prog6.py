
from settings import driver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver.get(url="F:\selenium\Sandeep_Sir_prac_full_class\scripts\HTML FILES\loading.html")


  # VISIBILITY OF*******
#loading symbol till 5 sec of html page
#

# w=WebDriverWait(driver,2)  #wait for 4 second only raise time out exception
# w=WebDriverWait(driver,10)  # first name text feild is disable then raise elementnotinteractable exception
# w=WebDriverWait(driver,6)    #  working fine
# if the firstname text feild is erased in html then no such element execption
element=driver.find_element_by_name("fname")
w.until(ec.visibility_of(element))  #this element will take argument as element reference)
element.send_keys("Sarthak")
time.sleep(1)
driver.close()
driver.quit()

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome()
driver.get()
wait=WebDriverWait(driver,7)
ref=driver.find_element_by_name()
wait.until(ec.visibility_of(ref))





# VISIBILITY_OF_ELEMENT_LOCATED
# s=WebDriverWait(driver,4) #timeoutException
# s=WebDriverWait(driver,6)  #works fine
# if the firstname textfeild is disabled from the html page then elementNotInteractable
# s.until(ec.visibility_of_element_located(("name","fname")))
# driver.find_element_by_name("fname").send_keys("sachan")
# time.sleep(1)
# driver.close()


#INVISIBILITY_OF_ELEMENT
# i=WebDriverWait(driver,10)
# element=driver.find_element_by_id("loader")
# i.until(ec.invisibility_of_element(element))
# i.until(ec.invisibility_of_element_located(("id","loader")))
# driver.find_element_by_name('fname').send_keys("sarthak")
# time.sleep(1)
# driver.close()



