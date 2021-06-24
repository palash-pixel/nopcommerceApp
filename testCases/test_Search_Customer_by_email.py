
#### Run in desire browser
## to run -firefox -->> pytest -v -s testCases/Search_Customer_by_name.py --browser firefox
## to run -chrome -->> pytest -v -s testCases/Search_Customer_by_name.py --browser chrome
### to Run test parallel -->> pytest -v -s -n=2 testCases/Search_Customer_by_name.py --browser chrome
### to Run test parallel -->> pytest -v -s -n=2 testCases/Search_Customer_by_name.py --browser firefox
### to Run HTML Report -->> pytest -v -s --html=Reports\Search_Customerreport.html testCases/Search_Customer_by_name.py --browser firefox

import pytest
from selenium import webdriver
import time
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import Readconfig
from Utilities import XLUtils
from pageObjects.AddnewCustomer_page import AddCustomer
from pageObjects.SearchCustomer_page import SearchCustomer

class Test_003_Search_Customerby_Email:
    # URL = Readconfig.ApplicationURL()
    URL = Readconfig.ApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()

    @pytest.mark.sanity
    def test_Search_Customerby_Email(self, setup):
        # driver = self.driver
        self.driver = setup

        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.login = LoginPage(self.driver)

        self.login.setUsername(self.username)
        self.login.setPassword(self.password)
        title = self.driver.title

        print(title)
        self.login.clickLogin()
        time.sleep(5)

        title = self.driver.title
        print(title)

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        time.sleep(5)
        self.addcust.clickOnCustomersMenuItem()



        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        self.driver.close()
        assert True == status














































