#### TRY IT YOURSELF - Chapter 8 - City Name
def city_country(city, country):
    """Return a city and country, neatly formatted"""
    location = f"{city}, {country}"
    return location.title()

formatted_location = city_country('new york', 'america')
print(formatted_location)

formatted_location = city_country('london', 'england')
print(formatted_location)

formatted_location = city_country('paris', 'france')
print(formatted_location)