import time
from selenium.webdriver.support.select import Select
from settings import driver,facebook,demoshop
from selenium.webdriver.common.by import By
# driver.get(url=r"F:\selenium\Sandeep_Sir_prac_full_class\scripts\HTML FILES\checkbox.html")
# references=driver.find_elements_by_name("download")
# print(type(references))
# print(references)
# for box in references:
#     box.click()
#     print(box)
#     time.sleep(1)
# driver.close()
# for box in reversed(references):
#     box.click()
#     print(box)
#     time.sleep(1)
# driver.close()
# for box in references[4:0:-1]:
#     box.click()
#     print(box)
#     time.sleep(1)
# driver.close()
# for box in references[(len(references)-1):0:-1]:
#     box.click()
#     print(box)
#     time.sleep(1)
# driver.close()
# for box in range((len(references)-1),0,-1):
#     references[box].click()
#     print(references[box])
#     time.sleep(1)
# driver.close()
driver.get(url=demoshop)
def click_element(locator):
    locatortype, locatorvalue = locator
    driver.find_element(locatortype, locatorvalue).click()
click_element((By.LINK_TEXT,"Register"))
# driver.find_element(By.LINK_TEXT,"Register").click()
time.sleep(3)