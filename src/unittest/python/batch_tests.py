import unittest
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

if __name__ == '__main__':
    unittest.main()
