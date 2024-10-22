chromepath=r'C:\Users\sarthak sachan\PycharmProjects\online_selenium\onlineSelPrg\drivers\chromedriver.exe'
from selenium import webdriver
youTubeUrl='https://www.youtube.com'
googleurl='https://www.google.com'
appUrl='https://www.gmail.com'
actiTimeUrl='https://demo.actitime.com'
driver=webdriver.Chrome(chromepath)
import time
def SetWindow():
    driver=webdriver.Chrome(chromepath)
    driver.get(googleurl)
    driver.maximize_window()
    # driver.set_window_size(800,900)
    # time.sleep(6)
    # driver.set_window_position(450,350)
    # time.sleep(6)
    driver.set_window_rect(350,400,500,400)
    time.sleep(5)
    WinSize=driver.get_window_size() #used to return the size of the window in dictionary format
    WinPos=driver.get_window_position()#used to return the position of the window in dictionary format
    WinRect=driver.get_window_rect()#used to return the x and y coordinates of the window in dictionary format
    print('Window size', WinSize,'Window position',WinPos,'Window Rect',WinRect)
SetWindow()