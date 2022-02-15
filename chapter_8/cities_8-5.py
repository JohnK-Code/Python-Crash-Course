#### TRY IT YOURSELF - Chapter 8 - Cities
def describe_city(name, country='america'):
    """Describe a city."""
    print(f"{name.title()} is in {country.title()}.")
describe_city('new york') 
describe_city('london', 'england')
describe_city(country='france', name='paris')