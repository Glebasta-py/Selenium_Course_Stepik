from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Firefox() #ЕСЛИ ИСПОЛЬЗУЕШЬ Chrome замени Firefox -> Chrome в этой строке
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys(y)
    input2 = browser.find_element(By.ID, 'robotCheckbox')
    input2.click()
    input3 = browser.find_element(By.ID, "robotsRule")
    input3.click()
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(30)
    browser.quit()