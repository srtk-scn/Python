from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as ec
from settings import chromepath,qspider

driver=webdriver.Chrome(chromepath)
driver.get(qspider)
time.sleep(4)


_courses=[' Python - Selenium','Advanced Selenium-Software Testing Course','Api Testing']
f=open("batches.csv", "w")
# f=open("batches.txt", "w")
print("Course, Branch, Date, Timings",file=f)
for _course in _courses:
    _xpath=f'//span[text()="{_course}"]/../..//a[text()="Show batches"]'
    driver.find_element_by_xpath(_xpath).click()
    time.sleep(3)

    _branches=driver.find_elements_by_xpath('//td[@class="views-field views-field-field-branch"]')
    _dates=driver.find_elements_by_xpath('//span[@class="date-display-single"]')
    _timings=driver.find_elements_by_xpath('//td[@class="views-field views-field-field--batch-commencing-date-1"]/span')

    for _branch,_date,_timing in zip(_branches,_dates,_timings):
        print(_course,',',_branch.text,",",_date.text,',',_timing.text,file=f)
    print("*"*50,file=f)
    driver.find_element_by_xpath("//button[text()='Close']").click()
driver.close()