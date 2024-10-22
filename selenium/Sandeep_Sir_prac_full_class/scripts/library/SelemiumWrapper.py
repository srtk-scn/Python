from scripts.library import *
from scripts.library.Config import Config
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
class Wrapper:
    def __init__(self):
        self.driver=None

    def launch_url(self):
        browser=Config.BROWSER_TYPE
        if browser.upper()=="CHROME":
            self.driver=webdriver.Chrome(executable_path=Config.CHROME_DRIVER)
        elif browser.upper() == 'FIREFOX':
            self.driver = webdriver.Firefox(Config.GECKO_DRIVER)
        elif browser.upper() == 'SAFARI':
            self.driver = webdriver.Safari()
        self.driver.get(Config.URL)
        time.sleep(3)
    def click_element(self,locator):
        locatortype,locatorvalue=locator
        self.driver.find_element(locatortype,locatorvalue).click()


    def enter_text(self,locator,value):
        locatortype, locatorvalue = locator
        self.driver.find_element(locatortype, locatorvalue).send_keys(value.strip())

    def select_item(self,locator,item):
        locatortype, locatorvalue = locator
        lst_box=self.driver.find_element(locatortype,locatorvalue)
        select=Select(lst_box)
        if isinstance(item,str):
            select.select_by_visible_text(item)
        else:
            select.select_by_index(item)

    def select_multiple_items(self,locator,items):
        locatortype, locatorvalue = locator
        lst_box = self.driver.find_element(locatortype, locatorvalue)
        select = Select(lst_box)
        for item in items:
            if isinstance(item,str):
                select.select_by_visible_text(item)
                time.sleep(1)
            else:
                select.select_by_index(item)
                time.sleep(1)
    def get_current_selected_item(self,locator):
        locatortype, locatorvalue = locator
        lst_box = self.driver.find_element(locatortype, locatorvalue)
        select = Select(lst_box)
        return select.first_selected_option.text

    def mouse_hover(self,locator):
        locator_type, locator_value = locator
        element = self.driver.find_element(locator_type, locator_value)
        actions=ActionChains(self.driver)
        actions.move_to_element(element).perform()

    # driver.get("F:\selenium\Sandeep_Sir\scripts\HTML FILES\Hovarable.html")
    # mouse_hover(('xpath',"//a[text()='About']"))

    def send_keyboard_input(self,key):
        if not key.upper() in {'PAGE_DOWN', 'PAGE_UP', 'ARROW_UP', 'ARROW_DOWN', 'ENTER', 'ESCAPE', 'TAB'}:
            raise ValueError(f'Invalid passed key {key}')
        actions = ActionChains(self.driver)
        if key.upper() == 'PAGE_DOWN':
            actions.send_keys(Keys.PAGE_DOWN).perform()
        elif key.upper() == 'PAGE_UP':
            actions.send_keys(Keys.PAGE_UP).perform()
        elif key.upper() == 'ARROW_UP':
            actions.send_keys(Keys.ARROW_UP).perform()
        elif key.upper() == 'ARROW_DOWN':
            actions.send_keys(Keys.ARROW_DOWN).perform()
        elif key.upper() == 'ENTER':
            actions.send_keys(Keys.ENTER).perform()
        elif key.upper() == 'ESCAPE':
            actions.send_keys(Keys.ESCAPE).perform()
        elif key.upper() == 'TAB':
            actions.send_keys(Keys.TAB).perform()

    def close_application(self):
        self.driver.quit()
# w = Wrapper()
# w.launch_url()
# w.click_element(("link text", "Register"))
# w.click_element(("id", "gender-male"))
# w.enter_text(("name", "FirstName"), "Sandeep")
# w.enter_text(("name", "LastName"), "Suryaprasad")
# w.click_element(("id", "register-button"))
# time.sleep(3)
# w.close_application()