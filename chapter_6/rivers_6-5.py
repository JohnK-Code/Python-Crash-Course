#### TRY IT YOURSELF - Chapter 6 - Rivers 
rivers = {
    'nile': 'egypt',
    'amazon river': 'brazil',
    'yangtze river': 'china',
}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")


print("\n") # line break
for river in rivers.keys():
    print(river.title())


print("\n") # line break
for country in rivers.values():
    print(country.title())