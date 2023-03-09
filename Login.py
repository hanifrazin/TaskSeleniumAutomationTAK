import unittest

import warnings
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from master.locator import LocatorPath
from master.data_test import DataTest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

class TestLogin(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        sv = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=sv)

    def test_success_login_checkout_cart(self):
        driver = self.browser
        driver.get(str(DataTest.base_url+"/login"))
        driver.find_element(By.XPATH, LocatorPath.username_login).send_keys(DataTest.email)
        driver.find_element(By.XPATH, LocatorPath.password_login).send_keys(DataTest.password)
        driver.find_element(By.XPATH, LocatorPath.login_button).click()

        message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, LocatorPath.welcome)))
        self.assertIn(DataTest.welcome, message.get_attribute("outerText"))
        self.assertEqual(driver.current_url, DataTest.base_url + '/')
        driver.get(driver.current_url)

        click_laptop = driver.find_element(By.XPATH, LocatorPath.laptop_14inch)
        self.assertIn(DataTest.laptop, click_laptop.get_attribute("innerText"))
        click_laptop.click()

        cart_qty = driver.find_element(By.XPATH, LocatorPath.qty)
        cart_qty.clear()
        cart_qty.send_keys(3)
        # print("Jumlah Barang : "+str(cart_qty.get_attribute("textContent")))

        add_to_cart = driver.find_element(By.CSS_SELECTOR, LocatorPath.add_laptop_to_cart)
        self.assertIn(DataTest.add_to_cart, add_to_cart.get_attribute("defaultValue"))
        add_to_cart.click()
        # WebDriverWait(driver,10).until(EC.presence_of_element_located((add_to_cart.click())))

        shopping_cart = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, LocatorPath.shopping_cart)))
        self.assertIn(DataTest.shopping, shopping_cart.get_attribute("innerText"))
        shopping_cart.click()
        self.assertEqual(driver.current_url, DataTest.base_url + '/cart')

        select = Select(driver.find_element(By.XPATH, "//select[@id='CountryId']"))
        select.select_by_visible_text('Indonesia')
        ship_button = driver.find_element(By.XPATH, LocatorPath.shipping_button)
        self.assertIn(DataTest.shipping, ship_button.get_attribute("defaultValue"))
        ship_button.click()

        accept = driver.find_element(By.XPATH, "//input[@id='termsofservice']")
        accept.click()

        checkout = driver.find_element(By.XPATH, "//button[@id='checkout']")
        self.assertIn("Checkout", checkout.get_attribute("innerText"))
        checkout.click()

        self.assertEqual(driver.current_url, DataTest.base_url + '/onepagecheckout')

        driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_FirstName']").send_keys(DataTest.firstname)
        driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_LastName']").send_keys(DataTest.lastname)
        driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_Email']").send_keys(DataTest.email)
        driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_Company']").send_keys("Moladin")
        select = Select(driver.find_element(By.XPATH, "//select[@id='BillingNewAddress_CountryId']"))
        select.select_by_visible_text('Indonesia')
        driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_City']").send_keys("Jakarta")
        driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_Address1']").send_keys("Cilandak")
        driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_Address2']").send_keys("Kedoya")
        driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_ZipPostalCode']").send_keys("13125")
        driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_PhoneNumber']").send_keys("811555698755")
        driver.find_element(By.XPATH, "//input[@id='BillingNewAddress_FaxNumber']").send_keys("0218989776655")
        

    def test_failed_login(self):
        driver = self.browser
        driver.get(str(DataTest.base_url+"/login"))
        driver.find_element(By.XPATH, LocatorPath.username_login).send_keys(DataTest.empty_field)
        driver.find_element(By.XPATH, LocatorPath.password_login).send_keys(DataTest.empty_field)
        driver.find_element(By.XPATH, LocatorPath.login_button).click()
        msg = driver.find_element(By.XPATH, LocatorPath.login_empty)
        self.assertIn(DataTest.error_login, msg.get_attribute("innerText"))

    def tearDown(self):
        self.browser.close()
