from selenium.webdriver.common.by import By
import time


def test_logout(driver):
    driver.get("https://www.saucedemo.com/")

    url_before = driver.current_url

    driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys("standard_user")

    driver.find_element(By.XPATH, '//input[@data-test="password"]').send_keys("secret_sauce")

    driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()

    driver.find_element(By.ID, 'react-burger-menu-btn').click()
    time.sleep(1)

    driver.find_element(By.ID, 'logout_sidebar_link').click()

    assert url_before == driver.current_url

