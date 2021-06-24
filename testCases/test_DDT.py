# import pytest
import time
import openpyxl
from selenium import webdriver
from Utilities import XLUtils



path = "C:/Users/palas/PycharmProjects/nopcommerceApp/TestData/data.xlsx"

workbook = openpyxl.load_workbook(path)
sheet = workbook.active
rows = XLUtils.getRowCount(path, 'Sheet1')

cols = XLUtils.getColCount(path, 'Sheet1')
print(rows)
print(cols)

for r in range(2, rows + 1):
    # print(sheet.cell(r, c).value, end="   ")
    driver = webdriver.Chrome()
    driver.get("https://forum.piit.us/")
    username = XLUtils.readData(path, 'Sheet1', r, 1)
    password = XLUtils.readData(path, 'Sheet1', r, 2)
    print(username)
    print(password)

    driver.find_element_by_xpath("//*[@id='frmLogin']/div/div[3]/dl/dd[1]/input").send_keys(username)
    driver.find_element_by_xpath("//*[@id='frmLogin']/div/div[3]/dl/dd[2]/input").send_keys(password)
    driver.find_element_by_xpath("//*[@id='frmLogin']/div/div[3]/p/input").click()
    time.sleep(5)

    # driver.close()

    if driver.title == "Forum of PeopleNTech - Index":
        print("test passed")
        XLUtils.writeData(path, 'Sheet1', r, 3, "test passed")
        driver.find_element_by_xpath("// span[contains(text(), 'Logout')]").click()

    else:
        print("test failed")
        XLUtils.writeData(path, 'Sheet1', r, 3, "test failed")
        driver.close()

    # driver.close()



# user_name = XLUtils.readData(path, "Sheet1", r, 1)
# pass_word = XLUtils.readData(path, "Sheet1", r, 2)

#
# driver.find_element_by_xpath("//*[@id='frmLogin']/div/div[3]/dl/dd[1]/input").send_keys(user_name)
#
#
# driver.find_element_by_xpath("//*[@id='frmLogin']/div/div[3]/dl/dd[2]/input").send_keys(pass_word)
# driver.find_element_by_xpath("//*[@id='frmLogin']/div/div[3]/p/input").click()
# time.sleep(5)
# driver.find_element_by_xpath("// span[contains(text(), 'Logout')]").click()
# driver.close()
