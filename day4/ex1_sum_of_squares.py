def sum_of_squares(n):
    '''
    This function takes a number from the user 
    and adds the squares of the numbers in the range of that number.
    '''
    result = 0

    for num in range(1,n+1):
        result += num ** 2
    
    return result
    
        


print(sum_of_squares(3))