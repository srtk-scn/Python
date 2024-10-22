from Library import SeleniumWrapper
from Data import *

class RegistrationPage(SeleniumWrapper):
    RegistrationPage_Objects = read_locators("RegistrationPage")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def select_gender(self, gender):
        if gender.upper() == 'MALE':
            rdo_male = self.__class__.RegistrationPage_Objects['rdo_gender_male']
            self.click_element(rdo_male)
        else:
            rdo_male = self.__class__.RegistrationPage_Objects['rdo_gender_female']
            self.click_element(rdo_male)

    def enter_firstname(self, fname):
        txt_firstname = self.__class__.RegistrationPage_Objects['txt_firstname']
        self.enter_text(txt_firstname, value=fname)

    def enter_lastname(self, lname):
        txt_lastname = self.__class__.RegistrationPage_Objects['txt_lastname']
        self.enter_text(txt_lastname, value=lname)

    def enter_email(self, email):
        txt_email = self.__class__.RegistrationPage_Objects['txt_email']
        self.enter_text(txt_email, value=email)

    def enter_password(self, pwd):
        txt_password = self.__class__.RegistrationPage_Objects['txt_password']
        self.enter_text(txt_password, value=pwd)

    def confirm_password(self, pwd):
        txt_confirm_password = self.__class__.RegistrationPage_Objects['txt_confirm_password']
        self.enter_text(txt_confirm_password, value=pwd)

    def click_register(self):
        btn_register = self.__class__.RegistrationPage_Objects['btn_register']
        self.click_element(btn_register)

    def confirm_registration(self):
        lbl_register = self.__class__.RegistrationPage_Objects['']
        self.wait_for_element(lbl_register)

    def verify_registered_email(self, fname, lname):
        _xpath = f"//a[text()='{fname}.{lname}@company.com']"
        self.wait_for_element(("xpath", _xpath))
