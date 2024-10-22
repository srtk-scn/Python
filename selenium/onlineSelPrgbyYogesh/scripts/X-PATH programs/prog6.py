# Track elements by using ATTRIBUTE from RELATIVE PATH
#SYNTAX:-   //TAGNAME[@attr_name="attr_value]
#SYNTAX:-   OR operator:-  //tagname[@attr1='val1'] or //tagname[@attr2='val2']
#    AND operator:-     AND operator:-  //tagname[@attr1='val1'] and //tagname[@attr2='val2']
#       //input[@name="pwd"]


#USing TEXT FUNCTION
# Syntaxx:- //tagname[text()="value"]
#1example:-  //div[text()="Login "]
#2          //label[text()="Keep me logged in"]
import time
from onlineSelPrg.setting import driver,actiTimeUrl
driver.get(actiTimeUrl)
driver.maximize_window()
driver.find_element_by_xpath('//input[@id="username"]').send_keys("sarthak786sachan11@gmail.com")
# driver.find_element_by_xpath('//input[@class="textField pwdfield"]').send_keys("sarthak@123")
# driver.find_element_by_xpath('//input[normalize-space(@name)="pwd"]').send_keys("sarthak@123")
driver.find_element_by_xpath('//input[normalize-space(@class)="textField pwdfield"]').send_keys("sarthak@123")
# driver.find_element_by_xpath('//div[text()="Login "]').click()
# driver.close()

#SYNTAXX:-  using normalize space()
#Example:-  //tagname[normalize-space(source)="value"]  source:-  text() or @attribute

driver.find_element_by_xpath('//div[normalize-space(text())="Login"]').click()
time.sleep(10)
driver.close()

#SYNTAXX:-  using contains()
#Example:-  //tagname[conains(source)="value"]  source:-  text() or @attribute

