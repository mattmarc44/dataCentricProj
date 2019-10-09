import unittest
from app import *

class FlaskTestCase(unittest.TestCase):
    #check flask is setup correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # check posts show up on the home page
    def test_posts_show_up_on_main_page(self):
        tester = app.test_client(self)
        response = tester.get(
            '/get_movies',
            follow_redirects=True
        )
        self.assertIn(b'Hot Fuzz', response.data)
        #b prefix makes it a byte literal and prevents TypeError
        #NOTE: I don't see this as the best way to test content being returned but its the best I could do

    #check forms send

if __name__ == '__main__':
    unittest.main()