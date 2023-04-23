from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


browser = webdriver.Firefox()
browser.get("http://suninjuly.github.io/selects1.html")


num1=int(browser.find_element(By.ID, "num1").text)
num2=int(browser.find_element(By.ID, "num2").text)
summa = num1+num2
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(summa))
browser.find_element(By.CLASS_NAME, "btn").click()