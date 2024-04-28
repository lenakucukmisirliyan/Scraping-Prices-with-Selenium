from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://vakiflilezzetleri.com")

product_elements = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_all_elements_located((
    By.CLASS_NAME, "wb-store-item")))

for product in product_elements:
    product_name_element = product.find_element(By.CLASS_NAME, "wb-store-name")
    product_price_element = product.find_element(By.CLASS_NAME, "wb-store-price")

    product_name = product_name_element.text
    product_price = product_price_element.text

    print(f"{product_name} : {product_price}")

driver.quit()