#### TRY IT YOURSELF - Chapter 10 - Page 193 - Guest Book
print("Enter quit to finish.")
while True:
    name = input("Enter your name: ")
    if name == 'quit' or name == 'Quit':
        print("Goodbye!")
        break
    else:
        print(f"Welcome, {name.title()}.\n")
        with open('guest_book.txt', 'a') as file_object:
            file_object.write(f"{name.title()}\n")