def calculator(n, m, ls):
    lst = [sum(ls[i:i+m]) for i in range(0, n, m)]
    total_value = 0
    for i, it in enumerate(lst):
        if i % 2 == 0:
            total_value += it
        else:
           total_value -= it
    return total_value

# Local Tests
print(calculator(8, 3, [1, 2, 3, 4, 5, 6, 7, 8]))
print(calculator(8, 1, [1, 2, 3, 4, 5, 6, 7, 8]))
print(calculator(10, 1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
