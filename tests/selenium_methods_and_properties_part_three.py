"""Learning Selenium WebDriver Methods and Properties."""

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class SeleniumMethodsAndPropertiesPartThree(unittest.TestCase):
    """Learn Selenium WebDriver Framework.
    Web table example, send keys to the input field and
    check if element is displayed."""

    @classmethod
    def setUpClass(cls):
        """Set up test environment."""
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('https://letskodeit.teachable.com/p/practice')

    def test_web_table(self):
        """Loop through the table and print values of the table to the console."""
        # locators
        table = '//table[@class="table-display"]//tbody//tr'
        # steps
        locate_table = WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_elements_by_xpath(table)
        )
        for element in locate_table:
            print(element.text)

    @classmethod
    def tearDownClass(cls):
        """Close test environment."""
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
