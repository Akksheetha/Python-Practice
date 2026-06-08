from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")
driver.maximize_window()
wait = WebDriverWait(driver,10)
homepage = driver.find_element(By.XPATH,"//a[normalize-space()='Home']")
if homepage.is_displayed():
    print("HomePage is visible")
else:
    print("HomePage is not visible")
products = driver.find_element(By.XPATH,"//a[@href='/products']")
driver.execute_script("arguments[0].click();",products)
wait.until(EC.text_to_be_present_in_element((By.XPATH, "//h2[@class='title text-center']"), "ALL PRODUCTS"))
all_products = driver.find_element(By.XPATH,"//h2[@class='title text-center']").text
assert "ALL PRODUCTS" in all_products.upper()
print("Navigated to all products page")
view_product = driver.find_element(By.CSS_SELECTOR,"a[href='/product_details/1']")
if view_product.is_displayed():
    print("Product listing is visble")
else:
    print("Product listing is not visible")
driver.execute_script("arguments[0].click();",view_product)
add_to_cart = driver.find_element(By.XPATH,"//button[@type='button']").text
assert add_to_cart == "Add to cart"
print("User can see the product details page")
product_name = driver.find_element(By.XPATH,"//h2[normalize-space()='Blue Top']").text
assert product_name=="Blue Top"
print("Detailed product details is visible")

