### Chapter 3 - Basic List - Bicycles 

bicycles = ['trek', 'cannondale', 'redline', 'specialized'] # a basic list - uses square brackets and values seperated by commas
print(bicycles) # prints list values and the square brackets they are in

# list indexes start at 0 and not 1
print(bicycles[0]) # square bracket is used after the list name to acces the value at the index number entered - prints 'trek'
# gets the second element by using index 1
print(bicycles[1].title()) # accesing the list value at index 1 and capitalizing the value using the 'title' method - prints 'Connandale'
print(bicycles[3]) # gets the 4th element by using index 3
print(bicycles[-1]) # using minus one as the the index accesses the last item in the list - minus two would return the second last item and minus three the third last item 


### Using Individual Items from a List
message = f"My first bicycle was a {bicycles[0].title()}." # add the value at index 0 of the list 'bicycles' to the string value in the 'message' variable. The list value is also capitalized using the 'title' method
print(message) # print message containing the capitalized 'bicycles' value

