

import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):

    if browser== 'chrome':
        driver = webdriver.Chrome()
        print("********Lunching Chrome browser********")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("******Lunching Firefox browser*******")
    else:
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser):       ## This will get the value fro CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):       ## This will return the browser value to setup method
    return request.config.getoption("--browser")

################# pytest HTML Report #####################
########### costomize input ##############
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'nop Commerce'
#     config._metadata['Module Name'] = 'Login'
#     config._metadata['Tester']      = 'Palash'
#
# ## It is hook for delete/modify environment in for HTML report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop('JAVA_HOME',None)
#     metadata.pop('Plugins', None)
