import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# import page object class
from PageObject.LoginPageObject import Login

from utilities.Logger import LogGen
from utilities.Readconfigfile import Readvalue     ## import class 'Readvalue' in the utilities.

class Test_Url_Login:
    username=Readvalue.getUsername()     # store the values returned by utility methods into Test class variables.
    password=Readvalue.getPassword()     # store the values returned by utility methods into Test class variables.
    url=Readvalue.getUrl()
    log = LogGen.loggen()

    # @pytest.mark.Sanity
    def test_url(self,setup):
        # self.log.debug("debug")
        # self.log.info("info")
        # self.log.warning("warning")
        # self.log.error("error")
        # self.log.critical("critical")

        self.log.info("Opening Browser")
        self.driver=setup
        self.driver.get(self.url)
        self.log.info("Going to URL")
        time.sleep(2)
        self.log.info("Checking Page title")

        if self.driver.title=='OrangeHRM':
            self.log.info("test_url is Passed")
            assert True
        else:
            self.log.info("test_url is Failed")
            self.driver.save_screenshot('D:\\SoftwareTesting\\Automation Testing\\Framework_Projects\\OrangeHRM\\Screenshot\\test_url_fail.png')
            assert False
        self.driver.close()
        self.log.info("test_url is Completed")

    # @pytest.mark.Sanity
    def test_login_002(self,setup):
        self.log.info("Opening Browser")
        self.driver = setup
        self.driver.get(self.url)
        self.log.info("Going to URL")
        self.lp = Login(self.driver)       # Create an instance of the page object class(i.e class Login)
        self.lp.enterUserName(self.username)     # Through this instance,use the page object methods in your tests
        self.log.info("Enter UserName--->"+ self.username)
        self.lp.enterPassword(self.password)  # Through this instance,use the page object methods in your tests
        self.log.info("Enter Password--->"+ self.password)
        self.lp.clickLogin()               # Through this instance,use the page object methods in your tests
        self.log.info("Click on login button")

        if self.lp.login_status()==True:
            self.log.info("test_login_002 is Passed")

            self.lp.click_Menu_Button()
            self.log.info("Click on Menu button")

            self.lp.click_Logout_Button()
            self.log.info("Click on Logout button")

            assert True
        else:
            self.log.info("test_login_002 is Failed")

            self.driver.save_screenshot('D:\\SoftwareTesting\\Automation Testing\\Framework_Projects\\OrangeHRM\\Screenshot\\test_login_002_fail.png')
            assert False

        self.driver.close()
        self.log.info("test_login_002 is Completed")










