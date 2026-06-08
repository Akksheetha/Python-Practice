from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")
driver.maximize_window()

homepage = driver.find_element(By.XPATH, "//a[normalize-space()='Home']")

if homepage.is_displayed():
    print("HomePage is visible")
else:
    print("HomePage is not visible")

product = driver.find_element(By.XPATH, "//a[@href='/products']")
driver.execute_script("arguments[0].click();", product)

actions = ActionChains(driver)

first_product = driver.find_element(
    By.XPATH,
    "(//div[@class='product-image-wrapper'])[1]"
)

actions.move_to_element(first_product).perform()

first_add_to_cart = driver.find_element(
    By.XPATH,
    "(//a[contains(text(),'Add to cart')])[1]"
)

driver.execute_script(
    "arguments[0].click();",
    first_add_to_cart
)

time.sleep(2)

continue_shopping = driver.find_element(
    By.XPATH,
    "//button[normalize-space()='Continue Shopping']"
)

driver.execute_script(
    "arguments[0].click();",
    continue_shopping
)

second_product = driver.find_element(
    By.XPATH,
    "(//div[@class='product-image-wrapper'])[2]"
)

actions.move_to_element(second_product).perform()

second_add_to_cart = driver.find_element(
    By.XPATH,
    "(//a[contains(text(),'Add to cart')])[2]"
)

driver.execute_script(
    "arguments[0].click();",
    second_add_to_cart
)

time.sleep(2)

view_cart = driver.find_element(
    By.XPATH,
    "//u[normalize-space()='View Cart']"
)

driver.execute_script(
    "arguments[0].click();",
    view_cart
)

products = driver.find_elements(
    By.XPATH,
    "//tr[contains(@id,'product')]"
)

if len(products) == 2:
    print("Both products are added to cart")
else:
    print("Products are not added properly")

price1 = driver.find_element(
    By.XPATH,
    "(//td[@class='cart_price'])[1]"
).text

price2 = driver.find_element(
    By.XPATH,
    "(//td[@class='cart_price'])[2]"
).text

quantity1 = driver.find_element(
    By.XPATH,
    "(//td[@class='cart_quantity'])[1]"
).text

quantity2 = driver.find_element(
    By.XPATH,
    "(//td[@class='cart_quantity'])[2]"
).text

total1 = driver.find_element(
    By.XPATH,
    "(//td[@class='cart_total'])[1]"
).text

total2 = driver.find_element(
    By.XPATH,
    "(//td[@class='cart_total'])[2]"
).text

print("Product 1 Price :", price1)
print("Product 1 Quantity :", quantity1)
print("Product 1 Total :", total1)

print("Product 2 Price :", price2)
print("Product 2 Quantity :", quantity2)
print("Product 2 Total :", total2)

time.sleep(3)
driver.quit()