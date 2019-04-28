#import requests
import os
import sys
import urllib
from urllib.request import urlopen
import time
import re
#from bs4 import BeautifulSoup
import sys
import argparse
import zipfile
import urllib



#SELENIUM_SITE = 'https://www.seleniumhq.org/download/'

CHROME = 'https://chromedriver.storage.googleapis.com/74.0.3729.6/chromedriver_win32.zip'
FF = 'https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-win64.zip'
OPERA = 'https://github.com/operasoftware/operachromiumdriver/archive/v.2.42.zip'
GHOSTDRIVER = 'https://github.com/detro/ghostdriver/archive/2.1.0.zip'
HTMLUNITDRIVER = 'https://github.com/SeleniumHQ/htmlunit-driver/archive/2.34.0.zip'

drivers_dict = {CHROME:'/gh.zip', FF:'/ff.zip', OPERA:'/opera.zip', GHOSTDRIVER:'/ghost.zip', HTMLUNITDRIVER:'/html.zip'}


def create_download_directory():
    current_directory = os.getcwd()
    download_directory = os.path.join(current_directory, r'binaries')
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)

    return download_directory

def drivers_scrap(dict, directory):
    for browser in dict:
        current = directory + dict[browser]
        print(dict[browser])
        urllib.request.urlretrieve(browser, current)
        with zipfile.ZipFile(current, 'r') as zipobj:
            zipobj.extractall(directory)


def final_derectory():
    parser = argparse.ArgumentParser(description='get_directory_name')
    try:
        parser.add_argument("directory")
        args = parser.parse_args()
        dir = args.directory
    except:
       dir = create_download_directory()
    return dir


def main():
    try:
        directory_to_download = final_derectory()
        dowload = drivers_scrap(drivers_dict, directory_to_download)

    except Exception as e:
        print('Exception:', e)
        exit(1)


if __name__ == "__main__":
        main()