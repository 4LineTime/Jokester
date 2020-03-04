import unittest 
from unittest import TestCase
from unittest.mock import patch, call

import ui.ui as ui
import configs.db_tools as db_tools
import configs.view_tools as view_tools
import database.database as database
import view




class TestJokesterApplications(TestCase):

    test_db_url = 'test_jokester_db.sqlite'

    def setup(self):

        database.db = self.test_db_url
        database.connect_db()


    @patch('builtins.input', side_effect=['21','d', -2, 2])
    def test_input_id_selection_validation(self, mock_input):
        id = ui.input_selection()
        self.assertEqual(2, id)
        self.assertNotEqual(-2,id)
        self.assertRaises(ValueError)
    
    @patch('builtins.input', side_effect=['something'])
    def test_search_validation(self, mock_input):
        search = ui.search()
        self.assertEqual('something', search)
        self.assertNotEqual('-2,id', search)

    @patch('builtins.print')
    def test_save_joke_confirmation_validation(self, mock_print):
        ui.display_joke('Some Joke')
        mock_print.assert_called_once_with('\nSome Joke\n')
        
    def test_menu_selection(self):
        menu = view.menu_generator()
        self.assertEqual(view_tools.make_selection(menu, 1), menu[1])
        self.assertNotEqual(view_tools.make_selection(menu, 2), menu[1])
        self.assertNotEqual(view_tools.make_selection(menu, 3), menu[1])
        self.assertNotEqual(view_tools.make_selection(menu, 4), menu[1])

        self.assertNotEqual(view_tools.make_selection(menu, 1), menu[2])
        self.assertEqual(view_tools.make_selection(menu, 2), menu[2])
        self.assertNotEqual(view_tools.make_selection(menu, 3), menu[2])
        self.assertNotEqual(view_tools.make_selection(menu, 4), menu[2])

        self.assertNotEqual(view_tools.make_selection(menu, 1), menu[3])
        self.assertNotEqual(view_tools.make_selection(menu, 2), menu[3])
        self.assertEqual(view_tools.make_selection(menu, 3), menu[3])
        self.assertNotEqual(view_tools.make_selection(menu, 4), menu[3])

        self.assertNotEqual(view_tools.make_selection(menu, 1), menu[4])
        self.assertNotEqual(view_tools.make_selection(menu, 2), menu[4])
        self.assertNotEqual(view_tools.make_selection(menu, 3), menu[4])
        self.assertEqual(view_tools.make_selection(menu, 4), menu[4])

    def test_setup_search(self):
        self.assertIsNotNone(view_tools.setup_search('dad'))

    def test_check_joke(self):
        self.assertIsNone(view_tools.check_joke(''))
        self.assertIsNotNone(view_tools.check_joke('Something'))

    def test_generate_random_joke(self):
        self.assertIsNotNone(view_tools.generate_random_joke)

    
    def tearDown(self):
        database.db.close()

if __name__ == '__main__':
    import unittest
    unittest.main()
