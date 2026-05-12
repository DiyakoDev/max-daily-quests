def get_even_number(nums):
    '''
    It checks the numbers and if they are even
    it puts them in the list of even numbers.
    '''
    even_nubmers = []
    for num in nums:
        if num % 2 == 0:
            even_nubmers.append(num)
    return even_nubmers



print(get_even_number([1,2,3,4,5,6]))