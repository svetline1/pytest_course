from selenium.webdriver.common.by import By

def test_add_item_to_cart_from_catalog(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys("standard_user")

    driver.find_element(By.XPATH, '//input[@data-test="password"]').send_keys("secret_sauce")

    driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()
    # time.sleep(5)

    driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]').click()

    driver.find_element(By.CSS_SELECTOR, 'a[class="shopping_cart_link"]').click()

    item = driver.find_element(By.CSS_SELECTOR, "a[id='item_4_title_link'] > div[class='inventory_item_name']")

    assert item.is_displayed()


def test_add_item_to_cart_from_item_card(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys("standard_user")

    driver.find_element(By.XPATH, '//input[@data-test="password"]').send_keys("secret_sauce")

    driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()

    driver.find_element(By.XPATH, '//*[contains (text(), "Sauce Labs Bike Light")]').click()

    driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-bike-light"]').click()

    driver.find_element(By.CSS_SELECTOR, 'a[class="shopping_cart_link"]').click()

    item = driver.find_element(By.XPATH, '//*[contains (text(), "Sauce Labs Bike Light")]')

    assert item.is_displayed()


