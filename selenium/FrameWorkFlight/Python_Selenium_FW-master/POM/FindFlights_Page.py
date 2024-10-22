from POM import *
from Library import *


class FindFlightsPage(BasePage):
    FindFlightsPage_Objects = read_locators('Find_Flights_Page')

    def select_trip_type(self, trip_type):
        if trip_type.upper() in ['ROUND TRIP', 'ROUND_TRIP']:
            rdo_round_trip = self.__class__.FindFlightsPage_Objects['rdo_round_trip']
            self.click_element(rdo_round_trip)
        else:
            rdo_round_trip = self.__class__.FindFlightsPage_Objects['rdo_one_way']
            self.click_element(rdo_round_trip)
    
    def select_no_of_passengers(self, passenger_number):
        lst_passenger_count = self.__class__.FindFlightsPage_Objects['lst_passenger_count']
        self.select_list_item(lst_passenger_count, item=int(passenger_number))
        
    def select_departing_from(self, departing_from):
        lst_departing_from = self.__class__.FindFlightsPage_Objects['lst_departing_from']
        self.select_list_item(lst_departing_from, item=departing_from)
    
    def select_departing_month(self, departing_month):
        lst_from_month = self.__class__.FindFlightsPage_Objects['lst_from_month']
        self.select_list_item(lst_from_month, item=departing_month)
    
    def select_departing_date(self, departing_date):
        lst_from_day = self.__class__.FindFlightsPage_Objects['lst_from_day']
        self.select_list_item(lst_from_day, item=departing_date)
    
    def select_arriving_in(self, arriving_in):
        lst_arriving_in = self.__class__.FindFlightsPage_Objects['lst_arriving_in']
        self.select_list_item(lst_arriving_in, item=arriving_in)
    
    def select_returning_month(self, returning_from):
        lst_to_month = self.__class__.FindFlightsPage_Objects['lst_to_month']
        self.select_list_item(lst_to_month, item=returning_from)
    
    def select_returning_date(self, returning_date):
        lst_to_day = self.__class__.FindFlightsPage_Objects['lst_to_day']
        self.select_list_item(lst_to_day, item=returning_date)
    
    def select_service_class(self, service_class):
        if service_class.upper() in ['ECONOMY CLASS', 'ECONOMY_CLASS']:
            rdo_economy_class = self.__class__.FindFlightsPage_Objects['rdo_economy_class']
            self.click_element(rdo_economy_class)
        elif service_class.upper() in ['BUSINESS CLASS', 'BUSINESS_CLASS']:
            rdo_business_class = self.__class__.FindFlightsPage_Objects['rdo_business_class']
            self.click_element(rdo_business_class)
        else:
            rdo_first_class = self.__class__.FindFlightsPage_Objects['rdo_first_class']
            self.click_element(rdo_first_class)
    
    def click_continue(self):
        btn_continue = self.__class__.FindFlightsPage_Objects['btn_continue']
        self.click_element(btn_continue)
