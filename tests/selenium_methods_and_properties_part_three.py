"""Learning Selenium WebDriver Methods and Properties."""

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


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

    def test_is_element_displayed(self):
        """Test if element is displayed.
        Test send keys into input field."""
        # locators
        input_field = 'displayed-text'
        hide_button = 'hide-textbox'
        show_button = 'show-textbox'
        # steps
        locate_input_field = WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element_by_id(input_field)
        )
        # scrolling to located element
        self.driver.execute_script("window.scrollBy(0, 400);")
        locate_show_button = WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element_by_id(show_button)
        )
        locate_hide_button = WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element_by_id(hide_button)
        )
        locate_hide_button.click()
        if not locate_input_field.is_displayed():
            locate_show_button.click()
        locate_input_field.clear()
        locate_input_field.send_keys("This is for learning purpose")

    @classmethod
    def tearDownClass(cls):
        """Close test environment."""
        cls.driver.quit()
