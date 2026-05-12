def common_keys(dict1,dict2):
    '''
    We give the function two dictionaries and it gives us their common keys.
    '''
    common_key = []
    keys = []

    for key in dict1:
        common_key.append(key)

    for key in dict2:
        if key in common_key:
            keys.append(key)
        else:
            common_key.append(key)

    return keys

print(common_keys({'a': 1, 'b': 2, 'c': 3},{'b': 4, 'c': 5, 'd': 6}))
