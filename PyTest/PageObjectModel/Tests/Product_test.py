import pytest

from Pages.HomePage import HomePage
from Pages.ProductPage import ProductPage

@pytest.mark.usefixtures("setup_and_teardown")
class TestDesktopProduct:
    def test_verify_macbook_price(self):
        home = HomePage(self.driver)
        home.click_desktops()
        home.click_mac()
        product = ProductPage(self.driver)
        product.click_product()
        actual_price = product.get_price()
        print("Price displayed:", actual_price)
        assert actual_price == "$122.00"