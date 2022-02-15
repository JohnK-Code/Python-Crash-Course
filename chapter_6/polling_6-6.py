#### TRY IT YOURSELF - Chapter 6 - Polling
### code from exercise 'favorite_language_6.py' 
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
language = favorite_languages['sarah'].title() # Access the 'favorite_language' dict and get the value assigned to the 'sarah' key, this is then saved to the 'language' variable
print(f"Sarah's favorite language is {language}.") # print string about favorite language and add the value saved in the 'language' variable


print("\n") # new line
students = ['john', 'sarah', 'kirsty', 'phil', 'terry']
for student in students:
    if student in favorite_languages.keys():
        print(f"Thank you for taking the poll, {student.title()}.\n")        
    else:
        print(f"{student.title()}, please take the poll.\n")