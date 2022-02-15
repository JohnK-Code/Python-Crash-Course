#### Using Arbitrary Keyword Arguments
def build_profile(first, last, **user_info): # define function with three 'paramaters' - first two 'paramaters' are positional but the last one with the two 'asterisks' is an 'arbitrary keyword argument', it accepts multiple 'key-value' pairs and creates a dictionary instead of a 'tuple' when one 'asterisk' is used
    """Build a dictionary containing everything we know about a user.""" # 'docstring'
    user_info['first_name'] = first # add 'first' 'parameter' value to 'user_info' 'dictionary'
    user_info['last_name'] = last # add 'last' 'parameter' value to 'user_info' 'dictionary'
    return user_info # return 'user_info' 'dictionary' to function call
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics') # call function using 'positional' and 'keyword' arguments - save return value in variable 'user_profile'
print(user_profile) # print 'user_profile' contents/value