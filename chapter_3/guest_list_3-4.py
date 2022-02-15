# TRY IT YOURSELF - Guest List - Chapter 3 - 3.4
famous_people = ['Billy Connolly', 'Jeremy Clarkson', 'Bill Gates'] # List of famous people, I'd invite to dinner
print(f"I would like to invite {famous_people[0].title()} to dinner.")
print(f"I would like to invite {famous_people[1].title()} to dinner.")
print(f"I would like to invite {famous_people[2].title()} to dinner.")


# TRY IT YOURSELF - Changing Guest List - Chapter 3 - 3.5
print(f"\nUnfortunaly, {famous_people[1].title()} cant make it to the meal.")
famous_people[1] = "David Freiburger" # replace list value at index 1
print(f"I would like to invite {famous_people[0].title()} to dinner.")
print(f"I would like to invite {famous_people[1].title()} to dinner.")
print(f"I would like to invite {famous_people[2].title()} to dinner.")

# TRY IT YOURSELF - More Guests - Chapter 3 - 3.6
print("\nWe have found a bigger dinner table so can now invite more guests.")
famous_people.insert(0, 'Moog')
famous_people.insert(3, 'Barack Obama')
famous_people.insert(-1, 'Elon Musk')
print(f"I would like to invite {famous_people[0].title()} to dinner.")
print(f"I would like to invite {famous_people[1].title()} to dinner.")
print(f"I would like to invite {famous_people[2].title()} to dinner.")
print(f"I would like to invite {famous_people[3].title()} to dinner.")
print(f"I would like to invite {famous_people[4].title()} to dinner.")
print(f"I would like to invite {famous_people[5].title()} to dinner.")


# TRY IT YOURSELF - Shrinking Guest List - Chapter 3 - 3.7
print("\nUnfortunately our dinner table won't arrive in time and we now only have room for two dinner guests")
message = "Hi {}, we unfortunately no longer have room for six guest and have had to remove you from the dinner party. Sorry."
print(message.format(famous_people[-2].split(' ', 1)[0]))
famous_people.pop(-2)
print(message.format(famous_people[-2].split(' ', 1)[0]))
famous_people.pop(-2)
print(message.format(famous_people[-2].split(' ', 1)[0]))
famous_people.pop(-2)
print(message.format(famous_people[-0].split(' ', 1)[0]))
famous_people.pop(0)
print(f"Hi Mr {famous_people[0].split(' ', 1)[1]} and Mr {famous_people[1].split(' ', 1)[1]}, you are both still invited to our reduced sized dinner party, congratulations.")
del famous_people[0]
del famous_people[0]
print(famous_people)