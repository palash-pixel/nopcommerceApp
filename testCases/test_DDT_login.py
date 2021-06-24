
#### Run in desire browser
## to run -chrome all the test -->> pytest -v -s --browser chrome
## to run -firefox -->> pytest -v -s testCases/DDT_login.py --browser firefox
## to run -chrome -->> pytest -v -s testCases/DDT_login.py --browser chrome
### to Run test parallel -->> pytest -v -s -n=2 testCases/DDT_login.py --browser chrome
### to Run test parallel -->> pytest -v -s -n=2 testCases/login.py --browser firefox
### to Run HTML Report -->> pytest -v -s --html=Reports\reports.html testCases/DDT_login.py --browser firefox

import pytest
from selenium import webdriver
import time
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import Readconfig
from Utilities import XLUtils


class Test_002_DDT_login:
    # URL = Readconfig.ApplicationURL()
    URL = Readconfig.ApplicationURL()
    path = './/TestData/test_Data.xlsx'

    # URL = "https://admin-demo.nopcommerce.com/"
    # ###username = "admin@yourstore.com"
    # password = "admin"

    @pytest.mark.regression
    def test_login_DDT(self, setup):
        # driver = self.driver
        self.driver = setup
        self.driver.get(self.URL)

        self.login = LoginPage(self.driver)
        self.driver.maximize_window()

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print(self.rows)

        for r in range(2, self.rows +1):
            self.user_name1 = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password1 = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)

            print(self.user_name1)
            print(self.password1)

            self.login.setUsername(self.user_name1)
            self.login.setPassword(self.password1)

            self.login.clickLogin()
            time.sleep(5)


            # self.driver.find_element_by_link_text("Logout").click()

            act_title = self.driver.title

            exp_title = "Dashboard / nopCommerce administration"

            print(act_title)
            # self.msg = self.driver.find_element_by_tag_name("body").text    ### To collect all the elements by tag name in the webpage with body text
            # print(self.msg)

            # self.login.clickLogout()

            if exp_title == act_title:
                print("Title Valid ")
                XLUtils.writeData(self.path, 'Sheet1', r, 3, "Title Valid--Test passed")
                self.login.clickLogout()
                assert True

            else:
                print("Title not Valid  ")
                self.driver.save_screenshot(".\\ScreenShots\\ " + "test_login_02_dashboard_error.png")
                XLUtils.writeData(self.path, 'Sheet1', r, 3, "Title not Valid --Test failed")

        self.driver.close()
