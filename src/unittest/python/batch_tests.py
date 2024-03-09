import unittest
import sys

# Add the path to the module containing the Person class
sys.path.append("c:\\Users\\Grace\\PYB\\src\\main\\python\\src")

# Import the Person class
from batch import Person as PersonClass

class TestPerson(unittest.TestCase):
    """
    A class that inherits unittest.TestCase to perform unit tests on the Person class.
    """
    def setUp(self):
        """
        Method called to prepare the test fixture. 
        """
        self.person = PersonClass()  # Instantiate the Person Class
        self.user_id = []  # List to store obtained user_ids
        self.user_name = []  # List to store person names

    # Test case function to check the Person.set_name method
    def test_set_name(self):
        """
        Test case to verify the Person.set_name method.
        """
        for i in range(4):
            # Initialize a name
            name = 'name' + str(i)
            # Store the name in the list variable
            self.user_name.append(name)
            # Get the user_id obtained from the set_name method
            user_id = self.person.set_name(name)
            # Check if the obtained user_id is not None
            self.assertIsNotNone(user_id)
            # Store the user_id in the list
            self.user_id.append(user_id)

        # Print the results for debugging
        print("user_id length =", len(self.user_id))
        print(self.user_id)
        print("user_name length =", len(self.user_name))
        print(self.user_name)

    # Test case function to check the Person.get_name method
    def test_get_name(self):
        """
        Test case to verify the Person.get_name method.
        """
        length = len(self.user_id)  # Total number of stored user information
        print("user_id length =", length)
        print("user_name length =", len(self.user_name))
        
        for i in range(6):
            # If i does not exceed total length, then verify the returned name
            if i < length:
                # If the two names do not match, the test case will fail
                self.assertEqual(self.user_name[i], self.person.get_name(self.user_id[i]))
            else:
                print("Testing for get_name no user test")
                # If length exceeds, then check for 'There is no such user' message
                self.assertEqual('There is no such user', self.person.get_name(i))

if __name__ == '__main__':
    unittest.main()
