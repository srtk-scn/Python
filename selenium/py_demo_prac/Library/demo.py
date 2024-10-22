from Library.custom_wait import wait_
from selenium import webdriver
driver=webdriver.Chrome(executable_path="F:\selenium\py_demo_prac\Library\chromedriver")


@wait_
def loading(driver):
    driver.get("F:\selenium\py_demo_prac\Library\loading.html")
