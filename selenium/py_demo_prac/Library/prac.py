from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="F:\selenium\py_demo_prac\Library\chromedriver")
driver.get("http://demowebshop.tricentis.com/")
time.sleep(2)
driver.save_screenshot('F:\selenium\py_demo_prac\Data\screenshots')
driver.quit()