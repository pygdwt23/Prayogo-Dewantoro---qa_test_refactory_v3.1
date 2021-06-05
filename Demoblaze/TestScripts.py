from unittest import TestSuite

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

from TestData import TestData
from Locators import Locators
from Pages import HomePage

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=TestData.CHROME_PATH)
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.close()
        self.driver.quit()

# HEADER LINK TEST
class HeaderLinksTest(BaseTest):
    def test_001_home_link(self):
        # Load Object
        self.header = HomePage(self.driver)

        # Execute
        self.header.check_home_link()

        # Assertion
        status = self.header.get_text(Locators.CATEGORIES)
        self.assertEqual(status, TestData.CATEGORIES_LABEL)

    def test_002_contact_link(self):
        # Load Object
        self.header = HomePage(self.driver)

        # Execute
        self.header.check_contact_link()

        # Assertion
        status = self.header.get_text(Locators.NEW_MESSAGE)
        self.assertEqual(status, TestData.CONTACT_LABEL)

    def test_003_aboutus_link(self):
        # Load Object
        self.header = HomePage(self.driver)

        # Execute
        self.header.check_aboutus_link()

        # Assertion
        status = self.header.get_text(Locators.ABOUT_US)
        self.assertEqual(status, TestData.ABOUTUS_LABEL)

    def test_004_cart_link(self):
        # Load Object
        self.header = HomePage(self.driver)

        # Execute
        self.header.check_cart_link()

        # Assertion
        status = self.header.get_text(Locators.PRODUCTS_IN_CART)
        self.assertEqual(status, TestData.CART_LABEL)

        time.sleep(3)

    def test_005_login_link(self):
        # Load Object
        self.header = HomePage(self.driver)

        # Execute
        self.header.check_login_link()

        # Assertion
        status = self.header.get_text(Locators.LOGIN_LINK)
        self.assertEqual(status, TestData.LOGIN_LABEL)

    def test_006_signup_link(self):
        # Load Object
        self.header = HomePage(self.driver)

        # Execute
        self.header.check_signup_link()

        # Assertion
        status = self.header.get_text(Locators.SIGNUP_LINK)
        self.assertEqual(status, TestData.SIGNUP_LABEL)


# SIDEBAR LINK TEST
class SidebarLinksTest(BaseTest):
    def test_001_phone_links(self):
        # Load Object
        self.sidebar = HomePage(self.driver)

        # Execute
        self.sidebar.check_phones_link()

        # Assertion
        status = self.sidebar.get_text(Locators.PHONE_SAMPLE)
        self.assertEqual(status, TestData.PHONE_1)
        time.sleep(3)

    def test_002_laptop_links(self):
        # Load Object
        self.sidebar = HomePage(self.driver)

        # Execute
        self.sidebar.check_laptops_link()

        # Assertion
        status = self.sidebar.get_text(Locators.LAPTOP_SAMPLE)
        self.assertEqual(status, TestData.LAPTOP_1)
        time.sleep(3)

    def test_003_monitor_links(self):
        # Load Object
        self.sidebar = HomePage(self.driver)

        # Execute
        self.sidebar.check_monitors_link()

        # Assertion
        status = self.sidebar.get_text(Locators.MONITOR_SAMPLE)
        self.assertEqual(status, TestData.MONITOR_1)
        time.sleep(3)

if __name__ == "__main__":
    # Create Test Suite
    suite = TestSuite()

    # Load test
    tests = unittest.TestLoader()

    # Add test to suite
    suite.addTests(tests.loadTestsFromTestCase(HeaderLinksTest))
    suite.addTests(tests.loadTestsFromTestCase(SidebarLinksTest))

    # Run the suite
    runner = unittest.TextTestRunner()
    runner.run(suite)