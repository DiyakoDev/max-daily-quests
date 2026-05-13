def flatten_list(nested_list):
    '''
    This function takes a nested list as input
    and returns a single list as output.
    '''
    flatten_lst = []

    for num in nested_list:
        if isinstance(num,list):
            for j in num:
                flatten_lst.append(j)
        else:
            flatten_lst.append(num)
            
    return sorted(flatten_lst)
    



print(flatten_list([10,20,[37,66,19],15,12,[1,5,9]]))