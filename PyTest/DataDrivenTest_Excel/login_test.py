import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities import logCreator
from Utilities import excelReader

@pytest.mark.parametrize("username,password",excelReader.get_data(excelReader.get_data("DataDrivenTest_Excel/ExcelFiles/loginData.xlsx","login")))
class TestLogin:
    def test_validlogin(self,username,password):
        logger = logCreator.log_generator()
        self.driver = webdriver.Chrome()
        logger.info("Opened the Webdriver")
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/")
        logger.info("Opened the site")
        self.driver.find_element(By.ID,value = "login2").click()
        time.sleep(5)
        self.driver.find_element(By.ID,value = "loginusername").send_keys(username)
        time.sleep(5)
        self.driver.find_element(By.ID,value="loginpassword").send_keys(password)
        time.sleep(2)
        try :
            login = self.driver.find_element(By.CSS_SELECTOR,"#logInModal > div > div > div.modal-footer > button.btn.btn-primary").click()
            time.sleep(3)
            logger.info("Logged in successfully")
        except Exception:
            print("Invalid data entered")
            logger.info("Invalid username entered, login failed")
        # welcome = self.driver.find_element(By.XPATH,"//a[@id='nameofuser']").text
        # assert welcome == "Welcome Admin"
        print("Program finished")
        self.driver.quit()