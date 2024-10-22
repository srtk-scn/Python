import os
class Config:

    project_dir = os.getcwd().split('Tests')[0]
    data_file_path = project_dir+'Data/TestData.xls'
    objects_file_path = project_dir+'Data/Objects.xlsx'

    URL = r'http://www.newtours.demoaut.com/'
    BROWSER_NAME = "chrome"
    USERNAME = "mercury"
    PASSWORD = "mercury"
    FIREFOX_DRIVER_PATH = r""
    GECKO_DRIVER_PATH = r""
    CHROME_DRIVER_PATH = project_dir+"Library/chromedriver"
    IE_DRIVER_PATH = r""
    DATA_FILE_PATH = data_file_path
    OBJECTS_FILE_PATH = objects_file_path