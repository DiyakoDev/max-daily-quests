def sum_postive(list):
    total = 0
    for num in list:
        if num >= 0:
            total += num
    return total



print(sum_postive([10, -5, 20, -3, 0, 7]))