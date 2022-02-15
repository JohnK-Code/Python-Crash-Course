#### TRY IT YOURSELF - Chapter 6 - Favorite Places
favorite_places = {
    'john': ['new york', 'london', 'los angeles'],
    'kirsty': ['paris', 'london', 'new york'],
    'vinny': ['home', 'garden', 'street'],
}
for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for city in places:
        print(f"\t{city.title()}")