import pytest
from selenium import webdriver
import time
from pageObjects.Pnt_login_page import Pnt_LoginPage
from Utilities.readProperties import Readconfig
from Utilities import XLUtils


class Test_002_Pnt_DDT_login:
    URL_Pnt = Readconfig.ApplicationURL_Pnt()
    path = './/TestData/data.xlsx'

    # URL = "https://admin-demo.nopcommerce.com/"
    # ###username = "admin@yourstore.com"
    # password = "admin"

    @pytest.mark.skip


    def test_Pnt_login_DDT(self, setup):
        # driver = self.driver
        self.driver = setup

        # self.driver.get(self.URL_Pnt)

        self.login_Pnt = Pnt_LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print(self.rows)

        for r in range(2, self.rows + 1):
            # self.driver = setup
            self.driver.get(self.URL_Pnt)
            self.username = XLUtils.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
            self.writedata = XLUtils.writeData(self.path, 'Sheet1', r, 3, "test passed")

            print(self.username)
            print(self.password)

            self.login_Pnt.setUsername(self.username)
            self.login_Pnt.setPassword(self.password)
            time.sleep(5)

            self.login_Pnt.clickLogin()
            time.sleep(5)

            act_title = self.driver.title

            exp_title = "Forum of PeopleNTech - Index"
            print(act_title)

            if exp_title == act_title:
                print("Title Valid --Test Passed")
                assert True
                self.writedata
                # XLUtils.writeData(self.path, 'Sheet1', r, 3, "Test passed")
                self.login_Pnt.clickLogout()

            else:
                print("Title not Valid --Test Failed")
                self.driver.save_screenshot(".\\ScreenShots\\ " + "test_login_pnt_02_Forum_error.png")
                XLUtils.writeData(self.path, 'Sheet1', r, 3, "Test failed")

        self.driver.close()
