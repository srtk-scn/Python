"""Yogesh sir class about storing cookies fron a webpage and used it later whenever we login to again not require to fill the login password feild again

Cookies:- It is a information / Data which is stiored in web browser
1.we can add cookies
2. we can delete the cookies

Session cookies:- 15min, 1hr Small time period
Persistant cookies:- Stored in our machine to long time years / months
1.HTTP protocol(Not Save)(not save info)
2.Statefull HTTP Protocol(save info)"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from settings import chromepath,actiTimeUrl
import time
driver=webdriver.Chrome(chromepath)
driver.get(actiTimeUrl)
# cookie_info={'name':'xyz','value':'xyz123'}
# driver.add_cookie(cookie_info)
# time.sleep(4)
# print("cookie",cookie_info,'is added')
#
# result=driver.get_cookies()
# print('cookies are',result)
# for i in result:
#     print(i)
# driver.delete_cookie('value')
# driver.delete_all_cookies()
# print("result after deleting",result)
# driver.quit()

driver