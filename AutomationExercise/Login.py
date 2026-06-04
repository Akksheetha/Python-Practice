from selenium.webdriver.common.by import *
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")
driver.maximize_window()
titletext = driver.title
if titletext:
    print("Visiblity of page is successful")
else:
    print("Visiblity of page is failed")
signup = driver.find_element(By.XPATH,"//a[normalize-space()='Signup / Login']")
signup.click()
login = driver.find_element(By.XPATH,"//h2[normalize-space()='Login to your account']")
email = driver.find_element(By.NAME,"email")
email.send_keys("2k22csbs03@kiot.ac.in")
password = driver.find_element(By.NAME,"password")
password.send_keys("Password@1234")
loginbtn = driver.find_element(By.XPATH,"//button[normalize-space()='Login']")
loginbtn.click()
user = driver.find_element(By.XPATH,"//b[normalize-space()='Akkshee']")
if user.is_displayed():
    print("Username visible")
else:
    print("Username  is not visible")




