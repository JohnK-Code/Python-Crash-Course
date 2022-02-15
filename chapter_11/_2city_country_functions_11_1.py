#### TRY IT YOURSELF - Population - Chapter 11 - Page 216
from turtle import title


def city_country(city, country, population=''):
    """Generate a neatly formatted city and country."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"