#### TRY IT YOURSELF - Chapter 9 - Page 181 - Lottery Analysis - Attempt 2 
from random import choice

def get_winning_numbers(possible_numbers):
    """Return the winning lottery numbers"""
    winning_numbers = []
    while len(winning_numbers) < 4:
        number = choice(possible_numbers)
        if number not in winning_numbers:
            winning_numbers.append(number)
    print(f"Any ticket matching these numbers will win a prize: {winning_numbers}")
    return winning_numbers

def get_my_ticket(possible_numbers):
    """Return the numbers on my lottery ticket"""
    my_numbers = []
    while len(my_numbers) < 4:
        number = choice(possible_numbers)
        if number not in my_numbers:
            my_numbers.append(number)
    print(f"Your numbers are: {my_numbers}")
    return my_numbers

def check_results(winning_numbers, my_numbers):
    for number in winning_numbers:
        if number not in my_numbers:
            return False

    return True

possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
#winning_numbers = get_winning_numbers(possible_numbers)
my_numbers = get_my_ticket(possible_numbers)
#print(my_numbers)
#print(check_results(winning_numbers, my_numbers))

plays = 0
won = False

while not won:
    winning_numbers = get_winning_numbers(possible_numbers)
    won = check_results(winning_numbers, my_numbers)
    plays += 1
    if plays == 1_000_000:
        break

if won:
    print(f"You won the lottery!!!")
    print(f"Your numbers: {my_numbers}")
    print(f"The winning numbers: {winning_numbers}")
    print(f"It took {plays} attempts to win.")
else:
    print("You didn't win!")
    print(f"Your numbers: {my_numbers}")
    print(f"The winning numbers: {winning_numbers}")
    print(f"You reached {plays} without winning.")