import unittest
import mock


import menus
import entry
import worklog


class EntryTests(unittest.TestCase):
    def setUp(self):
        self.test_entry = entry.Entry()

    def test_entry_get_project(self):
        # fake the input, and test to see if the entry.project is correct
        with mock.patch("builtins.input", return_value="Test Project"):
            assert self.test_entry.get_project() == "Test Project"

    def test_entry_get_employee(self):
        # fake the input, and test to see if the entry.project is correct
        pass

    def test_entry_get_notes(self):
        # fake the input, and test to see if the entry.project is correct
        pass

    def test_entry_get_display_date(self):
        # fake the input, and test to see if the entry.project is correct
        pass


class MenuTests(unittest.TestCase):

    def test_print_header(self):
        test_input = "========" + "\n= TEST =\n" + "========"
        self.assertEquals(menus.print_header("test", 8), test_input)

    def test_print_bottom_line(self):
        self.assertEquals(menus.print_bottom_line(5), "-----")

    def test_validate_input(self):
        assert menus.validate_input("a", ["A", "B", "C"])

    def test_validate_input_fails(self):
        assert not menus.validate_input("x", ["A", "B", "C"])

    def test_bad_input_error(self):
        test_msg = "[Press Enter] Your input was not valid. Please try again."
        self.assertEquals(menus.bad_input_error(), test_msg)

    def test_invalid_choice_error(self):
        test_msg = "[Press Enter] Please choose a valid option: A, B, or C."
        self.assertEqual(menus.invalid_choice_error(["A", "B", "C"]), test_msg)

if __name__ == "__main__":
    unittest.main()
