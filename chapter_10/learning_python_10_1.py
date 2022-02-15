#### TRY IT YOURSELF - Chapter 10 - Page 191 - Learning Python
# print entire contents of the file 
filename = 'learning_python.txt'
with open(filename) as file_object:
    contents = file_object.read()
print(contents)



# print ocntents of file by looping over the file object 
print("\n") # new line between exercises 
filename2 = 'learning_python.txt'
with open(filename2) as file_object2:
    for line in file_object2:
        print(line.strip()) # strip() used to remove newline added by the print function and text file



# print contents of file by storing each line in a list and then working on them outside the with block
print("\n") # new line between exercises 
filename3 = 'learning_python.txt'
with open(filename3) as file_object3:
    lines = file_object3.readlines()
for line in lines:
    print(line.strip())