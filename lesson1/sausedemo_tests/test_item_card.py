import time

from selenium.webdriver.common.by import By
from data import *
from locators import *


def test_click_on_picture(driver):
    driver.get(MAIN_PAGE)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(LOGIN)

    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    driver.find_element(By.XPATH, ITEM_RED_TSHORT_PICTURE).click()

    assert ITEM_RED_TSHORT_CARD == driver.current_url


def test_click_on_item_name(driver):
    driver.get(MAIN_PAGE)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(LOGIN)

    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    driver.find_element(By.XPATH, ITEM_RED_TSHORT_NAME).click()

    assert ITEM_RED_TSHORT_CARD == driver.current_url
