from spam.spam import fact,square,cube,My_favorite_Exception
import pytest

class TestSpam:
    @pytest.mark.run(order=4)
    def test_square(self):
        assert square(5)==25

    @pytest.mark.run(order=13)
    def test_invalid_square(self):
        with pytest.raises((TypeError,ValueError)):
            square("sarthak")

    @pytest.mark.run(order=5)
    def test_fact(self):
        assert fact(5)==120

    @pytest.mark.run(order=1)
    def test_cube(self):
        assert cube(5)==125

    @pytest.mark.run(order=2)
    def test_invalid_cube(self):
        with pytest.raises(My_favorite_Exception):
            cube("golu")