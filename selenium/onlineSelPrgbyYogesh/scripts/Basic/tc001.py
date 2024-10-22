chromepath=r'C:\Users\sarthak sachan\PycharmProjects\online_selenium\onlineSelPrg\drivers\chromedriver.exe'
from selenium import webdriver

def Tc_001():
    driver=webdriver.Chrome(executable_path=chromepath)
    # driver= webdriver.Chrome(chromepath)
    appUrl='https://www.google.com'
    driver.get(url=appUrl)
    print('app url '+ appUrl +' enterned')
    driver.close()
    print('chrome closed')
    # driver.get(appUrl)
Tc_001()
#
def Tc_002():
    driver = webdriver.Chrome(executable_path=chromepath)
    driver.get('https://www.gmail.com')
    AppTitle=driver.title
    print(AppTitle)
    if 'gmail'==AppTitle.lower():
        print('enter the user name and password')
    else:
        print('enter a valid url')
        driver.close()
    print('App Titile name is', AppTitle)
# Tc_002()
youTubeUrl='https://www.youtube.com'
googleurl='https://www.google.com'
appUrl='https://www.gmail.com'
actiTimeUrl='https://demo.actitime.com'
def Curr_url():
    driver=webdriver.Chrome(executable_path=chromepath)
    driver.get(url=appUrl)
    url1=driver.current_url
    print('first url is', url1)
    driver.get(url=actiTimeUrl)
    url2=driver.current_url
    print('second url is', url2)
    if url1 != actiTimeUrl:
        print('not actitime page')
    else:
        print('it is actitime page url')
# Curr_url()

def PageCode():
    driver=webdriver.Chrome(executable_path=chromepath)
    driver.get(url=appUrl)
    url1=driver.current_url
    print('first url is \n',url1)
    Page_code=driver.page_source
    print('page code is\n',Page_code)
    driver.close()
# PageCode()



def PageCode():
    driver=webdriver.Chrome(chromepath)
    driver.get(actiTimeUrl)
    driver.maximize_window()
    driver.minimize_window()
    code=driver.page_source
    # print('page source is \n',code)
    import json as j
    c_code=j.dumps(code)
    fileObj=open('actiTimePage.txt','w')
    fileObj.write(c_code)
    fileObj.close()
# PageCode()

def BackMethod():
    driver= webdriver.Chrome(chromepath)
    driver.get(appUrl)
    print(driver.current_url)
    driver.get(youTubeUrl)
    print(driver.current_url)
    driver.back()
    CUR=driver.current_url
    if CUR==appUrl:
        print('back button called')
        driver.refresh()
        print('page refreshed')
        driver.forward()
        currene_url=driver.current_url
        print(currene_url, 'after rfresh')
# BackMethod()


