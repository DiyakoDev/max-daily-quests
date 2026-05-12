
def is_palindrome(s):
    '''
    This function uses the reverse_string function to check whether
    the reversed string is equal to the normal string.
    '''
    def reverse_string(s):
        '''
        This function takes a string and reverses it.
        '''
        reverse = ''
        for char in s:
            reverse = char + reverse
        return reverse
    if reverse_string(s) == s:
        return True
    else:
        return False
    


print(is_palindrome("radar"))   # True
print(is_palindrome("hello"))   # False
print(is_palindrome("level"))   # True