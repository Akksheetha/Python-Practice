from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://automationexercise.com")
driver.maximize_window()
assert "Automation Exercise" in driver.title
driver.find_element(By.LINK_TEXT, "Signup / Login").click()
login_text = driver.find_element(By.XPATH, "//h2[text()='Login to your account']").text
assert login_text == "Login to your account"
driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("wrong@test.com")
driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys("wrongpassword")
driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()
error_msg = driver.find_element(By.XPATH,"//p[text()='Your email or password is incorrect!']").text
assert error_msg == "Your email or password is incorrect!"
print("Test Passed")
time.sleep(3)
driver.quit()