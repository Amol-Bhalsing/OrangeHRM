import time

import pytest

# import page object class
from PageObject.LoginPageObject import Login
from utilities import XLutils

from utilities.Logger import LogGen
from utilities.Readconfigfile import Readvalue     ## import class 'Readvalue' in the utilities.


class Test_Login_DDT:
    url=Readvalue.getUrl()
    log = LogGen.loggen()
    path="D:\\SoftwareTesting\\Automation Testing\\Framework_Projects\\OrangeHRM\\testData\\LoginData.xlsx"

    @pytest.mark.regression
    def test_login_ddt_004(self,setup,getDataForLogin):
        self.log.info("Opening Browser")
        self.driver = setup
        self.driver.get(self.url)
        self.log.info("Going to URL")
        self.lp = Login(self.driver)       # Create an instance of the page object class(i.e class Login)
        self.rows=XLutils.getRowCount(self.path,'Sheet1')
        print('Number of rows are-->',self.rows)
        login_status=[]
        #
        for r in range(2,self.rows+1):
            self.username=XLutils.readData(self.path,'Sheet1',r,1)
            self.password=XLutils.readData(self.path,'Sheet1',r,2)
            self.exp_status=XLutils.readData(self.path,'Sheet1',r,3)

            self.lp.enterUserName(self.username)     # Through this instance,use the page object methods in your tests
            self.log.info("Enter UserName--->"+ self.username)
            self.lp.enterPassword(self.password)  # Through this instance,use the page object methods in your tests
            self.log.info("Enter Password--->"+ self.password)
            self.lp.clickLogin()               # Through this instance,use the page object methods in your tests
            self.log.info("Click on login button")

            login_status=[]
            if self.lp.login_status()==True:
                if self.exp_status=='Pass':
                    login_status.append('Pass')
                    self.lp.click_Menu_Button()
                    self.log.info("Click on Menu button")
                    self.lp.click_Logout_Button()
                    self.log.info("Click on Logout button")
                    XLutils.writeData(self.path,'Sheet1',r,4,'Pass')

                elif self.exp_status=='Fail':
                    login_status.append('Fail')
                    self.driver.save_screenshot('D:\\SoftwareTesting\\Automation Testing\\Framework_Projects\\OrangeHRM\\Screenshot\\test_login_ddt_004_fail.png')
                    self.lp.click_Menu_Button()
                    self.log.info("Click on Menu button")
                    self.lp.click_Logout_Button()
                    self.log.info("Click on Logout button")
                    XLutils.writeData(self.path,'Sheet1',r,4,'Fail')

            else:
                if self.exp_status == 'Fail':
                    login_status.append('Pass')
                    self.driver.save_screenshot('D:\\SoftwareTesting\\Automation Testing\\Framework_Projects\\OrangeHRM\\Screenshot\\test_login_ddt_004_fail.png')
                    XLutils.writeData(self.path,'Sheet1',r,4,'Fail')

                elif self.exp_status == 'Pass':
                    login_status.append('Fail')
                    self.driver.save_screenshot('D:\\SoftwareTesting\\Automation Testing\\Framework_Projects\\OrangeHRM\\Screenshot\\test_login_ddt_004_fail.png')
                    XLutils.writeData(self.path,'Sheet1',r,4,'Fail')
            print(login_status)

        if 'Fail' not in login_status:
            self.log.info("test_login_ddt_004 is Passed")
            assert True
        else:
            self.log.info("test_login_ddt_004 is Failed")
            assert False
        self.driver.close()
        self.log.info("test_login_ddt_004 is Completed")














