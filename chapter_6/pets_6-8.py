#### TRY IT YOURSELF - Chapter 6 - pets - dictionaries
pet1 = {
    'name': 'vinny',
    'owner': 'kirsty',
    'likes': 'chicken',
    'toy': 'squeaky',
    'type': 'dog'
}
pet2 = {
    'name': 'max',
    'owner': 'kim',
    'likes': 'chicken',
    'toy': 'carrot',
    'type': 'dog'
}
pet3 = {
    'name': 'bruno',
    'owner': 'joanne',
    'likes': 'biscuits',
    'toy': 'bone',
    'type': 'dog'
}
pets = [pet1, pet2, pet3]
for pet in pets:
    print(f"Info about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key.title()}: {value.title()}")