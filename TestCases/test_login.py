import pytest
from selenium import webdriver
from PageObject.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

#to use ini file nd get data form readProperties python file
#to use static method Readconfig class to import login data


class Test_001_Login:                    # without using class is in #form
    baseURL = ReadConfig.getApplicationURL()    #" https://admin-demo.nopcommerce.com/admin/"  from config.ini file
    username = ReadConfig.getUseremail()     # "admin@yourstore.com"
    password = ReadConfig.getPassword()  # "admin"

    logger = LogGen.Loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("*************Test_001_Login***************")
        self.logger.info("*************verifying homepage title***************")
        self.driver = setup    # setup came from conftest file to replace driver (webdriver.Chrome is replaced with setup )
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()

        if act_title == "Your store. Login":
            assert True
            self.logger.info("*************Test_001_Login is passed***************")
        else:
            assert False
            self.logger.info("*************Test_001_Login if failed***************")

    def test_Login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

#to access login class we need to creat object here the we can use all functions

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)  #email from config.ini file
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title = self.driver.title
        self.driver.close()

        if act_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False

