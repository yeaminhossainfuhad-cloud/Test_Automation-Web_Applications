import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

def test_serach():
    driver = webdriver.Chrome()  # 1. Open the Google Chrome

    driver.get("https://jpetstore.aspectran.com/")
    driver.maximize_window()

    time.sleep(2)

    elem_search_box = driver.find_element("xpath", "/html/body/section/div[2]/div[1]/div/form/div/input")
    #elem_search_box.click()

    elem_search_box.send_keys("dog")

    elem_search_box.send_keys(Keys.ENTER)

    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 500);")

    elem_search_res = driver.find_element("xpath", "/html/body/section/div[2]/div[2]/table/tbody/tr[2]/td[2]")
    assert (elem_search_res.text == "Bulldog")


    time.sleep(10)