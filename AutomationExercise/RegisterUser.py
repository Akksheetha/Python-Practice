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
visiblity = driver.find_element(By.XPATH,"//h2[normalize-space()='New User Signup!']")
if visiblity.is_displayed():
    print("New User Sign Up Visible")
else:
    print("New User Sign Up is not Visible")
name = driver.find_element(By.NAME,"name")
name.send_keys("Akkshee")
email = driver.find_element(By.NAME,"email")
email.send_keys("2k22csbs03@kiot.ac.in")
signupbtn = driver.find_element(By.XPATH,"//button[normalize-space()='Signup']")
# signupbtn.click()



