import sys
import os
 
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.insert(0, project_root)

import unittest
from application import app


class testSearches(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_search_in_field(self):
        search_string = "Tissue Y"
        node_type = "Sample"
        search_field = "tissue"
        response = self.app.get(f'/search_in_field/{node_type}/{search_field}/{search_string}')
        ##print(response.get_json())
        self.assertEqual(response.status_code, 200)

    def test_search_all_fields(self):
        search_string = "Tissue Y"
        node_type = "Sample"
        response = self.app.get(f'/search_all_fields/{node_type}/{search_string}')
        ##print(response.get_json())
        self.assertEqual(response.status_code, 200)

    def test_search_all_nodes(self):
        search_string = "Tissue Y"
        response = self.app.get(f'/search_all_nodes/{search_string}')
        ##print(response.get_json())
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()