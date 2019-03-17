
from selenium import webdriver
import os
import sys


class WebDriverFactory:

    def __init__(self,browser):
        self.browser = browser

    def getLinuxDriverInstance(self):
        if self.browser.lower() == 'firefox':
            return webdriver.Firefox(executable_path='../../driver/geckodriver')
        elif self.browser.lower() == 'chrome':
            print('Please download geckodriver for your version and implement')
            sys.exit()
        elif self.browser.lower() == 'ie':
            print('Please download geckodriver for your version and implement')
            sys.exit()
        elif self.browser.lower() == 'safari':
            print('Please download geckodriver for your version and implement')
            sys.exit()
        else:
            print('print please choose correct browser')
            sys.exit()

    def getWindowsDriverInstance(self):
        if self.browser.lower() == 'firefox':
            return webdriver.Firefox(executable_path='driver/geckodriver')
        elif self.browser.lower() == 'chrome':
            return webdriver.Chrome(executable_path="../../driver/chromedriver.exe")
            sys.exit()
        elif self.browser.lower() == 'ie':
            print('Please download geckodriver for your version and implement')
            sys.exit()
        elif self.browser.lower() == 'safari':
            print('Please download geckodriver for your version and implement')
            sys.exit()
        else:
            print('print please choose correct browser')
            sys.exit()
