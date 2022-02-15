#### List in a dictionary - Chapter 6 - favorite_languages.py
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items(): # looping through a dictionaries keys and values
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages: # looping through the 'list values' from the dictionary 'value'
        print(f"\t{language.title()}")

