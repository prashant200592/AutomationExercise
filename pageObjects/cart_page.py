from selenium.webdriver.common.by import By

class Cart_Page:

    # Locators
    link_cart_xpath = "//a[@href='/view_cart']"
    link_here_xpath = "//u[normalize-space()='here']"



    # init method
    def __init__(self,setup):
        self.driver = setup

    # action methods
    def click_cart(self):
        self.driver.find_element(By.XPATH, self.link_cart_xpath).click()

    def click_here(self):
        self.driver.find_element(By.XPATH, self.link_here_xpath).click()