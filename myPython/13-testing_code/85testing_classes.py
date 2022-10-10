'''
from surveyclassmodule import AnonymousSurvey



question = 'what is your favorite food? '
q1 = AnonymousSurvey(question)

q1.show_question()


print("Press 'q' to stop the program.")

while True:
    response = input("Favorite food: ")
    if response == 'q':
        break
    else:
        q1.store_responses(response)


q1.show_responses()
#----------------------------------------------------------------------------------------------------

import unittest
from surveyclassmodule import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Test for the class AnonymousSurvey."""


    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"

        # To run a test on class, we need to create an instance first. So that 
        # we can run a test on it.
        q1 = AnonymousSurvey(question)
        q1.store_responses('English')
        self.assertIn('English',q1.responses)
        # Is English stored in a list named responses? 


    def test_store_multiple_response(self):
        """Test that multiple responses are stored properly."""
        question = 'What are your favorite fruits?'
        q2 = AnonymousSurvey(question)
        responses = ['manog','banana','apple']

        # storing all the responses in a list.
        for response in responses:
            q2.store_responses(response)

        # checking whether all the responses are stored in the list responses.
        for response in responses:
            self.assertIn(response,q2.responses)


if __name__ == '__main__':
    unittest.main()
'''
#------------------------------------------------------------------------------------------------------
# Using setUp() method


import unittest
from surveyclassmodule import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Test for the class AnonymousSurvey."""


    def setUp(self):
        """Create a survey and  a set of responses for use in all test methods."""
        
        question = 'What language did you first learn to speak?'

        # Creating an instance that every unit test will use
        self.q1 = AnonymousSurvey(question)

        # creating a response that every unit test will use
        self.responses = ['English','German','Spanish','Hindi']
    

    def test_store_single_response(self):
        """Test that a single response is stored properly."""

        # using a method of the class.
        self.q1.store_responses(self.responses[0])

        # checkig the output of the method.
        self.assertIn('English',self.q1.responses)


    def test_store_single_response(self):
        """Test that a multiple response are stored properly."""
        for response in self.responses:
            self.q1.store_responses(response)

        for response in self.responses:
            self.assertIn(response,self.q1.responses)


if __name__ == '__main__':
    unittest.main()







