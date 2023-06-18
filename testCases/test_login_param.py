import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# import page object class
from PageObject.LoginPageObject import Login

from utilities.Logger import LogGen
from utilities.Readconfigfile import Readvalue     ## import class 'Readvalue' in the utilities.


class Test_Login_Params:
    url=Readvalue.getUrl()
    log = LogGen.loggen()

    @pytest.mark.regression
    def test_login_params_003(self,setup,getDataForLogin):
        self.log.info("Opening Browser")
        self.driver = setup
        self.driver.get(self.url)
        self.log.info("Going to URL")
        self.lp = Login(self.driver)       # Create an instance of the page object class(i.e class Login)
        self.lp.enterUserName(getDataForLogin[0])     # Through this instance,use the page object methods in your tests
        self.log.info("Enter UserName--->"+ getDataForLogin[0])
        self.lp.enterPassword(getDataForLogin[1])  # Through this instance,use the page object methods in your tests
        self.log.info("Enter Password--->"+ getDataForLogin[1])
        self.lp.clickLogin()               # Through this instance,use the page object methods in your tests
        self.log.info("Click on login button")

        login_status=[]

        if self.lp.login_status()==True and getDataForLogin[2]=='Pass':
            login_status.append('Pass')
            self.lp.click_Menu_Button()
            self.log.info("Click on Menu button")
            self.lp.click_Logout_Button()
            self.log.info("Click on Logout button")

        elif self.lp.login_status() == True and getDataForLogin[2] == 'Fail':
            login_status.append('Fail')
            self.driver.save_screenshot(r'D:\SoftwareTesting\Automation Testing\Framework_Projects\OrangeHRM\Screenshot\test_login_params_003_fail.png')
            self.lp.click_Menu_Button()
            self.log.info("Click on Menu button")
            self.lp.click_Logout_Button()
            self.log.info("Click on Logout button")

        elif self.lp.login_status() == False and getDataForLogin[2] == 'Fail':
            login_status.append('Pass')

        else:
            login_status.append('Fail')
            self.driver.save_screenshot(r'D:\SoftwareTesting\Automation Testing\Framework_Projects\OrangeHRM\Screenshot\test_login_params_003_fail.png')
        print(login_status)

        if 'Fail' not in login_status:
            self.log.info("test_login_params_003 is Passed")
            assert True
        else:
            self.log.info("test_login_params_003 is Failed")
            assert False
        self.driver.close()
        self.log.info("test_login_params_003 is Completed")










