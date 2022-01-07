from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def comment(browser):
    browser.get('https://www.instagram.com/')
    time.sleep(40)
    for i in range(5):
        browser.get('POST LINK')
        commentArea = browser.find_element_by_class_name('Ypffh')
        commentArea.click()
        time.sleep(5)
        commentArea = browser.find_element_by_class_name('Ypffh')
        commentArea.click()
        commentArea.send_keys("Using selenium to comment in burst of 5 ")
        commentArea.send_keys(Keys.RETURN)
        time.sleep(5)
    
    
    
if __name__ == '__main__':
    browser = webdriver.Chrome()
    comment(browser)