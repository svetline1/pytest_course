from selenium.webdriver.common.by import By
from data import LOGIN, PASSWORD, MAIN_PAGE
from locators import *


def test_add_item_to_cart_from_catalog(driver):
    driver.get(MAIN_PAGE)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(LOGIN)

    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    driver.find_element(By.CSS_SELECTOR, ADD_TO_CART_ITEM_1_BUTTON).click()

    driver.find_element(By.CSS_SELECTOR, CART).click()

    item = driver.find_element(By.CSS_SELECTOR, ITEM_1_IN_CART)

    assert item.is_displayed()


def test_add_item_to_cart_from_item_card(driver):
    driver.get(MAIN_PAGE)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(LOGIN)

    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    driver.find_element(By.XPATH, ITEM_2).click()

    driver.find_element(By.CSS_SELECTOR, ADD_TO_CART_ITEM_2_BUTTON).click()

    driver.find_element(By.CSS_SELECTOR, CART).click()

    assert driver.find_element(By.XPATH, ITEM_2).is_displayed()


