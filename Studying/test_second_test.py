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

a=1
b=223

def test_second_two(driver):
    driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
    driver.find_element_by_css_selector('#sum1').send_keys(a)
    driver.find_element_by_css_selector('#sum2').send_keys(b)
    driver.find_element_by_xpath("//button[contains(text(),'Get Total')]").click()
    assert a + b == int(driver.find_element_by_css_selector('#displayvalue').text)