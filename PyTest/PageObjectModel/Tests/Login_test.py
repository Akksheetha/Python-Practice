import pytest
from selenium.webdriver.common.by import By
from Utilities import read_config
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from Pages.LoginPage import LoginPage

@pytest.mark.usefixtures("setup_and_teardown")
class Testlogin:
    
    def test_validLogin(self):
        login = LoginPage(self.driver)
        login.click_dropdown()
        print("Dropdown clicked")
        login.click_login_link()
        print("Login link clicked")
        email = read_config.get_data("Login credentials","email")
        password = read_config.get_data("Login credentials","password")
        login.enter_email(email)
        login.enter_password(password)
        login.click_login_button()
        print("Login button clicked")
        
        