from selenium.webdriver.common.by import By

class ProductPage:
    product_link = (By.LINK_TEXT, "iMac")
    product_price = (By.XPATH, "//h1[text()='iMac']/following::h2[1]")
    def __init__(self, driver):
        self.driver = driver
    def click_product(self):
        self.driver.find_element(*self.product_link).click()
    def get_price(self):
        return self.driver.find_element(*self.product_price).text