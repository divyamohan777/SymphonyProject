from time import sleep
import random
from selenium import webdriver
import os


def gotoSymphony():
    HOME =os.environ['HOME']
    chrome_driver = webdriver.Chrome(
        HOME+'/PycharmProjects/pythonProject2/SymphonyTest/driver/chromedriver')

    chrome_driver.get('https://my.symphony.com/')
    chrome_driver.maximize_window()
    return chrome_driver


def visualdelay():
    sleep(random.randint(3, 5))
