from POM import *


class PaymentPage(BasePage):
    PaymentPage_Objects = read_locators('Payments_Page')
    
    def enter_first_name(self, first_name):
        txt_first_name = self.__class__.PaymentPage_Objects['txt_first_name']
        self.enter_text(txt_first_name, value=first_name)
    
    def enter_last_name(self, last_name):
        txt_last_name = self.__class__.PaymentPage_Objects['txt_last_name']
        self.enter_text(txt_last_name, value=last_name)
    
    def select_meal_preference(self, meal_preference):
        lst_meal_preference = self.__class__.PaymentPage_Objects['lst_meal_preference']
        self.select_list_item(lst_meal_preference, item=meal_preference)
    
    def select_card_type(self, card_type):
        lst_card_type = self.__class__.PaymentPage_Objects['lst_card_type']
        self.select_list_item(lst_card_type, item=card_type)
    
    def enter_card_number(self, card_number):
        txt_card_number = self.__class__.PaymentPage_Objects['txt_card_number']
        self.enter_text(txt_card_number, value=card_number)
    
    def select_expiration_month(self, exp_month):
        lst_exp_month = self.__class__.PaymentPage_Objects['lst_exp_month']
        self.select_list_item(lst_exp_month, item=exp_month)
    
    def select_expiration_year(self, exp_year):
        lst_exp_year = self.__class__.PaymentPage_Objects['lst_exp_year']
        self.select_list_item(lst_exp_year, item=exp_year)
    
    def click_secure_purchase(self):
        btn_secure_purchase = self.__class__.PaymentPage_Objects['btn_secure_purchase']
        self.click_element(btn_secure_purchase)
