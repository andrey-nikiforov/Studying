from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pytest
import allure
import time



def test_bootstrap1(driver):
    wait = WebDriverWait(driver, 10)

    with pytest.allure.step('Open link'):
        driver.get('https://www.seleniumeasy.com/test/dynamic-data-loading-demo.html')

    with pytest.allure.step('Click button'):
        driver.find_element_by_xpath("//button[@id='save']").click()

    with pytest.allure.step('Wait until elements loaded'):
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='loading']/img[contains(@src,'randomuser')]")))
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'First Name :')]")))
