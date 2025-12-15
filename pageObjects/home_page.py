from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,ElementNotInteractableException

class HomePage:
    # Locators
    link_signuplogin_xpath = "//a[@href='/login']"

    textbox_signupname_name = "name"
    textbox_signupemail_xpath = "//input[@data-qa='signup-email']"
    button_signup_xpath = "//button[@data-qa='signup-button']"

    textbox_loginemail_xpath = "//input[@data-qa='login-email']"
    textbox_loginpassword_xpath = "//input[@data-qa='login-password']"
    button_login_xpath = "//button[@data-qa='login-button']"

    link_logout_xpath = "//a[@href='/logout']"

    # init method
    def __init__(self,setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.mywait = WebDriverWait(self.driver, 10,
                                    ignored_exceptions=[NoSuchElementException, ElementNotInteractableException])

    # action methods
    def click_signuplogin(self):
        self.driver.find_element(By.XPATH, self.link_signuplogin_xpath).click()

    def set_name(self, username):
        name = self.driver.find_element(By.NAME, self.textbox_signupname_name)
        name.send_keys(username)

    def set_signupemail(self, email):
        mail = self.driver.find_element(By.XPATH, self.textbox_signupemail_xpath)
        mail.send_keys(email)

    def click_signup(self):
        self.driver.find_element(By.XPATH, self.button_signup_xpath).click()

    def set_loginemail(self, email):
        mail = self.driver.find_element(By.XPATH, self.textbox_loginemail_xpath)
        mail.send_keys(email)

    def set_loginpassword(self, password):
        pwd = self.driver.find_element(By.XPATH, self.textbox_loginpassword_xpath)
        pwd.send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def check_loginsuccess(self):
        try:
            login_check = self.mywait.until(EC.presence_of_element_located((By.XPATH, self.link_logout_xpath)))
            login_status = login_check.is_displayed()
            return login_status
        except:
            return False

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()