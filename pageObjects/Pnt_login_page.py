class Pnt_LoginPage:
    #
    # textbox_username_id = "Email"
    # textbox_password_id = "Password"
    # button_login_xpath = "//button[contains(text(),'Log in')]"
    # link_logout_linktext = "Logout"
    # pnt login page
    user_textbox_xpath = "//*[@id='frmLogin']/div/div[3]/dl/dd[1]/input"

    password_textbox_xpath = "//*[@id='frmLogin']/div/div[3]/dl/dd[2]/input"

    login_button_xpath = "//*[@id='frmLogin']/div/div[3]/p/input"

    logOut_button_xpath = "//span[contains(text(),'Logout')]"

    def __init__(self, driver):  ### constructor will call the driver
        self.driver = driver


    def setUsername(self, username):
        self.driver.find_element_by_xpath(self.user_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.user_textbox_xpath).send_keys(username)


    def setPassword(self, password):

        self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.logOut_button_xpath).click()
