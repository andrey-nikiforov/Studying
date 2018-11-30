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

text ='TEXT123^%&^%'
def test_first_test(driver):

    with allure.step('Open link'):
        driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

        driver.find_element_by_css_selector('#user-message').send_keys(text)
        driver.find_element_by_xpath("//button[contains(text(),'Show Message')]").click()
        assert text == driver.find_element_by_css_selector('#display').text