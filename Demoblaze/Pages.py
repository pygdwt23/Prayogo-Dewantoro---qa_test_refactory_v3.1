from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from TestData import TestData
from Locators import Locators

class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    # Fungsi Klik Locator
    def click(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    # Fungsi Hapus Data
    def clear_text(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).clear()

    # Fungsi input data
    def enter_text(self, locator, teks):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).send_keys(teks)

    # Fungsi ambil teks
    def get_text(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        ).text

    # Fungsi cek elemen visible
    def is_visible(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return bool(element)
        except TimeoutException:
            return False

    # Fungsi select dropdown
    def select_dropdown_by_value(self, locator, item):
        dropdown = Select(self.driver.find_element_by_id(locator))
        dropdown.select_by_value(item)

    def select_dropdown_by_visible_text(self, locator, item):
        dropdown = Select(self.driver.find_element_by_id(locator))
        dropdown.select_by_visible_text(item)

    # Fungsi Hover
    def move_element_to(self,locator):
        hover = self.driver.find_element_by_xpath(locator)
        self.action.move_to_element(hover).perform()

    # Fungsi Click JS Alert
    def alert_click(self, locator):
        self.driver.find_element_by_xpath(locator).click()
        self.driver.switch_to.alert.accept()


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    #     HEADER LINK
    def check_home_link(self):
        self.click(Locators.HOME_LINK)
        self.is_visible(Locators.CATEGORIES)

    def check_contact_link(self):
        self.click(Locators.CONTACT_LINK)
        self.is_visible(Locators.NEW_MESSAGE)

    def check_aboutus_link(self):
        self.click(Locators.ABOUTUS_LINK)
        self.is_visible(Locators.ABOUT_US)

    def check_cart_link(self):
        self.click(Locators.CART_LINK)
        self.is_visible(Locators.PRODUCTS_IN_CART)

    def check_login_link(self):
        self.click(Locators.LOGIN_LINK)
        self.is_visible(Locators.LOGIN_POPUP)

    def check_signup_link(self):
        self.click(Locators.SIGNUP_LINK)
        self.is_visible(Locators.LOGIN_POPUP)

    #     SIDEBAR LINK
    def check_phones_link(self):
        self.click(Locators.PHONES_LINK)
        self.is_visible(Locators.PHONE_SAMPLE)

    def check_laptops_link(self):
        self.click(Locators.LAPTOPS_LINK)
        self.is_visible(Locators.LAPTOP_SAMPLE)

    def check_monitors_link(self):
        self.click(Locators.MONITORS_LINK)
        self.is_visible(Locators.MONITOR_SAMPLE)