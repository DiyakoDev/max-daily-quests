def common_elements(lst1,lst2):
    '''
    This function receives two lists and returns the union of the two sets.
    '''
    new_list = [num for num in lst1 if num in lst2]
    return new_list


print(common_elements([5,7,10,15,4],[4,15,9,13,12]))
    