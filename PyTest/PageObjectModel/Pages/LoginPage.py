from selenium.webdriver.common.by import By

class LoginPage:

    dropdown = (By.XPATH, "//span[@class='caret']")
    login_link = (By.XPATH, "//a[text()='Login']")
    email = (By.NAME, "email")
    password = (By.NAME, "password")
    loginbtn = (By.XPATH, "//input[@value='Login']")
    def __init__(self, driver):
        self.driver = driver
    def click_dropdown(self):
        self.driver.find_element(*self.dropdown).click()
    def click_login_link(self):
        self.driver.find_element(*self.login_link).click()
    def enter_email(self, email):
        self.driver.find_element(*self.email).send_keys(email)
    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)
    def click_login_button(self):
        self.driver.find_element(*self.loginbtn).click()