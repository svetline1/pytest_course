from selenium.webdriver.common.by import By


def test_remove_item_from_cart(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH, '//input[@data-test="username"]').send_keys("standard_user")

    driver.find_element(By.XPATH, '//input[@data-test="password"]').send_keys("secret_sauce")

    driver.find_element(By.XPATH, '//input[@data-test="login-button"]').click()

    driver.find_element(By.CSS_SELECTOR, 'button[data-test="add-to-cart-sauce-labs-backpack"]').click()

    driver.find_element(By.CSS_SELECTOR, 'a[class="shopping_cart_link"]').click()

    driver.find_element(By.ID, 'remove-sauce-labs-backpack').click()

    assert driver.find_element(By.XPATH, '//div[@class="removed_cart_item"]')



