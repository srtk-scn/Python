from Library import *
import unittest


class BaseTest(unittest.TestCase):
    def setUp(self):
        print('\n Running setUp')
        if Config.BROWSER_NAME.upper() == 'CHROME':
            self.driver = webdriver.Chrome(executable_path=Config.CHROME_DRIVER_PATH)
        elif Config.BROWSER_NAME.upper() == 'FIREFOX':
            self.driver = webdriver.Firefox(executable_path=Config.FIREFOX_DRIVER_PATH)
        else:
            self.driver = webdriver.Ie(Config.IE_DRIVER_PATH)
        self.driver.get(Config.URL)
        self.driver.maximize_window()

    def tearDown(self):
        print('\n Running teardown')
        sw = SeleniumWrapper(self.driver)
        try:
            sw.capture_screen_shot()
        except Exception as e:
            print(e)
        finally:
            self.driver.quit()

