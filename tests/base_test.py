from pathlib import Path

import pytest
import yaml

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def config():
    path = Path(__file__).parent / "../data/config.yaml"
    try:
        with open(path) as config_file:
            data = yaml.load(config_file, Loader=yaml.FullLoader)
        return data
    finally:
        config_file.close()

class BaseTest:

    @pytest.fixture(autouse=True)
    def init_driver(self):
        if config()["browser"] == "chrome":
            self.driver = webdriver.Chrome()
        elif config()['browser'] == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            raise Exception("Incorrect Browser")

        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        yield self.wait, self.driver

        if self.driver is not None:
            self.driver.close()
            self.driver.quit()