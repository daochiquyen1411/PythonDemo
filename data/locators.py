from selenium.webdriver.common.by import By

class DashboardPageLocators:
    FLIGHT_FROM_LABEL = (By.XPATH, "//*[contains(@class, 'mktnd_frm_flight_departure')]")
    FLIGHT_FROM_INPUT_TEXTBOX = (By.XPATH, "//*[contains(@class, 'flight_from_autocomplete autocomplete-flight-input')]")
    FLIGHT_FROM_INPUT_RESULT_LABEL = (By.XPATH, "//strong[contains(text(),'HAN')]")
    FLIGHT_TO_INPUT_TEXTBOX = (By.XPATH, "//*[contains(@class, 'flight_to_autocomplete autocomplete-flight-input')]")
    FLIGHT_TO_INPUT_RESULT_LABEL = (By.XPATH, "//strong[contains(text(),'SGN')]")

    FROM_DATE_LABEL = (By.XPATH, "//*[contains(@class, 'departure_date_flight')]")
    PICK_FROM_DATE_LABEL = (By.XPATH, "//*[contains(@data-month, '5')]//*[contains(text(),'29')]")

    TO_DATE_LABEL = (By.XPATH, "//*[contains(@class, 'returning_date_flight')]")
    PICK_TO_DATE_LABEL = (By.XPATH, "//*[contains(@data-month, '5')]//*[contains(text(),'30')]")

    FLIGHT_PASSENGER_LABEL = (By.XPATH, "//*[contains(@class, 'flight_passenger')]")
    ADD_CHILDREN_PASSENGER_PLUS_ICON = (By.XPATH, "//*[contains(@class, 'pop-flight-passenger')]//*[contains(@class, 'btn_children_adult_plus')]")

    FIND_FLIGHT_BTN = (By.XPATH, "//*[contains(@class, 'mktnd_btn_flight_search_flight')]")