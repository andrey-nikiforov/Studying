# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pytest
import allure


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.close()


def test_google(driver):
    wait = WebDriverWait(driver, 10)

    with pytest.allure.step('Open google'):
        driver.get('https://www.google.com')

    with pytest.allure.step('Send query'):
        search_field = driver.find_element_by_css_selector('input[name="q"]')
        search_field.send_keys('pytest')
        search_field.submit()

    with pytest.allure.step('Check result'):
        page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'td.cur')))
        assert page.text == '1'

