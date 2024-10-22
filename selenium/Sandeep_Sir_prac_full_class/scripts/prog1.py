import time
from settings import driver,demoshop
driver.get(url=demoshop)
driver.maximize_window()
driver.find_element_by_link_text("Register").click()
time.sleep(4)
driver.find_element_by_id("gender-male").click()
driver.find_element_by_id('FirstName').send_keys("Sarthak")
driver.find_element_by_id('LastName').send_keys('Sachan')
driver.find_element_by_id("register-button").click()
driver.find_element_by_id("Email").send_keys("sarthak786sachan@gmail.com")
driver.find_element_by_id("Password").send_keys('Sarrthak@123')
driver.find_element_by_id("ConfirmPassword").send_keys('Sarrthak@123')
time.sleep(5)
driver.close()

