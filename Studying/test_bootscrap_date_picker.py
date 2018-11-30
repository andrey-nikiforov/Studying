from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pytest
import allure


@pytest.mark.parametrize("day", [
    (12),
    (20)
])2
def test_bootstrap1(driver,day):

    with pytest.allure.step('Open link'):
        driver.get('https://www.seleniumeasy.com/test/bootstrap-date-picker-demo.html')

    with pytest.allure.step('Find datepicker and choose date'):
        driver.find_element_by_xpath("//input[@placeholder='dd/mm/yyyy']").click()
        driver.find_element_by_xpath("//td[contains(text(),'{0}')]".format(day)).click()

    with pytest.allure.step('Assign found elements sequense to a variable'):
        z = driver.find_element_by_xpath("//input[@class='form-control']").get_attribute('value')

    with pytest.allure.step('Check day of picked date'):
        print(z)
        assert z[:2] == str(day)
