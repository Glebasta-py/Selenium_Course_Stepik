from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

#Работа с отправкой файла на Selenium
link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'example.txt')
try:
    browser = webdriver.Firefox()
    browser.get(link)
    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys("ivanpetrov@mail.ru")
    input3 = browser.find_element(By.NAME, 'file')
    input3.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
