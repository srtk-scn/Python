from Library.SeleniumWrapper import SeleniumWrapper
from Data import *


class HomePage(SeleniumWrapper):
    HomePage_objects = read_locators("HomePage")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def click_register(self):
        lnk_register = self.__class__.HomePage_objects['lnk_register']
        self.click_element(lnk_register)

    def click_login(self):
        lnk_login = self.__class__.HomePage_objects['lnk_login']
        self.click_element(lnk_login)

