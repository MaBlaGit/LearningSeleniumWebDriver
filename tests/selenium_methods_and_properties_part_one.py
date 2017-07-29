"""Learning Selenium WebDriver Methods and Properties."""

import random
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SeleniumMethodsAndPropertiesPartOne(unittest.TestCase):
    """Learn Selenium WebDriver Framework.
    Radio button menu, drop down menu, multiple select menu,
    checkbox menu."""

    @classmethod
    def setUpClass(cls):
        """Set up test environment."""
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('https://letskodeit.teachable.com/p/practice')

    def test_radio_buttons(self):
        """Test radio buttons."""
        # locators
        radio_button = 'bmwradio'
        # steps
        locate_radio_button = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.ID, radio_button))
        )
        locate_radio_button.click()

    def test_drop_down_menu(self):
        """Test drop down menu."""
        # locators
        drop_down_menu = 'carselect'
        # steps
        locate_drop_down_menu = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.ID, drop_down_menu))
        )
        collect_all_options = Select(locate_drop_down_menu)
        # select random option from drop down menu
        upper_range_of_list = len(collect_all_options.options)
        collect_all_options.select_by_index(random.randrange(1, upper_range_of_list))

    def test_multiple_drop_down_menu(self):
        """Test multiple drop down menu."""
        # locators
        multiple_drop_down = 'multiple-select-example'
        # steps
        locate_multiple_drop_down = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.ID, multiple_drop_down))
        )
        # loop through menu elements and select all options and deselect
        collect_all_options = Select(locate_multiple_drop_down)
        for element in range(len(collect_all_options.options)):
            collect_all_options.select_by_index(element)
            collect_all_options.deselect_by_index(element)

    def test_checkbox_menu(self):
        """Test checkboxes on the website."""
        # locators
        checkbox = 'bmwcheck'
        # steps
        locate_checbox = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.ID, checkbox))
        )
        locate_checbox.click()

    @classmethod
    def tearDownClass(cls):
        """Close test environment."""
        cls.driver.quit()
