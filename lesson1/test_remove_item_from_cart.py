from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

def test_remove_item_from_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    button_add_to_cart = driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]')
    button_add_to_cart.click()

    cart_button = driver.find_element(By.CSS_SELECTOR, 'a[class="shopping_cart_link"]')
    cart_button.click()

    remove_button = driver.find_element(By.ID, 'remove-sauce-labs-backpack')
    remove_button.click()

    removed_cart_item = driver.find_element(By.XPATH, '//div[@class="removed_cart_item"]')
    assert removed_cart_item

    driver.quit()

