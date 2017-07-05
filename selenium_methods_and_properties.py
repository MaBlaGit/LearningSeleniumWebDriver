#! /usr/bin/python3

"""Learnig Selenium Webdriver Methods and properties."""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import unittest


class LearningSelenium(unittest.TestCase):
    """Testing class."""

    def setUp(self):
        """Fixtures."""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('https://letskodeit.teachable.com/')

    def test_properties_webdriver_class(self):
        """Properties of WebDriver class: current_url, current_window_handle,
           name, orientation, page_source, title.
           Methods of WebDriver class : back(), close(), forward(), get(url),
           maximize_window(), quit(), refresh(), swith_to.active_element(),
           Switch.to_alert(), swith_to.default_content(),
           swith_to.frame(frame_reference), swith_to.window(window_name),
           implicitly_wait(time_to_wait), set_page_load_timeout(time_to_wait),
           set_script_timeout(time_to_wait).
        """
        # locators
        practice_button = '//a[@class="fedora-navbar-link navbar-link"]'
        enroll_button = '//a[contains(text(), "Enroll now")]'
        window_button = 'openwindow'
        search_input = 'search-courses'
        page_title = '//h1[contains(text(), "Practice Page")]'
        courses_listing = '//div[@class="course-listing-title"]'

        # activities
        find_pr_button = self.driver.find_element_by_xpath(practice_button)
        find_pr_button.click()
        find_page_title = self.driver.find_element_by_xpath(page_title)
        # verify if page was loaded
        self.assertEqual('Practice Page', find_page_title.text)
        self.driver.back()
        find_enr_burron = self.driver.find_element_by_xpath(enroll_button)
        self.assertEqual('Enroll now', find_enr_burron.text)
        self.driver.forward()
        self.driver.refresh()
        find_open_wind_button = self.driver.find_element_by_id(window_button)
        find_open_wind_button.click()
        all_windows_handles = self.driver.window_handles
        # taking all windows into list
        new_window = all_windows_handles
        # selecting newest window
        select_window = new_window[1]
        # switching to newest window
        self.driver.switch_to.window(select_window)
        switched_to_new_window = self.driver.find_element_by_id(search_input)
        self.assertTrue(switched_to_new_window)
        find_courses = self.driver.find_elements_by_xpath(courses_listing)
        for element in find_courses:
            print(element.text)

    def tearDown(self):
        """Fixture."""
        self.driver.quit()

    # custom method to define if element is presented on the webpage
    def is_element_present(self, by, locator):
        """Check if locator exists."""
        try:
            self.driver.find_element(by, locator)
        except NoSuchElementException:
            print("Locator '{0}' was not found.".format(locator))
        print("Locator '{0}' was found.".format(locator))
        return -1


if __name__ == '__main__':
    unittest.main()
