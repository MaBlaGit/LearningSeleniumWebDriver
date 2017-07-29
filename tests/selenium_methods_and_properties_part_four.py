"""Learning Selenium WebDriver Methods and Properties."""

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class SeleniumMethodsAndPropertiesPartFour(unittest.TestCase):
    """Learn Selenium WebDriver Framework - mouse hover example."""

    @classmethod
    def setUpClass(cls):
        """Set up test environment."""
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.get('https://letskodeit.teachable.com/p/practice')

    def test_mouse_hover_example_one(self):
        """Test ActionChains class move mouse to the Top from the dropdown menu."""
        # locators
        mouse_hover_button = 'mousehover'
        mouse_hover_button_top = '//a[contains(text(), "Top")]'
        # steps
        locate_mouse_hover_button = WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element_by_id(mouse_hover_button)
        )
        locate_mouse_hover_button_top = WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element_by_xpath(mouse_hover_button_top)
        )
        self.driver.execute_script("window.scrollBy(0, 650);")
        actions = ActionChains(self.driver)
        actions.move_to_element(locate_mouse_hover_button)
        actions.move_to_element(locate_mouse_hover_button_top)
        actions.click()
        actions.perform()

    def test_mouse_hover_example_two(self):
        """Test ActionChains class move mouse to Reload from the dropdown menu."""
        # steps
        mouse_hover_button = 'mousehover'
        mouse_hover_button_reload = '//a[contains(text(), "Reload")]'
        # locators
        locate_mouse_hover_button = WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element_by_id(mouse_hover_button)
        )
        locate_mouse_hover_button_refresh = WebDriverWait(self.driver, 10).until(
            lambda driver: self.driver.find_element_by_xpath(mouse_hover_button_reload)
        )
        self.driver.execute_script("window.scrollBy(0, 650);")
        actions = ActionChains(self.driver)
        actions.move_to_element(locate_mouse_hover_button)
        actions.move_to_element(locate_mouse_hover_button_refresh)
        actions.click()
        actions.perform()

    @classmethod
    def tearDownClass(cls):
        """Close test environment."""
        cls.driver.quit()
