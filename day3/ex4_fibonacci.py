def fibonacci(n):
    '''
    This function takes an input number
    from the user and returns the Fibonacci number.
    '''
    if n == 0:
        return []
    
    a , b = 0 , 1
    result = []

    for _ in range(n):
        result.append(a)
        a , b = b , a + b
    return result


print(fibonacci(7))



