import time

import pytest
from selenium import webdriver
from Utilities.readProperties import Readconfig
from pageObjects.LoginPage import LoginPage
from pageObjects.AddnewCustomer_page import AddCustomer
from pageObjects.SearchCustomer_page import SearchCustomer


class Test_004_Search_Customer_by_name:

    URL = Readconfig.ApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()


    def test_Search_Customer_by_name(self, setup):
        self.driver = setup
        driver = self.driver
        driver.get(self.URL)
        driver.maximize_window()
        login = LoginPage(self.driver)
        login.setUsername(self.username)
        login.setPassword(self.password)
        login.clickLogin()

        #### add customer
        add_customer = AddCustomer(driver)
        add_customer.clickOnCustomersMenu()
        time.sleep(5)
        add_customer.clickOnCustomersMenuItem()

        ###### search customer by name
        search_customer = SearchCustomer(driver)
        search_customer.setFirstName("Arthur")
        search_customer.setLastName("Holmes")
        search_customer.clickSearch()
        self.driver.close()










