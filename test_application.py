from unittest import TestCase
import configs.view_tools as view_tools
import view

class TestJokesterApplications(TestCase):
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

    





        

    






if __name__ == '__main__':
    import unittest
    unittest.main()
