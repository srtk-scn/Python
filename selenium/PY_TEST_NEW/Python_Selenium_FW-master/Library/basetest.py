from Library import *
import pytest


@pytest.fixture()
def init(request):
    if Config.BROWSER_NAME.upper() == 'CHROME':
        driver = webdriver.Chrome(executable_path=Config.CHROME_DRIVER_PATH)
    elif Config.BROWSER_NAME.upper() == 'FIREFOX':
        driver = webdriver.Firefox(executable_path=Config.FIREFOX_DRIVER_PATH)
    else:
        driver = webdriver.Ie(Config.IE_DRIVER_PATH)
    driver.get(Config.URL)
    driver.maximize_window()
    # cls is the name of the class from where init fixture is being called
    request.cls.driver = driver
    yield
    driver.quit()
