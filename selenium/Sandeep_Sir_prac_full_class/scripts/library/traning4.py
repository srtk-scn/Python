from selenium import webdriver
from settings import chromepath,demoshop,qspider
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(chromepath)
driver.get(demoshop)
time.sleep(3)
actions=ActionChains(driver)
actions.send_keys(Keys.TAB).perform()          #this send keys is different from previous here because here only can input the keyboards input only KEYS

def mouse_hover(locator):
    locator_type,locator_value=locator
    actions=ActionChains(driver)
    element=driver.find_element(locator_type,locator_value)
    actions.move_to_element(element).perform()
# driver.get("F:\selenium\Sandeep_Sir\scripts\HTML FILES\Hovarable.html")
# mouse_hover(('xpath',"//a[text()='About']"))


def send_keyboard_input(key):
    if not key.upper() in {'PAGE_DOWN','PAGE_UP','ARROW_UP','ARROW_DOWN','ENTER','ESCAPE','TAB'}:
        raise ValueError(f'Invalid passed key {key}')
    actions=ActionChains(driver)
    if key.upper()=='PAGE_DOWN':
        actions.send_keys(Keys.PAGE_DOWN).perform()
    elif key.upper()=='PAGE_UP':
        actions.send_keys(Keys.PAGE_UP).perform()
    elif key.upper()=='ARROW_UP':
        actions.send_keys(Keys.ARROW_UP).perform()
    elif key.upper()=='ARROW_DOWN':
        actions.send_keys(Keys.ARROW_DOWN).perform()
    elif key.upper()=='ENTER':
        actions.send_keys(Keys.ENTER).perform()
    elif key.upper()=='ESCAPE':
        actions.send_keys(Keys.ESCAPE).perform()
    elif key.upper()=='TAB':
        actions.send_keys(Keys.TAB).perform()
# driver.get(demoshop)
# time.sleep(5)
# send_keyboard_input("tab")

