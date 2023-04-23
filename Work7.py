from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

browser = webdriver.Firefox()
link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser.get(link)
btn = browser.find_element(By.TAG_NAME, 'button').click()
alert = browser.switch_to.alert
alert.accept()
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[0])
time.sleep(0.5)
x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]').text
y = calc(x_element)
inp = browser.find_element(By.ID, "answer")
inp.send_keys(y)
btn2 = browser.find_element(By.CLASS_NAME,"btn-primary")
btn2.click()

