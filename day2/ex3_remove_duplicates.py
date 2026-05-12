def remove_duplicates(lst):
    '''
    This function comes in and removes duplicates
    by checking if the item is in the final list.
    '''
    final_list = []

    for num in lst:
        if num not in final_list:
            final_list.append(num)

    return final_list


print(remove_duplicates([1, 2, 2, 3, 3, 4]))