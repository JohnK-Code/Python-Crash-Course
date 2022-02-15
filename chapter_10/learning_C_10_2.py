#### TRY IT YOURSELF - Chapter 10 - Page 191 - Learning C
filename = 'learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip().replace('Python', 'C'))        