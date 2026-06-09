
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def setup_and_teardown():
    driver = webdriver.Chrome()
    driver.get("http://demoblaze.com/")
    driver.maximize_window()
    driver.implicitly_wait(3)

    yield driver

    driver.quit()