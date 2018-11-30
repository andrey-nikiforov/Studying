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

@pytest.mark.parametrize("text", [
    ("TEST TEST"),
    ("GASJHAKGHKAGHKAGHAKGHKAIYGWWIUQAFBKU@&RT@*I$EG@$^*F$@K*^R$F@VJU$K@VGMJ")
])
def test_first_test(driver,text):

    with allure.step('Open link'):
        driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

    with allure.step('Send input text'):
        driver.find_element_by_css_selector('#user-message').send_keys(text)

    with allure.step('Click Show message and compare with displayed text'):
        driver.find_element_by_xpath("//button[contains(text(),'Show Message')]").click()
        assert text == driver.find_element_by_css_selector('#display').text