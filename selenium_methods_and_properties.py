#! /usr/bin/python

"""Learnig Selenium Webdriver Methods and Properties."""

import unittest
import os
import csv
from logging_class import LoggingClass
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class LearningSelenium(unittest.TestCase):
    """Testing class."""
    
    @classmethod
    def setUpClass(cls):
        """Fixtures."""
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get('https://letskodeit.teachable.com/')
        cls.log = LoggingClass()

    def test_properties_webdriver_class_part_one(self):
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

        if not os.path.exists('./courses_titles/'):
            os.mkdir('./courses_titles/')

        with open('./courses_titles/courses.csv', 'w') as courses_data:
            writer = csv.writer(courses_data, delimiter=',')
            writer.writerow(['colected_data'])
            csv_data = list()
            for element in find_courses:
                print(element.text)
                LearningSelenium.log.logging_method("Found course '{0}'".format(element.text))
                csv_data.append(element.text)
                writer.writerow(csv_data)
                csv_data.remove(element.text)
        self.driver.close()
        # switching to main window handle
        self.driver.switch_to.window(new_window[0])
        
    def test_radio_buttons(self):
        # locators
        radio_button = 'bmwradio'
        # steps
        locate_radio_button = self.driver.find_element_by_id(radio_button)
        if locate_radio_button.is_selected() == False:
            LearningSelenium.log.logging_method("Radibutton '{0}' located".format(locate_radio_button.get_attribute("id")))
            locate_radio_button.click()
            LearningSelenium.log.logging_method("Radiobutton type: '{0}' id: '{1}' clicked".format(locate_radio_button.get_attribute("type"), locate_radio_button.get_attribute("id")))
    
    def test_select_dropdown_menu(self):
        # locators
        select_menu = 'carselect'
        # steps
        locate_dropdown_menu = self.driver.find_element_by_id(select_menu)
        self.assertTrue(locate_dropdown_menu)
        LearningSelenium.log.logging_method("Dropdown menu '{0}' located".format(locate_dropdown_menu.get_attribute("name")))
        select_menu = Select(locate_dropdown_menu)
        # select items from dropdown list by tvisible text
        for element in select_menu.options:
            print(element.text)
            select_menu.select_by_visible_text(element.text)
	# select items from dropdown list by index
        for element in range(len(select_menu.options)):
            select_menu.select_by_index(element)
            
    def test_select_multiple_dropdown_menu(self):
    	# locators
    	multiple_select_menu = 'multiple-select-example'
    	# steps
    	locate_multiple_select_menu = self.driver.find_element_by_id(multiple_select_menu)
    	self.assertTrue(locate_multiple_select_menu)
    	LearningSelenium.log.logging_method("Multiple dropdown menu '{0}' located".format(locate_multiple_select_menu.get_attribute("name")))
    	select_multi_menu = Select(locate_multiple_select_menu)
    	for element in range(len(select_multi_menu.options)):
    	    select_multi_menu.select_by_index(element)
                
    	for element in select_multi_menu.all_selected_options:
    	    LearningSelenium.log.logging_method("Element '{0}' located".format(element.text))
    	    
    	LearningSelenium.log.logging_method("First element from dropdown menu '{0}''".format(select_multi_menu.first_selected_option.text))
    	
    	select_multi_menu.deselect_all()
    	
    def test_properties_webdriver_class_part_two(self):
        # locators 
        alert_input_field = 'name'
        alert_button = 'alertbtn'
        # actions
        find_alert_input_field = self.driver.find_element_by_id(alert_input_field)
        find_alert_input_field.send_keys('TestTestTest')
        click_on_alert_button = self.driver.find_element_by_id(alert_button)
        click_on_alert_button.click()
        # switch to alert window
        switch_to_alert_window = self.driver.switch_to.alert
        print(switch_to_alert_window.text)
        # log message to the log file
        LearningSelenium.log.logging_method(switch_to_alert_window.text)
        switch_to_alert_window.accept()
            	
    @classmethod
    def tearDownClass(cls):
        """Fixture."""
        cls.driver.quit()

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
