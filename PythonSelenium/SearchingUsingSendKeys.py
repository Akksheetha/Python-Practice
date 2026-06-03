from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
element = driver.find_element(By.NAME,"q")
element.send_keys("Selenium", Keys.ENTER)
print("Entered selenium")
time.sleep(5)
driver.quit()