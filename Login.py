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

class TestLogin(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        sv = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=sv)

    def test_success_login(self):
        driver = self.browser
        driver.get(str(DataTest.base_url+"/login"))
        driver.find_element(By.XPATH, LocatorPath.username_login).send_keys('tonny.chopper996@mail.com')
        print(DataTest.email)
        driver.find_element(By.XPATH, LocatorPath.password_login).send_keys(DataTest.password)
        driver.find_element(By.XPATH, LocatorPath.login_button).click()
        message = driver.find_element(By.XPATH, LocatorPath.welcome)
        self.assertIn(DataTest.welcome, message.get_attribute("innerText"))
        # self.assertEqual(driver.current_url, "https://demowebshop.tricentis.com/registerresult/1")


    def test_failed_login(self):
        driver = self.browser
        driver.get(str(DataTest.base_url+"/login"))
        driver.find_element(By.XPATH, LocatorPath.username_login).send_keys(DataTest.empty_field)
        print(DataTest.email)
        driver.find_element(By.XPATH, LocatorPath.password_login).send_keys(DataTest.empty_field)
        driver.find_element(By.XPATH, LocatorPath.login_button).click()
        msg = driver.find_element(By.XPATH, LocatorPath.login_empty)
        self.assertIn(DataTest.error_login, msg.get_attribute("innerText"))

    def tearDown(self):
        self.browser.close()
