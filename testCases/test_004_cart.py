from pageObjects.cart_page import Cart_Page
from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig

class Test_004_Cart:
    logger = LogGen.loggen()
    baseURL = ReadConfig.get_baseurl()

    def test_cart(self,setup):
        self.driver = setup

        self.logger.info("Testing cart method...")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.co = Cart_Page(self.driver)
        self.logger.info("Clicking on cart...")
        self.co.click_cart()
        self.logger.info("Clicking on here link...")
        self.co.click_here()

        self.driver.close()
