"""Learning Selenium WebDriver Methods and Properties."""

import unittest
from ddt import ddt, data, unpack
from csv_file_reader.read_data_from_csv_file import extract_data_from_csv_file
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


@ddt
class SeleniumMethodsAndPropertiesPartFive(unittest.TestCase):
    """Learn Selenium WebDriver Framework - switching to iframe and searching courses
    read from csv file (ddt module used.)"""

    @classmethod
    def setUpClass(cls):
        """Set up test environment."""
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('https://letskodeit.teachable.com/p/practice')
        cls.driver.execute_script("window.scrollBy(0, 1300);")

    @data(*extract_data_from_csv_file("course_titles.csv"))
    @unpack
    def test_switch_to_frame_and_search_course(self, search_value):
        """Test - switching to iframe and searching course
        from csv file and print title to the console."""

        # locators
        iframe_element = 'courses-iframe'
        search_courses_input_field_iframe = 'search-courses'
        search_button_iframe = 'search-course-button'

        # steps
        locate_iframe_element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.ID, iframe_element))
        )
        self.driver.switch_to.frame(locate_iframe_element)
        locate_search_courses_input_field = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.ID, search_courses_input_field_iframe))
        )
        locate_search_courses_input_field.clear()
        locate_search_courses_input_field.send_keys(search_value)

        locate_search_button_iframe = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.ID, search_button_iframe))
        )
        locate_search_button_iframe.click()
        self.driver.back()

    @classmethod
    def tearDownClass(cls):
        """Close test environment."""
        cls.driver.quit()
