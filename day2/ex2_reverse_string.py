def reverse_string(s):
    '''
    This function takes a string and reverses it.
    '''
    reverse = ''
    for char in s:
        reverse = char + reverse
    return reverse

print(reverse_string("salam"))