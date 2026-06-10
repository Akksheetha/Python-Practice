import selenium
from selenium import webdriver
from Utilities import read_config
import pytest

@pytest.fixture()
def setup_and_teardown(request):

    driver = webdriver.Chrome()
    driver.maximize_window()

    url = read_config.get_data("basic info","url")
    driver.get(url)
    request.cls.driver = driver
    yield driver

    driver.quit()