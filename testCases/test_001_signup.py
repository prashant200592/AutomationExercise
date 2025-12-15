import pytest
from pageObjects.home_page import HomePage
from pageObjects.signup_page import SignupPage
from utilities.random_string import random_string_generator
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen      # For logging
import os

import time

class Test_001_Signup:
    baseURL = ReadConfig.get_baseurl()
    logger = LogGen.loggen()                    # For logging
    def test_001_signup(self,setup):
        self.logger.info("test_001_signup is started...")

        self.driver = setup
        self.driver.implicitly_wait(10)

        self.driver.get(self.baseURL)
        self.logger.info("Launching application...")
        self.driver.maximize_window()

        self.hpo = HomePage(self.driver)
        self.logger.info("Clicking on Signup/Login link...")
        self.hpo.click_signuplogin()
        self.hpo.set_name("Prashant")
        self.mail = random_string_generator()+"@gmail.com"
        self.hpo.set_signupemail(self.mail)
        self.hpo.click_signup()

        self.logger.info("Adding user details for signup...")
        self.suo = SignupPage(self.driver)
        self.suo.click_mr()
        self.suo.set_password("12345678")
        self.suo.set_date_of_birth("20", "May","1992")
        #self.suo.click_newsletter()
        #self.suo.click_offers()
        self.suo.set_firstname("Prashant")
        self.suo.set_lastname("Pansare")
        self.suo.set_company("PSL")
        self.suo.set_address("Warje")
        self.suo.set_country("India")
        self.suo.set_state("Maharashtra")
        self.suo.set_city("Pune")
        self.suo.set_zipcode("411058")
        self.suo.set_mobilenumber("1234567890")
        self.suo.click_createaccount()
        self.success_message = self.suo.check_successmsg()
        if self.success_message == "ACCOUNT CREATED!":
            self.logger.info("Account is successfully created for the user...")
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_001_sign_up_passed.png")
            self.driver.close()
            assert True
        else:
            self.logger.error("Account registration failed for the user...")
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_001_sign_up_failed.png")
            self.driver.close()
            assert False

        self.logger.info("test_001_sign_up is finished...")