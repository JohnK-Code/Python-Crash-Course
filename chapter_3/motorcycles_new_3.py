#### Chapter 3 - Avoiding index errors when working with lists
motorcycles = ["honda", "yamaha", "suzuki"] # new list
print(motorcycles[3]) # creates an 'IndexError' because we tried to access an index value that doesn't exists - only have 3 values and tried to access the 4th
print(motorcycles[-1]) # will always return the last item in the list - the only way it will return an error is if the list is empty

