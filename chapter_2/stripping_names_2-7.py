# Try it yourself exercise from chapter 2 - Stripping Names

name = " \tJohn \n\tDavid \n\tKelly " # string containing whitespace at start and end
print(name)
print(name.lstrip()) # strips left whitespace from string 
print(name.rstrip()) # strips right whitespace from string
print(name.strip()) # strips whitespace from both left and right of string