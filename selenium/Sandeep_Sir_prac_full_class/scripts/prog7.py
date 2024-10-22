from settings import driver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# driver.get(url="F:\selenium\Sandeep_Sir_prac_full_class\scripts\HTML FILES\progressBar.html")
# time.sleep(1)
# w=WebDriverWait(driver,9)
# driver.find_element_by_xpath("//button[text()='Click Me']").click()

#VISIBILTIY_OF
# ele=driver.find_element_by_xpath("//div[text()='100%']")   #NO SUCH ELEMENT EXCEPTION NOT IN DOM AS PROGRESS BAR INCRESING WITH TIME
# w.until(ec.visibility_of(ele))
# driver.close()




#VISIBILITY_OF_ELEMENT_LOCATED
# w.until(ec.visibility_of_element_located(("xpath","//div[text()='100%']")))   #IF 5 SECONDS ONLY THEN TIME OUT EXECPTION OTHERWISE WAIT TILL TIME TRACK THAT ELEMENT
# driver.close()


#INVISIBILITY OF ELEMENT
# s=WebDriverWait(driver,10)
# ele=driver.find_element_by_xpath("//div[text()='100%']")   # Since the element is not loaded at instance of html page NOSUCHELEMENTEXCEPTION RAISE
# s.until(ec.invisibility_of_element(ele))
# time.sleep(1)


#INVISIBILITY OF ELEMENT LOCATED
# s=WebDriverWait(driver,5)
# s.until(ec.invisibility_of_element_located(('xpath',"//div[text()='7%']")))
# time.sleep(1)
# driver.close()

driver.implicitly_wait(15)
driver.get('F:\selenium\Sandeep_Sir_prac_full_class\scripts\HTML FILES\progressBar.html')
ele=driver.find_element_by_xpath("//div[text()='100%']")

# class element_to_be_visible_enable:
#     def __init__(self,locator):
#         self.locator=locator
#
#     def __call__(self, driver):
#         locatortype,locatorvalue=self.locator
#         element=driver.find_element(locatortype,locatorvalue)
#         if element.is_dis