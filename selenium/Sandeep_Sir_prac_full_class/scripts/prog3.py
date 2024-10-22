import time
from selenium.webdriver.support.select import Select
from settings import driver,facebook,chromepath
driver.get(url=facebook)
time.sleep(2)
driver.find_element_by_id("u_0_2").click()
time.sleep(3)
f_name=driver.find_element_by_name("firstname").send_keys("sarthak")
l_name=driver.find_element_by_name("lastname").send_keys("sachan")
Mob=driver.find_element_by_xpath('//input[@name="reg_email__"]').send_keys("7011785707")
p_word=driver.find_element_by_id("password_step_input").send_keys("sarthak@123")
bday=driver.find_element_by_name("birthday_day")
b_day=Select(bday)
b_day.select_by_visible_text('10')
time.sleep(1)

bmonth=driver.find_element_by_name("birthday_month")
b_month=Select(bmonth)
b_month.select_by_visible_text("Dec")
time.sleep(2)

byear=driver.find_element_by_name("birthday_year")
b_year=Select(byear)
b_year.select_by_visible_text("1996")
time.sleep(2)

driver.find_element_by_xpath('//label[text()="Male"]').click()
time.sleep(3)
driver.find_element_by_name("websubmit").click()

from selenium import webdriver
driver=webdriver.Chrome(executable_path='F:\selenium\Sandeep_Sir\drivers\chromedriver.exe')
driver.get('F:\selenium\Sandeep_Sir\scripts\HTML FILES\Standard_listBox.html')
time.sleep(1)
lst_cars=driver.find_element_by_id("standard_cars")
select=Select(lst_cars)
select.select_by_visible_text("Land Rover")
time.sleep(2)

select.select_by_index(8)
time.sleep(1)
select.select_by_index(11)
time.sleep(1)
driver.quit()

#
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# import time
#
# # Instantiate a Chrome Browser
# driver = webdriver.Chrome(chromepath)
# driver.maximize_window()
# driver.get('http://demowebshop.tricentis.com/books')
#
# time.sleep(2)
#
# lst_sort_by = driver.find_element_by_id("products-orderby")
#
# select = Select(lst_sort_by)
#
# # Selecting item by visible text
# select.select_by_visible_text("Name: A to Z")
#
# time.sleep(3)
#
# # Selecting item by index
# select.select_by_index(4)   # Selects the item at index-4 (Price: High to Low)
#
# time.sleep(3)
# driver.quit()