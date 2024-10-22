import pytest
#
#
#
# @pytest.mark.usefixtures('init',scope='class')
# @pytest.mark.parametrize('username, password',[('u1',"p1"),('u2','p2')],scope="class")
# class TestDiffUser:
#     def test_admin(self, username, password):
#         print('entering', username)
#         print('entering', password)
#
#     def test_user(self, username, password):
#         print('entering', username)
#         print('entering', password)
#
#
#
#
#
#
#
#
#
# #
class TestLogin:
    @pytest.mark.dependency()
    def test_login(self):
        print('Running test_login')
        assert True
    @pytest.mark.dependency(depends=['TestLogin::test_login'])
    def test_logout(self):
        print('Runnung test_logout')
