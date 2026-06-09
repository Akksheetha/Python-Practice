import read_config
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

def test_login(setup_and_teardown):
    driver = setup_and_teardown
    loginclick = driver.find_element(By.XPATH,"//a[@id='login2']").click()
    username = read_config.get_config("login credentials","username")
    user = driver.find_element(By.ID,"loginusername")
    user.send_keys(username)
    password = read_config.get_config("login credentials","password")
    password1 = driver.find_element(By.ID,"loginpassword")
    password1.send_keys(password)
    login = driver.find_element(By.CSS_SELECTOR, "#logInModal > div > div > div.modal-footer > button.btn.btn-primary").click()
    driver.implicitly_wait(3)
    print("Logged in successfully")
