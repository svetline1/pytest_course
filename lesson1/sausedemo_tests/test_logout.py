from selenium.webdriver.common.by import By
import time
from data import MAIN_PAGE, LOGIN, PASSWORD
from locators import *

def test_logout(driver):
    driver.get(MAIN_PAGE)

    url_before = driver.current_url

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(LOGIN)

    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    driver.find_element(By.ID, BURGER_MENU).click()
    time.sleep(1)

    driver.find_element(By.ID, BURGER_LOG_OUT).click()

    assert url_before == driver.current_url

