"""Learning Selenium WebDriver Methods and Properties."""

import random
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class SeleniumMethodsAndPropertiesPartTwo(unittest.TestCase):
    """Learn Selenium WebDriver Framework.
    Radio button menu, drop down menu, multiple select menu,
    checkbox menu."""

    @classmethod
    def setUpClass(cls):
        """set up test environment."""
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get('https://letskodeit.teachable.com/p/practice')

    def test_switch_to_current_window(self):
        """Test switching to current window handle
        and printing out current courses content to the console."""
        # locators
        switch_to_window_button = 'openwindow'
        courses_in_new_window = '//div[@class="course-listing-title"]'
        # steps
        locate_switch_to_window_button = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.ID, switch_to_window_button))
        )
        locate_switch_to_window_button.click()
        # take all window handles into list
        all_window_handles = self.driver.window_handles
        # switch to newest window handle
        self.driver.switch_to.window(all_window_handles[1])
        locate_courses_in_new_window = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, courses_in_new_window))
        )
        # print courses titles into console
        for element in locate_courses_in_new_window:
            print("Course from new window: " + element.text)
        self.driver.close()
        self.driver.switch_to.window(all_window_handles[0])

    def test_switch_to_tab(self):
        """Test open new tab, switching to current window
        and printing out course content to the console."""
        # locators
        open_tab_button = 'opentab'
        new_tab_course_listing = '//div[@class="course-listing-title"]'
        new_tab_course_title = '//h1[@class="course-title"]'
        # actions
        locate_open_tab_button = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located((By.ID, open_tab_button))
        )
        locate_open_tab_button.click()
        new_window_handle = self.driver.window_handles
        self.driver.switch_to.window(new_window_handle[1])
        locate_new_tab_courses_listing = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located((By.XPATH, new_tab_course_listing))
        )
        # loop through each course and check if link of the selected course are clickable.
        for element in locate_new_tab_courses_listing:
            print("Course from new tab: " + element.text)
            element.click()
            locate_course_title = WebDriverWait(self.driver, 10).until(
                lambda driver: self.driver.find_element_by_xpath(new_tab_course_title)
            )
            # self.assertEqual(locate_course_title.text.strip(), element.text.strip())
            self.driver.execute_script("window.history.go(-1)")

    def test_alert_pop_up(self):
        """Test switching to alert window."""
        # locators
        alert_button = 'alertbtn'
        # steps
        locate_alert_button = WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element_by_id(alert_button)
        )
        locate_alert_button.click()
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.accept()

    @classmethod
    def tearDownClass(cls):
        """close test environment."""
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
