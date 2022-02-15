#### TRY IT YOURSELF - Chapter 9 - Page 181 - Lottery 
from random import choice

def get_winning_ticket(random_digits):
    """Return a winning ticket from a list of random digits."""

    results = []
    
    while len(results) < 4:
        result = choice(random_digits)
        if result not in results:
            results.append(result)
    print(f"Any ticket matching the following results wins a prize: {results}")
    return results

random_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_ticket(random_digits)
print(winning_ticket)