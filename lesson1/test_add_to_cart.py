from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_add_item_to_cart_from_catalog():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    text_before = driver.find_element(By.CSS_SELECTOR, "a[id='item_4_title_link'] > div[class='inventory_item_name']").text

    button_add_to_cart = driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]')
    button_add_to_cart.click()

    cart_button = driver.find_element(By.CSS_SELECTOR, 'a[class="shopping_cart_link"]')
    cart_button.click()

    text_after = driver.find_element(By.CSS_SELECTOR, "a[id='item_4_title_link'] > div[class='inventory_item_name']").text
    assert text_before == text_after

    driver.quit()


def test_add_item_to_cart_from_item_card():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    item_name = driver.find_element(By.XPATH, '//*[contains (text(), "Sauce Labs Bike Light")]')
    item_name.click()

    text_before = driver.find_element(By.XPATH, '//*[contains (text(), "Sauce Labs Bike Light")]').text

    button_add_to_cart = driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-bike-light"]')
    button_add_to_cart.click()

    cart_button = driver.find_element(By.CSS_SELECTOR, 'a[class="shopping_cart_link"]')
    cart_button.click()

    text_after = driver.find_element(By.XPATH, '//*[contains (text(), "Sauce Labs Bike Light")]').text
    assert text_before == text_after

    driver.quit()


