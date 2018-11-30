from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pytest
import allure



def test_bootstrap1(driver):

    with pytest.allure.step('open link'):
        driver.get('https://www.seleniumeasy.com/test/bootstrap-alert-messages-demo.html')

    with pytest.allure.step('Click button'):
        driver.find_element_by_xpath("//div[@class='col-md-4']/button").click()

    with pytest.allure.step('Check message'):
        driver.find_element_by_xpath("//div[@class='col-md-6']/div[@style='display: block;']")