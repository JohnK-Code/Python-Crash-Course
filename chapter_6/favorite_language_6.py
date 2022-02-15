#### Favorite Language - Chapter 6 - Dictionary of Similar Objects 
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
language = favorite_languages['sarah'].title() # Access the 'favorite_language' dict and get the value assigned to the 'sarah' key, this is then saved to the 'language' variable
print(f"Sarah's favorite language is {language}.") # print string about favorite language and add the value saved in the 'language' variable


#### Looping through a Dictionary - Key-value pairs
print("\n") # new line
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name, language in favorite_languages.items(): # loop through the dictionary and assign the key and value to the varaibles 'name' and 'language' one at a time - This uses the 'items()' method to create a view object of the key's and value's
    print(f"{name.title()}'s favorite language is {language.title()}.")


#### Looping Through All the Keys in a Dictionary 
print("\n") # new line
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in favorite_languages.keys(): # loo through dict and save the key's to the variable 'name' one at a time - Uses the 'keys()' method to create a view object of the key's in the dict
    print(name.title())


#### Using a list of names to print an extra string if the value from the list is in the dict 'key'
print("\n") # new line
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.") # runs for every key in the dict
    if name in friends: # Below indented code only runs if the key stored in the variable 'name' matches a value in the 'friends' list 
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")


#### Use 'key()' method to check if it contains a specific key or not
print("\n") # new line
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
if 'erin' not in favorite_languages.keys(): # check if there is 'not' a key matching the string 'erin' in the dict
    print("Erin, please take our poll!") 


#### Looping Through a Dictionary's Keys in a paticular Order
print("\n") # new line
favorite_languages = { 
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in sorted(favorite_languages.keys()): # 'key()' method creates a list of dict keys and the 'sorted()' method sorts them alphabetically 
    print(f"{name.title()}, thank you for taking the poll.") # 'sorted' key values are inserted into the print statement in alphabetical order


#### Looping Through All Values in a Dictionary
print("\n") # new line
favorite_languages = { 
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())


#### Loop Through Dictionary Values and Remove all Duplicates 'set()' method
print("\n")
favorite_languages = { 
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()): # use 'set()' to remove duplicates from list created using the 'values' method on the 'favorite_languages' dict
    print(language.title()) # prints the values in the 'language' variable - duplicates were removed from the variable using 'set()' method


