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

###


def test_second_two(driver):
    wait = WebDriverWait(driver, 10)

    with pytest.allure.step('Open link'):
        driver.get('https://www.seleniumeasy.com/test/table-records-filter-demo.html')

    with pytest.allure.step('Find and click Green button'):
        driver.find_element_by_xpath("//button[contains(text(),'Green')]").click()

    with pytest.allure.step('Wait for table restructurization'):
        wait.until(EC.visibility_of_element_located((By.XPATH, "//table[@class='table table-filter']")))

    with pytest.allure.step('Check count of Green elements rows after filtering'):
        count = len(driver.find_elements_by_xpath("//tr[not(contains(@style,'display: none;'))]"))

    with pytest.allure.step('Print result and check count'):
        print('elements: ' + str(count) )
        assert count == 2

