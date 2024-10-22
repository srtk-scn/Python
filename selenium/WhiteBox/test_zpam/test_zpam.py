from zpam.zpam import is_armstrong
import pytest
def test_armstrong():
    assert is_armstrong(153)==True

def test_not_arms():
    assert is_armstrong(45)==False

from test_practice.conftest import init
@pytest.mark.usefixtures("init")
class TestAuth:
    def test_login(self):
        print("Test Login")
        assert True == True