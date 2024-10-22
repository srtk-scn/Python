from POM import *
from Tests import *


column_names, test_data = read_data('Reservation', 'test_01')


@parameterized_class(column_names, test_data)
class TestLogin_01(BaseTest):
        def test_01(self):
                print('Running login test')
                # Login to Mercury Tours Application
                lp = LoginPage(self.driver)
                lp.enter_user_name()
                lp.enter_password()
                self.assertEqual(True, False)
                # lp.click_login()
                # Search Flight
                # ff = FindFlightsPage(self.driver)
                # ff.select_trip_type(self.TripType)
                # ff.select_no_of_passengers(self.Passengers)
                # ff.select_departing_from(self.DepartingFrom)
                # ff.select_departing_month(self.OnMonth)
                # ff.select_departing_date(self.OnDate)
                # ff.select_arriving_in(self.ArrivingIn)
                # ff.select_returning_month(self.ReturingMonth)
                # ff.select_returning_date(self.ReturningDate)
                # ff.select_service_class(self.ServiceClass)
                # ff.click_continue()
                # #
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
                #
                # Verify PNR Creation
