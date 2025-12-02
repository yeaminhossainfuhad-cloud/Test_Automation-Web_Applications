from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_login_():
        # Set up the WebDriver
        driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in PATH

        # Open saucedemo demo site
        driver.get("https://www.saucedemo.com/")

        # Log in
        username_input = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input")
        password_input = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input")
        login_button = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/input")

        username_input.send_keys("standard_user")
        password_input.send_keys("secret_sauce")
        login_button.click()

        # Wait for login to process
        time.sleep(3)

        # Assert login success by checking for the presence of a dashboard element
        # For example, check if the "Dashboard" header or menu is present
        assert driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[2]/div") is not None, "Login failed: Welcome message not found."

        # Close the browser
        driver.quit()