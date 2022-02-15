#### TRY IT YOURSELF - Chapter 6 - People
# This is from exercise persons_6-1.py
person = {'first_name': 'kirsty', 'last_name': 'murray', 'age': '30', 'city': 'glenrothes'} # new dictionary 
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# New code 
person1 = {'first_name': 'john', 'last_name': 'kelly', 'age': '32', 'city': 'glenrothes'}
person2 = {'first_name': 'eric', 'last_name': 'matthes', 'age': '40', 'city': 'new york'}

people = [person, person1, person2]
for person in people:
    print(f"Your name is {person['first_name'].title()} {person['last_name'].title()}, you are {person['age']} and from {person['city'].title()}.")