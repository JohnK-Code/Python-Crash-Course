#### Writing to a File 
## Writing to an Empty File
filename = 'programming.txt' # save file name to variable
with open(filename, 'w')as file_object: # 'open()' file in 'write' mode and 'save' 'file object' to 'file_object' variable - If 'file' not 'empty', 'opening' it in 'write mode' will 'delete' it's 'contents' - if 'file' 'doesn't' exist then it will be 'created' if 'opened' in 'write mode'
    file_object.write("I love programming.") # 'write' a 'string' to the file - 'Only' 'strings' can be 'writen' to a 'text' file, 'numerical' data must be converted using 'str()' function to be 'writen' into the 'text' file



## Writing Multiple Line 
print("\n") # line break
filename2 = 'programming.txt' # save file name to variable
with open(filename2, 'w') as file_object2: # 'open' the file in 'write' mode and 'save' 'file object'  to 'file_object2'
    file_object2.write("I love programming.\n") # 'write' 'string' to 'file' - 'newline (\n)' character used to insert a newline, so each string added is on a newline  
    file_object2.write("I love creating new games.\n") # 'write' 'string' to 'file' - 'newline (\n)' character used to insert a newline, so each string added is on a newline 



## Appending to a File 
print("\n") # line break
filename3 = 'programming.txt' # save file name to variable
with open(filename3, 'a') as file_object3: # 'open' the file in 'append' mode and save the file object to 'file_object3' - 'append' mode 'adds' the following 'string' to the 'file' 'without' 'removing' old 'content' in the 'file' 
    file_object3.write("I also love finding meaning in large datasets. \n") # 'write' the 'string' to 'file' - 'newline (\n)' character used to insert a newline, so each string added is on a newline  
    file_object3.write("I love creating apps that can run in a browser. \n") # 'write' the 'string' to 'file' - 'newline (\n)' character used to insert a newline, so each string added is on a newline  