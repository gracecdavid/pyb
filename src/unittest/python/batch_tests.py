import unittest

class Testing(unittest.TestCase):
    def test_string_equal(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_string_not_equal(self):
        a = 'some'
        b = 'different'
        self.assertNotEqual(a, b)

    def test_boolean_true(self):
        a = True
        self.assertTrue(a)

    def test_boolean_false(self):
        a = False
        self.assertFalse(a)

if __name__ == '__main__':
    unittest.main()
