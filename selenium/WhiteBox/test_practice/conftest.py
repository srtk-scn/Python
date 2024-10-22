# import pytest
# @pytest.fixture()
# def init():
#     print('Launching Browser and Navigating to a URL')
#     yield
#     print('Closing Browser')

import pytest
@pytest.fixture()
def init():
    print('lauching browser')
    yield
    print('closing browser')