#### TRY IT YOURSELF - Chapter 6 - Glossary
#### Fixing exercise 'glossary_6-3.py' to use a loop instead of repetative 'print' statements
glossary = {
    'dictionary': 'A colection of key-value pairs.',
    'variable': 'A container for storing data values.',
    'list': 'A collection of data value stored in a single variable.',
    'string': 'A data type surounded by quotes that make all within the quotes a single value.',
    'if': 'A conditional operation that is used to check if a condition is True or False.',
    'set': 'A built-in python data type used to store collections of data.',
    'for': 'Used to loop over a sequance of data such as a list or set',
    'tutple': 'Built-in data type for storing collections of data in a variable that are ordered and unchangeable',
    'function': 'A function is a block of code that is only run when it is called.',
    'boolean': 'Booleans represent one of two values, True or False'
}
for key, value in glossary.items():
    print(f"{key}: {value}")