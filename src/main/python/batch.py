"""
This module provides a class for managing person objects.
"""

class Person:
    """
    A class representing a person with a name.
    """

    name = []

    def set_name(self, user_name):
        """
        Sets the name of the person and returns the assigned id.

        Args:
            user_name (str): The name of the person.

        Returns:
            int: The id assigned to the person.
        """
        self.name.append(user_name)
        return len(self.name) - 1

    def get_name(self, user_id):
        """
        Retrieves the name of the person associated with the given id.

        Args:
            user_id (int): The id of the person.

        Returns:
            str: The name of the person, or 'There is no such user' if the id is invalid.
        """
        if user_id >= len(self.name):
            return 'There is no such user'
        return self.name[user_id]


if __name__ == '__main__':
    person = Person()
    print('User DevOps has been added with id ', person.set_name('DevOps'))
    print('User associated with id 0 is ', person.get_name(0))


