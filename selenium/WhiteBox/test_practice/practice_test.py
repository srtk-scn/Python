# from practice.practice import is_palindrome,is_even
import pytest
#
#
# @pytest.mark.usefixtures('init')
# class TestPractice:
#     @pytest.mark.run(order=4)
#     def test_even(self):
#         assert is_even(10)==True
#     @pytest.mark.run(order=5)
#     def test_palindrome(self):
#         print("SARTHAKK")
#         assert is_palindrome('racecar')==True
#     @pytest.mark.run(order=7)
#     def test_invalid(self):
#         assert is_even(1)==False
#     @pytest.mark.run(order=6)
#     def test_float(self):
#         with pytest.raises(ValueError):
#             is_even(4.2)
#
#     @pytest.mark.run(order=3)
#     def test_string(self):
#         with pytest.raises(TypeError):
#             is_even('sart')
#     @pytest.mark.regression
#     @pytest.mark.run(order=2)
#     def test_invalid_p(self):
#         with pytest.raises(TypeError):
#             is_palindrome(123)
#     @pytest.mark.smoke
#     @pytest.mark.run(order=1)
#     def test_not_palindrome(self):
#         assert is_palindrome('hello')==False

# from selenium import webdriver
#
# @pytest.fixture()
# def init():
#     driver=webdriver.Chrome()

# @pytest.mark.usefixtures("init")
# class TestAuth:
#     def test_login(self):
#         print("Test Login")
#         assert True == True


@pytest.mark.usefixtures("init")
class Test_:
    def test_log(self):
        print('login')
        assert True