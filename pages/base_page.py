class BasePage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def navigate_to_page(self, url):
        self.driver.get(url)