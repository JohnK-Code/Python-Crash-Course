#### TRY IT YOURSELF - Chapter 10 - Page 193 - Programming Poll
filename = 'programming_poll.txt'
print("Enter quit to finish the poll.")
while True:
    reason = input("Why do you like programming?: ")
    if reason == 'quit' or reason == 'Quit':
        print("Goodbye!")
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{reason}\n")