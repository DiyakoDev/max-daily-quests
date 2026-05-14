def count_case(s):
    '''
    This function takes a string from the user 
    and returns the number of uppercase and lowercase letters in a dictionary.
    '''
    counter = {
        'upper':len([char for char in s if char.isupper()]),
        'lower':len([char for char in s if char.islower()])
    }

    return counter

print(count_case("Hello World"))