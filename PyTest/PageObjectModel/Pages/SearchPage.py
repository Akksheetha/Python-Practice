from selenium.webdriver.common.by import By

class SearchPage:

    search_box = (By.NAME, "search")
    search_button = (By.XPATH, "//button[contains(@class,'btn-default')]")
    no_product_message = (By.XPATH,"//input[@id='button-search']/following-sibling::p")
    def __init__(self, driver):
        self.driver = driver
    def enter_product(self, product):
        self.driver.find_element(*self.search_box).send_keys(product)
    def click_search(self):
        self.driver.find_element(*self.search_button).click()
    def search_product(self, product):
        self.enter_product(product)
        self.click_search()
    def is_product_displayed(self, product_name):
        return self.driver.find_element(By.LINK_TEXT,product_name).is_displayed()
    def get_no_product_message(self):
        return self.driver.find_element(*self.no_product_message).text