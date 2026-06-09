import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:

    def test_validate(self):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("HP")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        assert self.driver.find_element(By.XPATH, "//a[normalize-space()='HP LP3065']").is_displayed()

    def test_invalid(self):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("kiot")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
        kiot = self.driver.find_elements(By.XPATH, "//a[normalize-space()='HP LP3065']")
        assert len(kiot) == 0