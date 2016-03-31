# -*- coding: utf-8 -*-

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    # called before each test:
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3) # opens browser and waits 3 seconds

    # runs after each test is complete (i.e. will run 7 times for 7 tests)
    def tearDown(self):
        self.browser.quit()

    # method starts with 'test' so it will be auto-tested
    def test_it_worked(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Welcome to Django', self.browser.title)

if __name__ == '__main__':
    # to avoid a 'ResourceWarning' message:
    unittest.main(warnings='ignore')

