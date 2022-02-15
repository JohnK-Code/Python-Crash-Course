# TRY IT YOURSELF - Chapter 3 
### Seeing the World 3-8
favorite_destinations = ["New York", "London", "Los Angeles", "Tokyo", "Sydney"]
print("Original list order of some of my dream destinations:")
print(favorite_destinations) 

print("\nList sorted alphabetically - This is temporary:")
print(sorted(favorite_destinations))

print("\nThe original list was not modified by using the sorted method.")
print(favorite_destinations)

print("\nList in reverse alphabetical order - This is temporary:")
print(sorted(favorite_destinations, reverse=True))

print("\nThe orginal list was again not modified in anyway by using the sorted method.")
print(favorite_destinations)

print("\nList in reverse order - This is permanent:")
favorite_destinations.reverse()
print(favorite_destinations)

print("\nList reversed back to original order - This is permanent:")
favorite_destinations.reverse()
print(favorite_destinations)

print("\nList sorted alphabetically - This is permanent:")
favorite_destinations.sort()
print(favorite_destinations)

print("\nList sorted in reverse alphabetical order - This is Permanent:")
favorite_destinations.sort(reverse=True)
print(favorite_destinations)


### Dinner Guests 3-9 - Uses the code from the previous 3-7 exercise called Dinner Guests also
famous_people = ["Billy Connolly", "Bill Gates"]
print(f"\nI am inviting {str(len(famous_people))} famous people to my dinner party.")