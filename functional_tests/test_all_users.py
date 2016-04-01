# -*- coding: utf-8 -*-

from selenium import webdriver
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils.translation import activate # so we can get translation page addresses right
from datetime import date
from django.utils import formats


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
        activate('en') # test the English version

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

    # test that robots.txt and humans.txt can be found:
    def test_home_files(self):
        self.browser.get(self.live_server_url + "/robots.txt")
        self.assertNotIn("Not Found", self.browser.title)
        self.browser.get(self.live_server_url + "/humans.txt")
        self.assertNotIn("Not Found", self.browser.title)

    # test if the translation works:
    def test_internationalization(self):
        for lang, h1_text in [('en', 'Welcome to TaskBuster!'),
                              ('ca', 'Benvingut a TaskBuster!')]:
            activate(lang)
            self.browser.get(self.get_full_url("home"))
            h1 = self.browser.find_element_by_tag_name("h1")
            self.assertEqual(h1.text, h1_text)

    # test if the datetime format changes screw up the javascript
    def test_localization(self):
        today = date.today()
        for lang in ['en', 'ca']:
            activate(lang)
            self.browser.get(self.get_full_url("home"))
            local_date = self.browser.find_element_by_id("local-date")
            non_local_date = self.browser.find_element_by_id("non-local-date")
            self.assertEqual(formats.date_format(today, use_l10n=True),
                             local_date.text)
            self.assertEqual(today.strftime('%Y-%m-%d'), non_local_date.text)

    # test if we are displaying the right time/date
    def test_time_zone(self):
        self.browser.get(self.get_full_url("home"))
        tz = self.browser.find_element_by_id("time-tz").text
        utc = self.browser.find_element_by_id("time-utc").text
        ny = self.browser.find_element_by_id("time-ny").text
        self.assertNotEqual(tz, utc)
        self.assertNotIn(ny, [tz, utc])

