import pytest
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from pageObjects import home_page
import time
import os

class Test_002_Login:
    baseURL = ReadConfig.get_baseurl()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_login(self,setup):
        self.driver = setup

        self.logger.info("Launching application...")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hpo = home_page.HomePage(self.driver)
        self.hpo.click_signuplogin()
        self.logger.info("Adding credentials...")
        self.hpo.set_loginemail(self.email)
        self.hpo.set_loginpassword(self.password)
        self.hpo.click_login()
        time.sleep(3)

        self.logger.info("Checking login status...")
        self.login_status = self.hpo.check_loginsuccess()
        if self.login_status == True:
            self.logger.info("Login Successful...")
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_002_login_passed.png")
            self.driver.close()
            assert True

        else:
            self.logger.error("Login Failed...")
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_002_login_failed.png")
            self.driver.close()
            assert False

