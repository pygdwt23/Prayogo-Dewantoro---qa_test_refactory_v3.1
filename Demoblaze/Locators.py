from selenium.webdriver.common.by import By

class Locators():

    # [Homepage]- Header Locator
    HOME_LINK = (By.XPATH, '//*[@id="navbarExample"]/ul/li[1]/a')
    CONTACT_LINK = (By.LINK_TEXT, "Contact")
    ABOUTUS_LINK = (By.LINK_TEXT, "About us")
    CART_LINK = (By.LINK_TEXT, "Cart")
    LOGIN_LINK = (By.LINK_TEXT, "Log in")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign up")

    # [Homepage] - Sidebar Locator
    PHONES_LINK = (By.LINK_TEXT, "Phones")
    LAPTOPS_LINK = (By.LINK_TEXT, "Laptops")
    MONITORS_LINK = (By.LINK_TEXT, "Monitors")

    PHONE_SAMPLE = (By.LINK_TEXT, "Samsung galaxy s6")
    LAPTOP_SAMPLE = (By.LINK_TEXT, "Sony vaio i5")
    MONITOR_SAMPLE = (By.LINK_TEXT, "Apple monitor 24")

    CATEGORIES = (By.ID, "cat")

    # Contact Locator
    NEW_MESSAGE = (By.ID, "exampleModalLabel")

    # About us Locator
    ABOUT_US = (By.ID, "videoModalLabel")

    # Cart page
    PRODUCTS_IN_CART = (By.XPATH, '//*[@id="page-wrapper"]/div/div[1]/h2')

    # Log in pop up
    LOGIN_POPUP = (By.ID, "logInModalLabel")

    # Sign up pop up
    SIGNUP_POPUP = (By.ID, "signInModalLabel")