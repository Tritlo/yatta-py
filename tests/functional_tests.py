from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_page_opens(self):
        self.browser.get('http://localhost:5000')
        self.assertIn('Yatta',self.browser.title)



if __name__ == "__main__":
    unittest.main(warnings='ignore')