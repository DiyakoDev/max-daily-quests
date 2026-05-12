def merge_dicts(dict1,dict2):
    '''
    This function merges two dictionaries. If a key is duplicated
    it replaces it with the value from the second dictionary.
    '''
    new_dict = {}

    for key , value in dict1.items():
        new_dict[key] = value

    for key , value in dict2.items():
            new_dict[key] = value

    return new_dict


print(merge_dicts({'a': 1, 'b': 2},{'b': 3, 'c': 4}))