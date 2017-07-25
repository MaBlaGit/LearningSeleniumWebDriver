"""Test Suite of the tests based on https://letskodeit.teachable.com/p/practice website."""

import unittest
import HtmlTestRunner
from LearningSeleniumWebDriver.tests.selenium_methods_and_properties_part_one import \
    SeleniumMethodsAndPropertiesPartOne
from LearningSeleniumWebDriver.tests.selenium_methods_and_properties_part_two import \
    SeleniumMethodsAndPropertiesPartTwo
from LearningSeleniumWebDriver.tests.selenium_methods_and_properties_part_three import \
    SeleniumMethodsAndPropertiesPartThree


class TestSuite(object):
    """Test suite class."""

    def __init__(self):
        self.selenium_methods_and_properties_one = unittest.TestLoader().loadTestsFromTestCase(
            SeleniumMethodsAndPropertiesPartOne
        )
        self.selenium_methods_and_properties_two = unittest.TestLoader().loadTestsFromTestCase(
            SeleniumMethodsAndPropertiesPartTwo
        )
        self.selenium_methods_and_properties_three = unittest.TestLoader().loadTestsFromTestCase(
            SeleniumMethodsAndPropertiesPartThree
        )

    def run_test_methods_and_properties_suite(self):
        """Collect tests into test suites."""
        return unittest.TestSuite([self.selenium_methods_and_properties_one,
                                   self.selenium_methods_and_properties_two,
                                   self.selenium_methods_and_properties_three,])

if __name__ == '__main__':
    test_suite = TestSuite()
    runner = HtmlTestRunner.HTMLTestRunner(output='test-suite-report.html')
    runner.run(test_suite.run_test_methods_and_properties_suite())
