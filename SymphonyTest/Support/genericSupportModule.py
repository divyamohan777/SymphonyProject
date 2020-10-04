from time import sleep
import random
from selenium import webdriver
import os
from selenium.webdriver import DesiredCapabilities


def gotoSymphonyChrome():
    HOME = os.environ['HOME']
    driver = webdriver.Chrome(HOME + '/PycharmProjects/pythonProject2/SymphonyTest/driver/chromedriver')
    driver.get('https://my.symphony.com/')
    driver.maximize_window()
    return driver



def gotoSymphonyEdge():
    HOME = os.environ['HOME']
    cap = DesiredCapabilities().EDGE
    cap["platform"] = "ANY"
    driver = webdriver.Edge(executable_path=HOME + "/PycharmProjects/pythonProject2/SymphonyTest/driver/msedgedriver", capabilities=cap)
    driver.get('https://my.symphony.com/')
    driver.maximize_window()
    return driver

def visualdelay():
    sleep(random.randint(3, 5))
