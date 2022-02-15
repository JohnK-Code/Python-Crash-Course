#### TRY IT YOURSELF - Chapter 6 - Favorite Numbers 
# Code from previous exercise favorite_numbers_6-2.py
favorite_numbers = {
    'kirsty': 8,
    'john': 7,
    'eva': 73,
    'georgie': 22,
    'sophie': 1,
}
print(f"Kirsty's favorite number is {favorite_numbers['kirsty']}.")
print(f"John's favorite number is {favorite_numbers['john']}.")
print(f"Eva's favorite number is {favorite_numbers['eva']}.")
print(f"Georgie's favorite number is {favorite_numbers['georgie']}.")
print(f"Sophie's favorite number is {favorite_numbers['sophie']}.")


#### New Code 
print("\n") # new line
favorite_numbers = {
    'kirsty': ['8', '73', '30'],
    'john': ['7', '14', '32'],
    'eva': ['73', '25', '40'],
    'georgie': ['22', '10', '46'],
    'sophie': ['1'],
}
for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are: ")
    for number in numbers:
        print(f"\t{number}")