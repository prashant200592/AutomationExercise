from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time



class SignupPage:
    # Locators
    radio_mr_xpath = "//input[@id='id_gender1']"
    textbox_password_xpath = "//input[@id='password']"
    dropdown_day_xpath = "//select[@id='days']"
    dropdown_month_xpath = "//select[@id='months']"
    dropdown_year_xpath = "//select[@id='years']"
    checkbox_newsletter_xpath = "//input[@name='newsletter']"
    checkbox_offers_xpath = "//input[@name='optin']"
    textbox_firstname_xpath = "//input[@data-qa='first_name']"
    textbox_lastname_xpath = "//input[@data-qa='last_name']"
    textbox_company_xpath = "//input[@data-qa='company']"
    textbox_address_xpath = "//input[@data-qa='address']"
    dropdown_country_xpath = "//select[@data-qa='country']"
    textbox_state_xpath = "//input[@data-qa='state']"
    textbox_city_xpath = "//input[@data-qa='city']"
    textbox_zipcode_xpath = "//input[@data-qa='zipcode']"
    textbox_phones_xpath = "//input[@data-qa='mobile_number']"
    button_createaccount_xpath = "//button[@data-qa='create-account']"
    message_success_xpath = "//h2[normalize-space()='Account Created!']"

    # init method
    def __init__(self,setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.mywait = WebDriverWait(self.driver, 10,
                               ignored_exceptions=[NoSuchElementException, ElementClickInterceptedException])

    # action method
    def click_mr(self):
        self.driver.find_element(By.XPATH, self.radio_mr_xpath).click()

    def set_password(self,password):
        pwd = self.driver.find_element(By.XPATH, self.textbox_password_xpath)
        pwd.send_keys(password)

    def set_date_of_birth(self,day,month,year):
        days = Select(self.driver.find_element(By.XPATH, self.dropdown_day_xpath))
        days.select_by_visible_text(day)

        months = Select(self.driver.find_element(By.XPATH, self.dropdown_month_xpath))
        months.select_by_visible_text(month)

        years = Select(self.driver.find_element(By.XPATH, self.dropdown_year_xpath))
        years.select_by_visible_text(year)

    def click_newsletter(self):
        #self.driver.find_element(By.XPATH, self.checkbox_newsletter_xpath).click()
        newsletter = self.mywait.until(EC.presence_of_element_located((By.XPATH, self.checkbox_newsletter_xpath)))
        newsletter.click()

    def click_offers(self):
        self.driver.find_element(By.XPATH, self.checkbox_offers_xpath).click()

    def set_firstname(self,firstname):
        fname = self.driver.find_element(By.XPATH, self.textbox_firstname_xpath)
        fname.send_keys(firstname)

    def set_lastname(self,lastname):
        lname = self.driver.find_element(By.XPATH, self.textbox_lastname_xpath)
        lname.send_keys(lastname)

    def set_company(self,company):
        comp = self.driver.find_element(By.XPATH, self.textbox_company_xpath)
        comp.send_keys(company)

    def set_address(self,address):
        addr = self.driver.find_element(By.XPATH, self.textbox_address_xpath)
        addr.send_keys(address)

    def set_country(self,country):
        nation = Select(self.driver.find_element(By.XPATH, self.dropdown_country_xpath))
        nation.select_by_visible_text(country)

    def set_state(self,state):
        state_name = self.driver.find_element(By.XPATH, self.textbox_state_xpath)
        state_name.send_keys(state)

    def set_city(self,city):
        city_name = self.driver.find_element(By.XPATH, self.textbox_city_xpath)
        city_name.send_keys(city)

    def set_zipcode(self,zipcode):
        zip_code = self.driver.find_element(By.XPATH, self.textbox_zipcode_xpath)
        zip_code.send_keys(zipcode)

    def set_mobilenumber(self,mobile_number):
        phone = self.driver.find_element(By.XPATH, self.textbox_phones_xpath)
        phone.send_keys(mobile_number)

    def click_createaccount(self):
        self.driver.find_element(By.XPATH, self.button_createaccount_xpath).click()

    time.sleep(3)
    def check_successmsg(self):
        successmessage = self.driver.find_element(By.XPATH, self.message_success_xpath).text
        print(successmessage)
        return successmessage
