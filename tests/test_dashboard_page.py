import pytest

from pages.dashboard_page import DashboardPage
from tests.base_test import BaseTest

class TestDashboardPage(BaseTest):

    @pytest.fixture
    def load_pages(self):
        self.page = DashboardPage(self.driver, self.wait)
        self.page.navigate_to_dashboard_page()

    def test(self, load_pages):
        self.page.click_flight_from_label()
        self.page.input_flight_from_textbox("HAN")
        self.page.click_flight_from_input_result_label()

        self.page.input_flight_to_textbox("Ho c")
        self.page.click_flight_to_input_result_label()

        self.page.click_from_date_label()
        self.page.pick_from_date()

        self.page.click_to_date_label()
        self.page.pick_to_date()

        self.page.click_on_flight_passenger_label()
        self.page.add_children_passenger()

        self.page.click_on_find_flight_btn()
