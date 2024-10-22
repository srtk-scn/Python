from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from settings import chromepath,demoshop
driver=webdriver.Chrome(chromepath)
driver.get("https://www.naukri.com/")
time.sleep(4)
# driver.close()  #this will close the currently opened browser only parent window
# driver.quit()  # this will close all the opened tabs parent window and all the child window
wins=driver.window_handles
for win in wins:
    driver.switch_to.window(win)
    print(win)
    print(win.title)
    driver.close()
# driver.quit()
# driver.switch_to.window(wins[1])
# driver.close()
# driver.switch_to.window(wins[2])
# driver.close()
# driver.switch_to.window(wins[3])
# driver.quit()

# print(wins)
# for win in wins:
#     driver.switch_to.window(win)
#     driver.close()
#     time.sleep(1)
# print(reversed(wins))
# for win in reversed(wins):
#     driver.switch_to.window(win)
#     print(driver.title)
#     driver.close()
#     time.sleep(1)

# win_handles=driver.window_handles
# for win_handle in win_handles:
#     print(win_handle)
# for win_id in win_handles:
#     driver.switch_to.window(win_id)
#     _title=driver.title
#     print(_title)
#     if _title=='Amazon':
#         driver.close()
# win_handle=driver.window_handles
# driver.switch_to.window(win_handle[1])
# driver.close()
# time.sleep(3)
# driver.quit()
# driver.get(demoshop)
#
# driver.find_element_by_xpath('//a[text()="Facebook"]').click()
# time.sleep(2)
# wins=driver.window_handles
# driver.switch_to.window(wins[1])
# driver.close()
