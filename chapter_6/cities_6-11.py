#### TRY IT YOURSELF - Chapter 6 - Cities 
cities = {
    'new york': {
        'country': 'america',
        'population': '8,804,190',
        'fact': 'most populated city in america',
    },
    'london': {
        'country': 'united kingdom',
        'population': '9,425,622',
        'fact': 'it is the capital of england and the united kingdom'
    },
    'tokyo': {
        'country': 'japan',
        'population': '14,043,239',
        'fact': 'it has a population of 14 millon but the greater tokyo area has a population of 37.5 million'
    }
}
for city, info in cities.items():
    print(f"Here is some information about {city.title()}:")
    for title, details in info.items():
        print(f"\t{title.title()}: {details.title()}")
    print("\n") 