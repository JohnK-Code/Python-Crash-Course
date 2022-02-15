#### TRY IT YOURSELF - Chapter 9 - Page 181 - Lottery Analysis
## Code from exercise lottery_9_14.py
from random import choice

def get_winning_numbers(random_digits):
    """Return a winning ticket from a list of random digits."""

    results = []
    
    while len(results) < 4:
        result = choice(random_digits)
        if result not in results:
            results.append(result)
    print(f"Any ticket matching the following results wins a prize: {results}")
    return results


## New code 
def get_my_ticket():
    """Create and return your current ticket to find a match"""
    
    my_ticket = []

    while len(my_ticket) < 4:
        number = choice(random_digits)
        if number not in my_ticket:
            my_ticket.append(number)
    return my_ticket


def check_my_ticket(my_ticket, win_numbers):
    """Check if my ticket matches the winnning numbers"""
    for element in my_ticket:
        if element not in win_numbers:
            return False

    return True


random_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_numbers(random_digits)

win = False
played = 0

maximum_tries = 1_000_000


while not win:
    new_ticket = get_my_ticket()
    won = check_my_ticket(new_ticket, winning_ticket)
    played += 1
    if played >= maximum_tries:
        break

if won:
    print("You are a winner!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning numbers: {winning_ticket}")
    print(f"It took {played} attempts to win!")
else:
    print("You did not win!!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning numbers: {winning_ticket}")
    print("Please try again!")