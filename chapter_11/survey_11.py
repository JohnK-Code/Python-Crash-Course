#### Testing a Class - Chapter 11 - Page 217 - A Class to Test
class AnonymousSurvey(): # Create class
    """Collect annonymous answers to a survey question.""" # docstring 

    def __init__(self, question): # define '__init__' function - This 'function/method' is run everytime an 'instance' is 'created' from the 'class'
        """Store a question, and prepare to store responses.""" # docstring
        self.question = question # create 'instance attribute' 'self.question' and assign the value of 'question' to it, the 'question' value is first provided when the 'object/instance' is created from the 'class'
        self.responses = [] # create 'instance attribute' 'self.responses' and assign the default value of an empty list - The list will be updated using the 'store_response' method/function' below  

    def show_question(self): # define 'method/function' 
        """Show the survey question.""" # docstring
        print(self.question) # print contents of 'self.question' - The contents is specific to the instance created using the class

    def store_response(self, new_response): # define 'method/function' 
        """Store a single response to the survey.""" # docstring
        self.responses.append(new_response) # 'append' the c'ontents' of the 'new_response' variable to the 'list' first created when the 'instance/object' was created from the class in the '__init__' methodd/function

    def show_results(self): # define 'method/function' 
        """Show all the responses that have been given.""" # docstring
        print("Survey results:") # print message
        for response in self.responses: # 'loop' through the 'list' first created when the 'instance/object' was created from the 'class' using the '__init__' method
            print(f"- {response}") # print each individual item from the list 'responses'