import unittest
from namemodule import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Test for 'namemodule.py'."""
    # all the method inside a Class which are actually unit tests runs 
    # automatically but make sure that the name of the method start with
    # 'test_'. Also try to run the program by renaming the methods and removing
    # 'test_', you'll notice how the method will not run automatically.

    def test_first_last_name(self):
        """Does names like janis joplin work?"""
        # first store the output of a function in a variable and then compare
        # that variable with expected output using assertEqual() method.

        formatted_name = get_formatted_name('janis', 'joplin')
        # output of a function

        self.assertEqual(formatted_name,'Janis Joplin')
        # self.assertEqual() takes two argument and checks whether both of them 
        # are equal and not.
        # self.assertEqual(output of a function,'expected output')
        #      first argument  -> output of a function
        #      second argument -> expected output
        #       formatted_name == 'Janis Joplin' ?
        # output of a function ==  expected output ?

    def test_first_last_middle_name(self):
        """Does names like 'Wolfgang Amadeus Mozart' works? """

        formatted_name = get_formatted_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')


    def test_more_than_required_args(self):
        "Does single name like sunyog works?"
        formatted_name = get_formatted_name('sunyog')
        self.assertEqual(formatted_name,'Sunyog')



# This thing runs the test.
if __name__ == '__main__':
    unittest.main()















