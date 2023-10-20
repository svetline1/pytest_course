from selenium.webdriver.common.by import By
from data import MAIN_PAGE, LOGIN, PASSWORD
from locators import *
import time

def test_remove_item_from_cart(driver):
    driver.get(MAIN_PAGE)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(LOGIN)

    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    driver.find_element(By.CSS_SELECTOR, ADD_TO_CART_ITEM_2_BUTTON).click()

    driver.find_element(By.CSS_SELECTOR, CART).click()

    driver.find_element(By.CSS_SELECTOR, REMOVE_FROM_CART_ITEM_2_BUTTON).click()

    assert driver.find_element(By.XPATH, REMOVED_CART_ITEM)



