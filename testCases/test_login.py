
#### Run in desire browser
## to run -firefox -->> pytest -v -s testCases/login.py --browser firefox
## to run -chrome -->> pytest -v -s testCases/login.py --browser chrome
### to Run test parallel -->> pytest -v -s -n=2 testCases/login.py --browser chrome
### to Run test parallel -->> pytest -v -s -n=2 testCases/login.py --browser firefox
### to run sanity test >>>pytest -v -s -m "sanity" --html=./Reports/sanity_report.html  testCases/login.py --browser chrome
### to run regression test >>>pytest -v -s -m "regression" --html=./Reports/sanity_report.html  testCases/login.py --browser chrome
### to run sanity and regression test >>>pytest -v -s -m "sanity and regression" --html=./Reports/sanity_report.html  testCases/login.py --browser chrome


import pytest
from selenium import webdriver

from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import Readconfig
class Test_001_login:
    URL = Readconfig.ApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()

 # URL = "https://admin-demo.nopcommerce.com/"
    # username = "admin@yourstore.com"
    # password = "admin"

    @pytest.mark.sanity
    # @pytest.mark.regression
    def test_homepage_01(self, setup):

        # driver = self.driver
        self.driver = setup

        self.driver.get(self.URL)
        title = self.driver.title
        print(title)
        self.driver.close()

        if title == "Your store. Login":
            print("Title Valid")
            assert True
        else:
            print("Title not Valid")
            self.driver.save_screenshot(".\\ScreenShots\\ " + "test_homepage_01_error.png")
            assert False

    @pytest.mark.sanity
    def test_login_02(self, setup):

        # driver = self.driver
        self.driver = setup

        self.driver.get(self.URL)

        self.login = LoginPage(self.driver)

        self.login.setUsername(self.username)
        self.login.setPassword(self.password)
        title = self.driver.title

        print(title)
        self.login.clickLogin()

        title = self.driver.title
        print(title)
        if title == "Dashboard / nopCommerce administration":
            print("Title Valid")
            assert True
        else:
            print("Title not Valid")
            self.driver.save_screenshot(".\\ScreenShots\\ " + "test_login_02_dashboard_error.png")
            assert False

        # self.login.clickLogout()
        self.driver.close()



