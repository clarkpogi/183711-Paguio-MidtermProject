import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
        def setUp(self):
                self.browser = webdriver.Firefox()
                
        def tearDown(self):
                self.browser.quit()

        def test_open_froyo(self):
                self.browser.get('http://localhost:8000')
                self.assertIn('The Good Place FroYo Shop', self.browser.title)

        def test_display_ICF(self):
                self.browser.get('http://localhost:8000/ingredients_create_form')
                self.assertIn('Ingredients - Create Form', self.browser.title)
                self.assertIn('http://localhost:8000/ingredients_create_form', self.browser.current_url)
                self.fail('Finish the test!')

if __name__ == '__main__':
        unittest.main(warnings = 'ignore')
