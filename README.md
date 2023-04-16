# SELENITUM-WITH-PYTHON
Data Driven Test / Pytest
import time

import pytest
from selenium import webdriver
from PageObject.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

#to use ini file nd get data form readProperties python file
#to use static method Readconfig class to import login data


class Test_002_DDT_Login:                    # without using class is in #form
    baseURL = ReadConfig.getApplicationURL()    #" https://admin-demo.nopcommerce.com/admin/
    path = ".//TestData/nopcommerce.xlsx" # data from excel file #path
    logger = LogGen.Loggen()



    def test_Login(self, setup):
        self.logger.info("*************Test_002_ddt***************")
        self.logger.info("*************verifying log in ddt tset***************")
        self.driver = setup
        self.driver.get(self.baseURL)

#to access login class we need to creat object here the we can use all functions

        self.lp = Login(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("number of rows", self.rows)

        List_status = [] #empty list variable

        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            #xpath from Login page and value from xlsx given from above code

            self.lp.setUserName(self.user) #xpath and use is username
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "pass":
                    self.logger.info('******* test passed********')
                    self.lp.clickLogout()
                    List_status.append("pass")
                if self.exp == "fail":
                    self.logger.info('******* test failed********')
                    self.lp.clickLogout()
                    List_status.append("fail")

            elif act_title != exp_title:
                if self.exp == "pass":
                    self.logger.info('******* test failed********')

                    List_status.append("fail")
                if self.exp == "pass":
                    self.logger.info('******* test passed********')

                    List_status.append("pass")

        if "fail" not in List_status:
            self.logger.info("login DDT test passed..")
            self.driver.close()
            assert True
        else:
            self.logger.info("login DDT test failed..")
            self.driver.close()
            assert False

        self.logger.info("**************login DDT test compeleted*********..")



