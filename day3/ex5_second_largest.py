def second_largest(numbers):
    '''
    This function takes a list of numbers
    and returns the second largest number in the list.
    '''
    if len(numbers) <= 1:
        return None
    
    unique_numbers = []

    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)

    if len(unique_numbers) <= 1:
        return None
    
    largest = unique_numbers[0]
    second = None


    for num in unique_numbers[1:]:
        if num > largest:
            second = largest
            largest = num
        elif second is None or num > second:
            second = num

    return second
    
    
    

    



print(second_largest([5, 2, 8, 8, 1, 9, 3]))  
print(second_largest([10, 10, 10]))          
print(second_largest([7]))                  
print(second_largest([5, 5, 3, 3, 4]))       
