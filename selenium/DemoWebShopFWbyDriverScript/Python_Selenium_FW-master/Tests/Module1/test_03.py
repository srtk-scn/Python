from parameterized import parameterized_class
from Tests.BaseTest import BaseTest
from POM.RegistrationPage import RegistrationPage
from POM.HomePage import HomePage
from Data import *


column_names, test_data = read_data('Registration', 'test_03')


@parameterized_class(column_names, test_data)
class Test_Registration(BaseTest):
        def test_01(self):
                # Create an Instance to Home Page
                hp = HomePage(self.driver)
                hp.click_register()

                # Registration Page
                rp = RegistrationPage(self.driver)
                rp.select_gender(self.Gender)
                rp.enter_firstname(self.FirstName)
                rp.enter_lastname(self.LastName)
                rp.enter_email(self.Email)
                rp.enter_password(self.Password)
                rp.confirm_password(self.Password)
                rp.click_register()

                # Verify Registration Message is displayed or not
                rp.verify_registered_email(self.FirstName, self.LastName)
