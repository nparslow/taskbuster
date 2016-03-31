# -*- coding: utf-8 -*-

from selenium import webdriver
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


'''
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
'''

class HomeNewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def get_full_url(self, namespace):
        # live_server_url gives the local host url, will be different for test server
        # reverse gives relative url of a particular namespace
        return self.live_server_url + reverse(namespace)

    def test_home_title(self):
        self.browser.get(self.get_full_url("home"))
        self.assertIn("TaskBuster", self.browser.title)

    def test_h1_css(self):
        self.browser.get(self.get_full_url("home"))
        h1 = self.browser.find_element_by_tag_name("h1")
        self.assertEqual(h1.value_of_css_property("color"),
                         "rgba(200, 50, 255, 1)")
