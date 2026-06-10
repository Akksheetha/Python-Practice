from selenium.webdriver.common.by import By

class HomePage:
    desktops_menu = (By.LINK_TEXT, "Desktops")
    mac_option = (By.LINK_TEXT, "Mac (1)")
    def __init__(self, driver):
        self.driver = driver
    def click_desktops(self):
        self.driver.find_element(*self.desktops_menu).click()
    def click_mac(self):
        self.driver.find_element(*self.mac_option).click()