import unittest
from unittest.mock import patch
import sys
sys.path.append("c:\\Users\\Grace\\PYB\\src\\main\\python")
from batch import Person

class TestPerson(unittest.TestCase):
    def test_set_name(self):
        person = Person()
        self.assertEqual(person.set_name('DevOps'), 0)
        self.assertEqual(person.set_name('John'), 1)

    def test_get_name_existing(self):
        person = Person()
        person.set_name('DevOps')
        self.assertEqual(person.get_name(0), 'DevOps')

    def test_get_name_non_existing(self):
        person = Person()
        self.assertEqual(person.get_name(0), 'There is no such user')

    @patch('builtins.print')
    def test_main(self, mocked_print):
        person = Person()
        person.set_name('DevOps')
        person.set_name('John')
        person.get_name(0)
        person.get_name(1)

        self.assertTrue(mocked_print.called)
        expected_calls = [
            unittest.mock.call('User DevOps has been added with id ', 0),
            unittest.mock.call('User associated with id 0 is ', 'DevOps')
        ]
        mocked_print.assert_has_calls(expected_calls)

if __name__ == '__main__':
    unittest.main()
