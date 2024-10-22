from Library import *


class SeleniumWrapper:
    def __init__(self, driver):
        self.driver = driver
    
    @wait_
    def enter_text(self, element, *, value):
        locator_type, locator_value = element
        self.driver.find_element(locator_type, locator_value).clear()
        self.driver.find_element(locator_type, locator_value).send_keys(value)
        self.log_message(f'Entered {value} in {locator_value}')
    
    @wait_
    def click_element(self, element):
        locator_type, locator_value = element
        self.driver.find_element(locator_type, locator_value).click()
        self.log_message(f'Clicked on {locator_value}')
    
    @wait_
    def select_list_item(self, element, *, item):
        locator_type, locator_value = element
        web_element = self.driver.find_element(locator_type, locator_value)
        select = Select(web_element)
        if isinstance(item, str):
            select.select_by_visible_text(item)
        else:
            select.select_by_index(item)
        self.log_message(f'Selected item {item} from {locator_value}')
    
    @wait_
    def select_multiple_items(self, element, *, items):
        locator_type, locator_value = element
        web_element = self.driver.find_element(locator_type, locator_value)
        select = Select(web_element)
        select.deselect_all()
        for item in items:
            if isinstance(item, str):
                select.select_by_visible_text(item)
            else:
                select.select_by_index(item)
            self.log_message(f'Selected item {item} from {locator_value}')

    @wait_
    def get_current_selected_item(self, element):
        locator_type, locator_value = element
        web_element = self.driver.find_element(locator_type, locator_value)
        select = Select(web_element)
        return select.first_selected_option.text

    @wait_
    def send_keyboard_input(self, key):
        time.sleep(1)
        if key.upper() not in {'ARROW_DOWN', 'ARROW_UP', 'BACK_SPACE', 'TAB', 'ENTER', 'PAGE_DOWN'}:
            raise ValueError('Keys Can be ',{'ARROW_DOWN', 'ARROW_UP', 'BACK_SPACE', 'TAB', 'ENTER', 'PAGE_DOWN'})
        action = ActionChains(self.driver)
        if key.upper() == 'ARROW_DOWN':
            action.send_keys(Keys.ARROW_DOWN).perform()
            self.log_message('Performed keyboard action Arrow Down')
        elif key.upper() == 'ARROW_UP':
            action.send_keys(Keys.ARROW_UP).perform()
            self.log_message('Performed keyboard action Arrow Up')
        elif key.upper() == 'BACK_SPACE':
            action.send_keys(Keys.BACK_SPACE).perform()
            self.log_message('Performed keyboard action Back Space')
        elif key.upper() == 'ESCAPE':
            action.send_keys(Keys.ESCAPE).perform()
            self.log_message('Performed keyboard action Escape')
        elif key.upper() == 'TAB':
            action.send_keys(Keys.TAB).perform()
            self.log_message('Performed keyboard action Tab')
        elif key.upper() == 'ENTER':
            action.send_keys(Keys.ENTER).perform()
            self.log_message('Performed keyboard action Enter')
    
    @wait_
    def mouse_hover(self, element):
        locator_type, locator_value = element
        action = ActionChains(self.driver)
        element = self.driver.find_element(locator_type, locator_value)
        action.move_to_element(element).perform()
        self.log_message(f'Mouse hovered on {locator_value}')
    
    @wait_(is_alert=True)
    def accept_alert(self):
        alert = Alert(self.driver)
        self.driver.switch_to.alert()
        alert.accept()
        self.log_message('Alert Accepted')
    
    @wait_(is_alert=True)
    def dismiss_alert(self):
        alert = Alert(self.driver)
        self.driver.switch_to.alert()
        alert.dismiss()
        self.log_message('Alert Dismissed')
    
    @wait_(is_alert=True)
    def get_alert_text(self):
        alert = Alert(self.driver)
        self.driver.switch_to.alert()
        return alert.text.strip() if alert.text.strip() else None

    @wait_(enabled=False)
    def get_element_text(self, element):
        locator_type, locator_value = element
        element = self.driver.find_element(locator_type, locator_value)
        return element.text.strip()
    
    def switch_to_window(self, window_index):
        if window_index < len(self.driver.window_handles):
            win_handles = self.driver.window_handles
            self.driver.switch_to.window(win_handles[window_index])
            self.log_message(f'Switched to window index: {window_index}')
        else:
            raise NoSuchWindowException(f'Window index :{window_index} does not exist')
    
    def switch_to_parent_window(self):
        win_handles = self.driver.window_handles
        self.driver.switch_to.window(win_handles[0])
        self.log_message('Switched to Parent window')
    
    def close_window(self, window_index):
        win_handles = self.driver.window_handles
        if window_index < len(win_handles):
            win_handles = self.driver.window_handles
            self.driver.switch_to.window(win_handles[window_index])
            self.driver.close()
            self.log_message(f'Closed window index: {window_index}')
        else:
            raise NoSuchWindowException(f'Window index :{window_index} does not exist')
    
    def close_all_child_window(self):
        handles = self.driver.window_handles
        for index in range(1, len(handles)):
            self.driver.switch_to.window(handles[index])
            self.driver.close()
            self.log_message('Closed all child windows')

    def get_page_title(self):
        return self.driver.title.strip()
    
    def get_web_elements(self, element):
        locator_type, locator_value = element
        return self.driver.find_elements(locator_type, locator_value)
    
    def capture_screen_shot(self):
        p = os.getcwd().split('Tests')[0] + 'Tests'
        if not os.path.isdir(p + '/screenshots'):
            os.chdir(p)
            os.mkdir(p + '/screenshots/')
        _screen_shot_name = self.get_date_time_stamp() + '.png'
        self.driver.save_screenshot(p + '/screenshots/' + _screen_shot_name)
        screen_shot_html = r'&nbsp&nbsp&nbsp&nbsp<a href="../screenshots/' + _screen_shot_name + '">View Screen Shot</a>'
        print(screen_shot_html)
    
    @staticmethod
    def get_date_time_stamp():
        temp_date_time = datetime.datetime.now()
        return str(temp_date_time)[:19].replace(':', '').replace(' ', '_').replace('-', '_')
    
    @staticmethod
    def get_random_number():
        """Returns 6 Digit Random Number"""
        temp_date_time = datetime.datetime.now()
        return str(temp_date_time)[20:]
    
    @staticmethod
    def get_by_type(loc):
        if len(loc) != 2:
            raise AttributeError('Missing Locator ', loc)
        locator_type, locator_value = loc
        if locator_type.upper() not in {'XPATH', 'NAME', 'ID', 'CSS_SELECTOR', 'CLASS_NAME', 'TAG_NAME'}:
            raise ValueError('Invalid Locator Type ', locator_type)
        if locator_type.upper() == 'XPATH':
            return By.XPATH, locator_value
        elif locator_type.upper() == 'NAME':
            return By.NAME, locator_value
        elif locator_type.upper() == 'ID':
            return By.ID, locator_value
        elif locator_type.upper() == 'CSS_SELECTOR':
            return By.CSS_SELECTOR, locator_value
        elif locator_type.upper() == 'CLASS_NAME':
            return By.CLASS_NAME, locator_value
    
    @staticmethod
    def log_message(message):
        print('<br>' + str(message))
    
    @wait_(enabled=False, timeout=5)
    def wait_for_element(self, element):
        pass

