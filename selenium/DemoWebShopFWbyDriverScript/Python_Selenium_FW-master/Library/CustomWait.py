from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from functools import wraps, partial
import datetime
import os
import time





class element_to_be_enabled:
    """ Custom Class to check if the element is enabled """
    def __init__(self, bytype, locator):
        self.bytype = bytype
        self.locator = locator

    def __call__(self, driver):
        element = driver.find_element(self.bytype, self.locator)
        return True if element.is_enabled() else False


def wait_(func=None, *, visibility=True, enabled=True, timeout=60, is_alert=False):
    if func is None:
        return partial(wait_, visibility=visibility, enabled=enabled, timeout=timeout,
                       is_alert=is_alert)

    @wraps(func)
    def wrapper(*args, **kwargs):
        instance, element = args
        locator_type, locator = element
        wait = WebDriverWait(instance.driver, timeout, poll_frequency=0.5)
        if is_alert:
            wait.until(ec.alert_is_present(), message='Alert does not exist')
            return func(*args, **kwargs)
        if visibility:
            wait.until(ec.visibility_of_element_located((locator_type, locator)),
                       message=f'{locator} not visible after timeout period of {timeout} seconds')
            if enabled:
                wait.until(element_to_be_enabled(locator_type, locator), message = f'{locator} is enabled after timeout period of {timeout} seconds')
                if func.__name__ == 'click_element':
                    wait.until(ec.element_to_be_clickable((locator_type, locator)), message=f'{locator} is not clickable after timeout period of {timeout} seconds')
            return func(*args, **kwargs)
        else:
            time.sleep(3)
            wait.until(ec.invisibility_of_element_located((locator_type, locator)),
                       message=f'{locator} is visible after timeout period of {timeout} seconds')
            return func(*args, **kwargs)
    return wrapper


def page_load(func=None, *, timeout=180):
    if func is None:
        return partial(page_load, timeout=timeout)
    @wraps(func)
    def wrapper(*args, **kwargs):
        instance, *rest = args
        wait = WebDriverWait(instance.driver, timeout)
        time.sleep(2)
        _xp = "Xpath of Loading Icon"
        wait.until(ec.invisibility_of_element_located(('xpath', _xp)), message=f'{_xp} is visible after timeout period of {timeout} seconds')
        time.sleep(0.5)
        return func(*args, **kwargs)
    return wrapper
