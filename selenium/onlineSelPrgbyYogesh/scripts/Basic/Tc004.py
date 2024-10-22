from selenium import webdriver
from onlineSelPrg.setting import chromepath,actiTimeUrl
driver=webdriver.Chrome(executable_path=chromepath)
from onlineSelPrg.scripts.locators import getWebElement

# result=getWebElement('id','username')
# print(result)
def LoginPage():
    print('start')
    Username='admin'
    Password='manager'
    userTextLoc='id'
    userTextValue='username'
    pwdTextLoc='class'
    pwdTextValue="textField pwdfield"
    print('start of get element')
    userWebEle=getWebElement(userTextLoc,userTextValue)
    print(userWebEle)
    print('ID element done')
    # print('pwd feild begins')
    # pwdWebEle=getWebElement(pwdTextLoc,pwdTextValue)
    # print(pwdWebEle)
    # print('pwd feild done')
    print('end of login')
# LoginPage()


def user_input():
    Username = 'admin'
    Password = 'manager'
    userTextLoc = 'id'
    userTextValue = 'username'
    print('get start')
    userWebEle=getWebElement(userTextLoc,userTextValue)
    print(userWebEle)

user_input()
driver.quit()