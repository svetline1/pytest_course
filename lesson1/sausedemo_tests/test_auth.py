from selenium.webdriver.common.by import By
import time 


def test_login_form(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys("standard_user")

    driver.find_element(By.XPATH, '//input[@data-test="password"]').send_keys("secret_sauce")

    driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()

    time.sleep(5)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"


def test_login_form_wrong_data(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys("user")

    driver.find_element(By.XPATH, '//input[@data-test="password"]').send_keys("user")

    driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()

    assert driver.find_element(By.XPATH, '//*[@class="error-button"]')

    assert driver.current_url == "https://www.saucedemo.com/"

