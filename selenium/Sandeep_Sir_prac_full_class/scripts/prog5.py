from settings import driver,demoshop
import time
driver.get(demoshop)
driver.find_element("link text",'Register').click()
time.sleep(2)
driver.close()