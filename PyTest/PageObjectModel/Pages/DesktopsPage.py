from selenium.webdriver.common.by import By

class DesktopsPage:

    hp_product = (By.LINK_TEXT, "HP LP3065")
    def __init__(self, driver):
        self.driver = driver
    def select_hp_product(self):
        self.driver.find_element(*self.hp_product).click()