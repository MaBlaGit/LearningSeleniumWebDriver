#! /usr/bin/python3

"""Learning Selenium WebDriver Methods and Properties."""

import random
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SeleniumMethodsAndProperties(unittest.TestCase):
    """Learn Selenium WebDriver Framework."""

    def setUp(self):
        """Fixture."""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://letskodeit.teachable.com/p/practice')

    def test_radio_buttons(self):
        """Test radio buttons."""
        # locators
        radio_button = 'bmwradio'
        # steps
        locate_radio_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, radio_button)))
        locate_radio_button.click()

    def test_drop_down_menu(self):
        """Test drop down menu."""
        # locators
        drop_down_menu = 'carselect'
        # steps
        locate_drop_down_menu = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, drop_down_menu)))
        collect_all_options = Select(locate_drop_down_menu)
        # select random option from drop down menu
        upper_range_of_list = len(collect_all_options.options)
        collect_all_options.select_by_index(random.randrange(1, upper_range_of_list))

    def tearDown(self):
        """Fixture."""
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
