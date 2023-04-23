from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Firefox() #ЕСЛИ ИСПОЛЬЗУЕШЬ Chrome замени Firefox -> Chrome в этой строке
    browser.get(link)
    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'third')
    input3.send_keys("ivanpetrov@mail.ru")
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
