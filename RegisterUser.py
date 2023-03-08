import unittest

import warnings
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from master.locator import LocatorPath
from master.data_test import DataTest
from selenium.webdriver.support.ui import WebDriverWait

class TestRegister(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        sv = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=sv)

    def test_success_register(self):
        driver = self.browser
        driver.get(str(DataTest.base_url+"/register"))
        driver.find_element(By.XPATH, LocatorPath.male_radio).click()
        driver.find_element(By.XPATH, LocatorPath.firstname).send_keys(DataTest.firstname)
        driver.find_element(By.XPATH, LocatorPath.lastname).send_keys(DataTest.lastname)
        driver.find_element(By.XPATH, LocatorPath.email).send_keys(DataTest.email)
        driver.find_element(By.XPATH, LocatorPath.password).send_keys(DataTest.password)
        driver.find_element(By.XPATH, LocatorPath.confirm_password).send_keys(DataTest.password)
        driver.find_element(By.XPATH, LocatorPath.register_button).click()
        message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, LocatorPath.message_after_regis)))
        # message = driver.find_element(By.XPATH, LocatorPath.message_after_regis)
        self.assertIn(DataTest.success_message, message.get_attribute("outerText"))
        self.assertEqual(driver.current_url, str(DataTest.base_url+"/registerresult/1"))
        driver.find_element(By.XPATH, LocatorPath.continue_button).click()
        driver.find_element(By.XPATH, LocatorPath.logout_link).click()
        print(DataTest.email)

    def test_register_is_empty(self):
        driver = self.browser
        driver.get(str(DataTest.base_url+"/register"))
        driver.find_element(By.XPATH, LocatorPath.firstname).send_keys(DataTest.empty_field)
        driver.find_element(By.XPATH, LocatorPath.lastname).send_keys(DataTest.empty_field)
        driver.find_element(By.XPATH, LocatorPath.email).send_keys(DataTest.empty_field)
        driver.find_element(By.XPATH, LocatorPath.password).send_keys(DataTest.empty_field)
        driver.find_element(By.XPATH, LocatorPath.confirm_password).send_keys(DataTest.empty_field)
        driver.find_element(By.XPATH, LocatorPath.register_button).click()
        error_firstname = driver.find_element(By.XPATH, LocatorPath.error_firstname)
        self.assertIn(DataTest.validasi_firstname, error_firstname.get_attribute("innerText"))
        error_lastname = driver.find_element(By.XPATH, LocatorPath.error_lastname)
        self.assertIn(DataTest.validasi_lastname, error_lastname.get_attribute("innerText"))
        error_email = driver.find_element(By.XPATH, LocatorPath.error_email)
        self.assertIn(DataTest.validasi_email, error_email.get_attribute("innerText"))
        error_password = driver.find_element(By.XPATH, LocatorPath.error_password)
        self.assertIn(DataTest.validasi_password, error_password.get_attribute("innerText"))
        error_conf_password = driver.find_element(By.XPATH, LocatorPath.error_password)
        self.assertIn(DataTest.validasi_password, error_conf_password.get_attribute("innerText"))
        # self.assertEqual(driver.current_url+'result/1', "https://demowebshop.tricentis.com/registerresult/1")

    def tearDown(self):
        self.browser.close()
