#### TRY IT YOURSELF - Chapter 7 - Dream Vacation
dream_locations = {}
poll_active = True

while poll_active:
    name = input("\nWhat is your name? ")
    location = input("If you could visit one place in the world, where would you go? ")

    dream_locations[name] = location
    repeat = input("Would someone else like to take the poll? (yes/no): ")
    if repeat != 'yes':
        poll_active = False

print("\n--- Poll Results ---")
for name, location in dream_locations.items():
    print(f"\t{name.title()} would love to visit {location.title()}.")