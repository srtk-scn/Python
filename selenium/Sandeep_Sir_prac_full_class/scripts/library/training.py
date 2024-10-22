from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from settings import demoshop

driver=webdriver.Chrome(executable_path="F:\selenium\Sandeep_Sir\drivers\chromedriver.exe")
# driver.get("F:\selenium\Sandeep_Sir\scripts\HTML FILES\loading.html")
driver.get(demoshop)
class element_to_be_visible_enabled:
    def __init__(self,locator):
        self.locator=locator
    def __call__(self,driver):
        locatortype,locatorvalue=self.locator
        element=driver.find_element(locatortype,locatorvalue)
        if element.is_displayed() and element.is_enabled():
            return True
        else:
            return False
def wait(visible=True,enabled=True,max_timeout=15):
    def decorate(func):
        def wrapper(*args,**kwargs):
            locator,=args
            w=WebDriverWait(driver,max_timeout)
            if visible and enabled:
                w.until(element_to_be_visible_enabled(locator))
            elif visible and not enabled:
                w.until(ec.visibility_of_element_located(locator))
            elif not visible:
                w.until(ec.invisibility_of_element_located(locator))
            return func(*args,**kwargs)
        return wrapper
    return decorate
@wait()
def enter_text(locator,*,value):
    loctype,locvalue=locator
    driver.find_element(loctype,locvalue).clear()
    driver.find_element(loctype,locvalue).send_keys(value)
@wait()
def click_element(locator):
    loctype, locvalue = locator
    driver.find_element(loctype, locvalue).click()
@wait()
def select_item(locator,*,item):
    loctype,locvalue=locator
    element=driver.find_element(loctype,locvalue)
    select=Select(element)
    items=[i.text for i in select.options]
    if item not in items:
        raise ValueError(f"{item} is not presentin the listbox")
    if isinstance(item,str):
        select.select_by_visible_text(item)
    else:
        select.select_by_index(item)



# def wait(locator,*,visible=True,enabled=True,max_timeout=15):
# wait(('id','loader'),visible=False)
# enter_text(('name','sarthak'),"sarthak")

# wait(('link text', "Register"), max_timeout=5)
click_element(('link text', "Register"))

# wait(("id", "gender-male"), max_timeout=1)
click_element(("id", "gender-male"))

# wait(("name", "FirstName"), max_timeout=1)
enter_text(("name", "FirstName"), value="Sandeep")

# wait(("name", "LastName"), max_timeout=1)
enter_text(("name", "LastName"), value="Suryaprasad")

# wait(("id", "register-button"), max_timeout=1)
click_element(("id", "register-button"))




