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
                
        def test_display_ID(self):
                self.browser.get('http://localhost:8000/ingredients_detail')
                self.assertIn('Ingredients - Detail', self.browser.title)
                self.assertIn('http://localhost:8000/ingredients_detail', self.browser.current_url)        

        def test_display_IL(self):
                self.browser.get('http://localhost:8000/ingredients_list')
                self.assertIn('Ingredients - List', self.browser.title)
                self.assertIn('http://localhost:8000/ingredients_list', self.browser.current_url)
                self.fail('Finish the test!')

        def test_display_IUF(self):
                self.browser.get('http://localhost:8000/ingredients_update_form')
                self.assertIn('Ingredients - Update Form', self.browser.title)
                self.assertIn('http://localhost:8000/ingredients_update_form', self.browser.current_url)
                
if __name__ == '__main__':
        unittest.main(warnings = 'ignore')

