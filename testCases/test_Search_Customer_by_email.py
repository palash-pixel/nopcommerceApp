
#### Run in desire browser
## to run -firefox -->> pytest -v -s testCases/test_Search_Customer_by_email.py --browser firefox
## to run -chrome -->> pytest -v -s testCases/test_Search_Customer_by_email.py --browser chrome
### to Run test parallel -->> pytest -v -s -n=2 testCases/Search_Customer_by_name.py --browser chrome
### to Run test parallel -->> pytest -v -s -n=2 testCases/test_Search_Customer_by_email.py.py --browser firefox
### to Run HTML Report -->> pytest -v -s --html=Reports\Search_Customerreport.html testCases/test_Search_Customer_by_email.py --browser firefox

import pytest
from selenium import webdriver
import time
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import Readconfig
from Utilities import XLUtils
from pageObjects.AddnewCustomer_page import AddCustomer
from pageObjects.SearchCustomer_page import SearchCustomer

class Test_003_Search_Customer_by_Email:
    # URL = Readconfig.ApplicationURL()
    URL = Readconfig.ApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()

    @pytest.mark.sanity
    def test_Search_Customer_by_Email(self, setup):

        self.driver = setup
        driver = self.driver

        driver.get(self.URL)
        driver.maximize_window()
        login = LoginPage(self.driver)

        login.setUsername(self.username)
        login.setPassword(self.password)
        title = driver.title

        print(title)
        login.clickLogin()
        time.sleep(5)

        title = self.driver.title
        print(title)

        add_customer = AddCustomer(driver)
        add_customer.clickOnCustomersMenu()
        time.sleep(5)
        add_customer.clickOnCustomersMenuItem()



        search_customer = SearchCustomer(driver)
        search_customer.setEmail("arthur_holmes@nopCommerce.com")
        search_customer.clickSearch()
        time.sleep(5)
        status = search_customer.searchCustomerByEmail("arthur_holmes@nopCommerce.com")
        self.driver.close()
        assert True == status














































