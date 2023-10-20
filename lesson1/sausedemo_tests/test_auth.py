from selenium.webdriver.common.by import By
from data import LOGIN, PASSWORD, MAIN_PAGE, WRONG_LOGIN, WRONG_PASSWORD, INVENTORY_PAGE
from locators import *
import time 


def test_login_form(driver):
    driver.get(MAIN_PAGE)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(LOGIN)

    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    time.sleep(3)
    assert driver.current_url == INVENTORY_PAGE


def test_login_form_wrong_data(driver):
    driver.get(MAIN_PAGE)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(WRONG_LOGIN)

    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(WRONG_PASSWORD)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    assert driver.find_element(By.XPATH, ERROR_BUTTON)

    assert driver.current_url == MAIN_PAGE

