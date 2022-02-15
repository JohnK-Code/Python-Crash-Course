#### Testing a Class - Chapter 11 - Page 217 - A Class to Test
from survey_11 import AnonymousSurvey # import the class 'AnonymousSurvey from the file 'survey_11.py'

# Define a question, make a survey.
question = "What language did you first learn to speak?" # assign string to variabale
my_survey = AnonymousSurvey(question) # 'create' an 'instance/object' from the 'AnonymousSurvey' class - provide required 'argument' for 'instance attribute' in the '__init__'method 

# Show the question, and store the responses to the question.
my_survey.show_question() # call method realted to the 'my_survey' instance created using the AnonymousSurvey class
print("Enter 'q' at any time to quit.\n") # print string
while True: # run indented code while True
    response = input("Language: ") # assign user input to variable
    if response == 'q': # if 'response == q' run indented code
        break # break out of while loop
    my_survey.store_response(response) # call method 'store_responses' for instance/object 'my_survey' - the response variable created previously is provided as the argument for the method being called

# Show the survey results.
print("\nThank you to everyone who participated in the survey!") # print string
my_survey.show_results() # call 'show_results' method related to 'my_survey' instance of the 'AnonymousSurvey' class