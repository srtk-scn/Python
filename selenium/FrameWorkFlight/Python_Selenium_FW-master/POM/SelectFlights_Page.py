from POM import *


class SelectFlightsPage(BasePage):
    SelectFlights_Objects = read_locators('Select_Flights_Page')
    
    def select_depart_flight(self):
        rdo_depart = self.__class__.SelectFlights_Objects['rdo_depart']
        self.click_element(rdo_depart)
    
    def select_arrive_flight(self):
        rdo_return = self.__class__.SelectFlights_Objects['rdo_return']
        self.click_element(rdo_return)
    
    def click_continue(self):
        btn_continue = self.__class__.SelectFlights_Objects['btn_continue']
        self.click_element(btn_continue)