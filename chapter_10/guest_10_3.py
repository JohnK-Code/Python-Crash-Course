#### TRY IT YOURSELF - Chapter 10 - Page 193 - Guest 
name = input("Enter your name: ")
filename = 'guest.txt'
with open(filename, 'w') as file_object:
    file_object.write(name)