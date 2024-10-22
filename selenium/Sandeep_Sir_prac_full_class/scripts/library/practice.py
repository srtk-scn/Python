from selenium import webdriver
driver= webdriver.Chrome(executable_path='F:\selenium\Sandeep_Sir_prac_full_class\drivers\chromedriver.exe')
from selenium.webdriver.support.select import Select

driver.get("https://www.facebook.com/login/web/")
import time

time.sleep(2)
driver.find_element_by_class_name("class=_42ft _4jy0 _16jx _4jy6 _4jy2 selected _51sy").click()
time.sleep(2)
list_=driver.find_element_by_class_name('birthday_day')
select=Select(list_)
select.select_by_visible_text("1")
time.sleep(1)
b_month=driver.find_element_by_class_name('birthday_month')
select=Select(b_month)
select.select_by_visible_text('Dec')
time.sleep(1)

b_year=driver.find_element_by_name('birthday_year')
select=Select(b_year)
select.select_by_value("1996")
time.sleep(1)
driver.quit()