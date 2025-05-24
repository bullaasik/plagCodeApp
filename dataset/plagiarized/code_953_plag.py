def fibonacci_iter(var_9884):
    if  not var_9884 > 1:
        return var_9884
    var_1468 = [0, 1]
    for var_9113 in range(2, var_9884 + 1):
        var_1468.append(var_1468[var_9113 - 1] + var_1468[var_9113 - 2])
    return var_1468[var_9884]


print(var_2112(10))

# Comment 38
# Comment 27