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



@pytest.mark.parametrize("a,b,sum", [
    (3,5,8),
    (100500,-100500,0),
    (0,0,0),
])
def test_second_two(driver,a,b,sum):

    with allure.step('Open link'):
        driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

    with allure.step('Send values'):
        driver.find_element_by_css_selector('#sum1').send_keys(a)
        driver.find_element_by_css_selector('#sum2').send_keys(b)

    with allure.step('click Get total and check sum'):
        driver.find_element_by_xpath("//button[contains(text(),'Get Total')]").click()
        assert sum == int(driver.find_element_by_css_selector('#displayvalue').text)
