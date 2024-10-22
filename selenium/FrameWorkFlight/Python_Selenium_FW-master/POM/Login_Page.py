from Library import *
from POM import *


class LoginPage(BasePage):
    
    LoginPage_Objects = read_locators('Login_Page')
    
    def enter_user_name(self):
        txt_username = self.get_by_type(self.__class__.LoginPage_Objects['txt_username'])
        self.enter_text(txt_username, value=Config.USERNAME)
        
    def enter_password(self):
        txt_password = self.get_by_type(self.__class__.LoginPage_Objects['txt_password'])
        self.enter_text(txt_password, value=Config.PASSWORD)
    
    def click_login(self):
        btn_login = self.get_by_type(self.__class__.LoginPage_Objects['btn_login'])
        self.click_element(btn_login)
