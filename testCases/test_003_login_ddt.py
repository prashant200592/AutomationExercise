from pageObjects.home_page import HomePage
from utilities import XLUtils
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig

import time
import os

class Test_003_login_ddt:
    cur_file_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(cur_file_dir)
    file = os.path.join(root_dir, 'testData', 'Automation_Exercise_LoginData.xlsx')
    sheetName = 'Sheet1'
    rows = XLUtils.getRowCount(file, sheetName)
    baseURL = ReadConfig.get_baseurl()
    logger = LogGen.loggen()

    def test_login_ddt(self,setup):
        self.driver = setup
        self.logger.info("Launching application...")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.hpo = HomePage(self.driver)
        exp_list = []
        for r in range(2, self.rows+1):
            self.logger.info("Checking combination of valid and invalid credentials...")
            self.hpo.click_signuplogin()

            mail = XLUtils.readData(self.file,self.sheetName,r,1)
            pwd = XLUtils.readData(self.file,self.sheetName,r,2)
            exp = XLUtils.readData(self.file,self.sheetName,r,3)

            self.hpo.set_loginemail(mail)
            self.hpo.set_loginpassword(pwd)
            self.hpo.click_login()
            time.sleep(3)
            self.status = self.hpo.check_loginsuccess()

            if self.status == True:
                if exp == 'Valid':
                    exp_list.append("Pass")
                    self.hpo.click_logout()
                else:
                    exp_list.append("Fail")

            elif self.status == True:
                if exp == 'Invalid':
                    exp_list.append("Fail")
                    self.hpo.click_logout()
                else:
                    exp_list.append("Pass")

        self.driver.close()
        if "Fail" not in exp_list:
            assert True
            self.logger.info("login ddt test passed...")

        else:
            self.logger.error("login ddt test failed...")
            assert False


        self.logger.info("Completed login ddt test...")