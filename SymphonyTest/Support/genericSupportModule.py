from time import sleep
import random
from selenium import webdriver
import os
from selenium.webdriver import DesiredCapabilities

symphonyURL = 'https://my.symphony.com/'
HOME = os.environ['HOME']

#Set up for Chrome
def gotoSymphonyChrome():
    driver = webdriver.Chrome(HOME + '/PycharmProjects/pythonProject2/SymphonyTest/driver/chromedriver')
    driver.get(symphonyURL)
    driver.maximize_window()
    return driver

#Set up for edge
def gotoSymphonyEdge():
    cap = DesiredCapabilities().EDGE
    cap["platform"] = "ANY"
    driver = webdriver.Edge(executable_path=HOME + "/PycharmProjects/pythonProject2/SymphonyTest/driver/msedgedriver",
                            capabilities=cap)
    driver.get(symphonyURL)
    driver.maximize_window()
    return driver


def gotoSymphonyFF():
    message = "Browser Not supported"
    return message


def visualdelay():
    sleep(random.randint(3, 5))
