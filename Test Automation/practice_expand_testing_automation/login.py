from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

def test_login():
    driver = webdriver.Chrome()

    driver.get("https://practice.expandtesting.com/login")

    time.sleep(2)

    driver.execute_script("window.scrollBy(0,500);")
    time.sleep(5)

    username = driver.find_element(By.XPATH, "/html/body/main/div[3]/div[2]/div/div[1]/div[2]/div/div/div/form/div/div[1]/input")
    username.send_keys("practice")

    password = driver.find_element(By.ID,"password")
    password.send_keys("SuperSecretPassword!")

    lng_btn = driver.find_element(By.ID,"submit-login")
    lng_btn.click()

    success_lng = driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div")
    assert success_lng.text == "You logged into a secure area!"
    time.sleep(5)

    driver.execute_script("window.scrollBy(0,200);")

    logout_btn = driver.find_element(By.XPATH, "/html/body/main/div[4]/div[2]/div/div/a")
    logout_btn.click()

    success_logout = driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div/b")
    assert success_logout.text == "You logged out of the secure area!"

    time.sleep(2)



