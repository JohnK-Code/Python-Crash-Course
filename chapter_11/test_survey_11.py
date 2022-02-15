#### Testing a Class - Chapter 11 - Page 218 - Testing the AnonymousSurvey Class
import unittest # import unittest
from survey_11 import AnonymousSurvey # from 'survey_11.py' file import the 'AnonymousSurvey' class

class TestAnonymousSurvey(unittest.TestCase): # define test class that inherits form the 'unittest.TestCase' class
    """Tests for the class AnonymousSurvey""" # docstring

    def setUp(self): # define setUp method - the objects created here can be used in all the tests to reduce repetitive code
        """Create a survey and a set of responses for use in all test methods.""" # docstring
        question = "What language did you first learn to speak?" # assign string to variable
        self.my_survey = AnonymousSurvey(question) # create instance/object from class and pass in any required arguments
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self): # define test function
        """Test that a single response is stored properly.""" # docstring
        self.my_survey.store_response(self.responses[0]) # call method related to instance/object created in 'setUp' - Provide required argument for method also
        self.assertIn(self.responses[0], self.my_survey.responses) # check if first value in 'responses' list created in setup is in 'self.my_survey.resposes' list created in 'setUp' - this checks the class used to create the instance is returning the correct responce 

    def test_store_three_responses(self): # define test function/method
        """Test that three individual responses are stored correctly.""" # docstring
        for response in self.responses: # loop through list and assign each value to the 'reponse' variable
            self.my_survey.store_response(response) # 'call' instance/object 'method' 'store_response' and 'provide' the 'response' variable on each 'iteration' of the 'loop' as the required 'argument' for the method 
        
        for response in self.responses: # loop through list and assign each value to the 'reponse' variable
            self.assertIn(response, self.my_survey.responses) # check if 'response' variable is in the 'list' 'responses' associated with the 'instance/object' 'my_survey' - checks the class and instance/object are working as expected 

if __name__ == '__main__': # check if '__name__' is equal to '__main__' - These will be equal if this file/module is the one being run in the interpreter - it has not been imported and run from another file/moduel
    unittest.main() # loads and runs the tests from module