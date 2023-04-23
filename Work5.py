from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Firefox()
browser.get("http://suninjuly.github.io/execute_script.html")


number = browser.find_element(By.ID, "input_value").text
res=calc(number)

inp1 = browser.find_element(By.ID, "answer")
inp1.send_keys(str(res))
browser.execute_script("document.querySelector('footer').remove()")
check = browser.find_element(By.ID, "robotCheckbox").click()
radio = browser.find_element(By.ID, "robotsRule").click()
btn = browser.find_element(By.CLASS_NAME, 'btn-primary').click()
