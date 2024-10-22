from POM import *
from Tests import *

column_names, test_data = read_data('EditReservation', 'test_m2_01')


@parameterized_class(column_names, test_data)
class TestLoginA1(BaseTest):
    def test_m2_01(self):
        print('Running Module 2')
        # self.assertEqual(True, False)
        # Login to Mercury Tours Application
        lp = LoginPage(self.driver)
        lp.enter_user_name()
        lp.enter_password()
        self.assertEqual(False, True)
        # lp.click_login()

        # # Search Flight
        # ff = FindFlightsPage(self.driver)
        # ff.select_trip_type(self.trip_type)
        # ff.select_no_of_passengers(self.passenger_count)
        # ff.select_departing_from(self.departing_from)
        # ff.select_departing_month(self.departing_month)
        # ff.select_departing_date(self.departing_day)
        # ff.select_arriving_in(self.arriving_in)
        # ff.select_returning_month(self.arriving_month)
        # ff.select_returning_date(self.arriving_day)
        # ff.select_service_class(self.travel_class)
        # ff.click_continue()
        #
        # # Select Flight
        # sf = SelectFlightsPage(self.driver)
        # sf.select_depart_flight()
        # sf.select_arrive_flight()
        # sf.click_continue()
        #
        # # Enter Payment Details
        # py = PaymentPage(self.driver)
        # py.enter_first_name(self.first_name)
        # py.enter_last_name(self.last_name)
        # py.select_meal_preference(self.meal_preference)
        # py.select_card_type(self.card_type)
        # py.enter_card_number(self.credit_card_number)
        # py.select_expiration_month(self.exp_month)
        # py.select_expiration_year(self.exp_year)
        # py.click_secure_purchase()
        
        # Verify PNR Creation
