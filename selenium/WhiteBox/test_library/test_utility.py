from library.utility import is_palindrome,is_string,is_even,MyExecption
import pytest
# import pytest_dependency
@pytest.fixture(scope="class")
# @pytest.fixture()
def init():
    print('Launching Browser')  #setup
    yield
    print('Closing Browser')    #teardown

class TestAdmin:
    def test_login(self,init):
        print('logging in')

    def test_logout(self,init):
        print('logging out')
#
#
# @pytest.mark.parametrize('username,password',[('u1','p1'),('u2','p2')],scope="class")
# class TestLogin:
#     # @pytest.mark.parametrize('username,password',[('u1','p1'),('u2','p2')],)
#     def test_login(self,username,password):
#         print('logging in')
#         print('Entering',username)
#         print('Entering',password)
#
#
#     def test_logout(self,username,password):
#         print('logging out')
#         print('Entering',username)
#         print('Entering',password)
# #
#
#
# class TestUser:
#     @pytest.mark.dependency()
#     def test_create_user(self):
#         print("testing create user")
#         assert True
#
#     @pytest.mark.dependency(depends=["TestUser::test_create_user"])
#     def test_delete_user(self):
#         print('deleting User')

# @pytest.mark.smoke
# @pytest.mark.regression
# class TestLibrary:
#     #Write test methods..
#     def test_even(self):
#         assert is_even(10)==True
#     @pytest.mark.smoke
#     def test_odd(self):
#         assert is_even(9)==False
#     @pytest.mark.regression
#     @pytest.mark.smoke
#     def test_invalid_number(self):
#         with pytest.raises(TypeError):
#             is_even("10")
#     def test_invalid_number_float(self):
#         with pytest.raises(MyExecption):
#             is_even(10.254)
#
#     def test_palindrome(self):
#         assert is_palindrome('racecar')==True
#
#     def test_not_palindrome(self):
#         assert is_palindrome('hello')==False

# from library.utility import is_palindrome,is_even,is_string, MyExecption
# import pytest
# class TestLibrary:
#     @pytest.mark.run(order=8)
#     def test_iseven(self):
#         assert is_even(14)==True
#
#     @pytest.mark.run(order=10)
#     def test_odd(self):
#         assert is_even(15)==False
#
#     @pytest.mark.run(order=9)
#     def test_evenFloat(self):
#         with pytest.raises(MyExecption):
#             is_even(2.5)
#
#     @pytest.mark.run(order=7)
#     def test_streven(self):
#         with pytest.raises(TypeError):
#             is_even('sarthak')
#
#     @pytest.mark.run(order=6)
#     def test_ispalin(self):
#         assert is_palindrome("racecar")==True
#
#     @pytest.mark.run(order=11)
#     def test_notpalin(self):
#         assert is_palindrome("saftgaj")== False
#
#     @pytest.mark.run(order=12)
#     def test_isstring(self):
#         with pytest.raises(ValueError):
#             is_string(685)
#
#     @pytest.mark.run(order=3)
#     def test_numberStr(self):
#         with pytest.raises(MyExecption):
#             is_string('Sarthak')
