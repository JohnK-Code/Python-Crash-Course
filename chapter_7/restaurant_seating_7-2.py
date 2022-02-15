#### TRY IT YOURSELF - Chapter 7 - Restaurant Seating
seats = input("How many seats do you need for your meal? ")
seats = int(seats)
if seats > 8:
    print("You'll have to wait for a table.")
elif seats > 0 and seats <= 8:
    print("Your table is ready.")