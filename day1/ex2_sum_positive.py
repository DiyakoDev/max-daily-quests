def sum_positive(numbers):
    total = 0
    for num in numbers:
        if num > 0:         
            total += num
    return total


print(sum_positive([10, -5, 20, -3, 0, 7]))  