from selenium.webdriver.support import expected_conditions as EC

from data.locators import DashboardPageLocators
from pages.base_page import BasePage

class DashboardPage(BasePage):

    def __init__(self, driver, wait):
        self.url = "https://www.bestprice.vn/"
        self.locators = DashboardPageLocators
        super().__init__(driver, wait)

    def navigate_to_dashboard_page(self):
        self.navigate_to_page(self.url)

    def click_flight_from_label(self):
        self.wait.until(EC.visibility_of_element_located(self.locators.FLIGHT_FROM_LABEL)).click()

    def input_flight_from_textbox(self, input):
        self.wait.until(EC.visibility_of_element_located(self.locators.FLIGHT_FROM_INPUT_TEXTBOX)).send_keys(input)

    def click_flight_from_input_result_label(self):
        self.wait.until(EC.visibility_of_element_located(self.locators.FLIGHT_FROM_INPUT_RESULT_LABEL)).click()

    def input_flight_to_textbox(self, input):
        self.wait.until(EC.visibility_of_element_located(self.locators.FLIGHT_TO_INPUT_TEXTBOX)).send_keys(input)

    def click_flight_to_input_result_label(self):
        self.wait.until(EC.visibility_of_element_located(self.locators.FLIGHT_TO_INPUT_RESULT_LABEL)).click()

    def click_from_date_label(self):
        self.wait.until(EC.visibility_of_element_located(self.locators.FROM_DATE_LABEL)).click()

    def pick_from_date(self):
        self.wait.until(EC.visibility_of_element_located(self.locators.PICK_FROM_DATE_LABEL)).click()

    def click_to_date_label(self):
        self.wait.until(EC.visibility_of_element_located(self.locators.TO_DATE_LABEL)).click()

    def pick_to_date(self):
        self.wait.until(EC.visibility_of_element_located(self.locators.PICK_TO_DATE_LABEL)).click()

    def click_on_flight_passenger_label(self):
        self.wait.until(EC.visibility_of_element_located(self.locators.FLIGHT_PASSENGER_LABEL)).click()

    def add_children_passenger(self):
        self.wait.until(EC.visibility_of_element_located(self.locators.ADD_CHILDREN_PASSENGER_PLUS_ICON)).click()

    def click_on_find_flight_btn(self):
        self.wait.until(EC.visibility_of_element_located(self.locators.FIND_FLIGHT_BTN)).click()