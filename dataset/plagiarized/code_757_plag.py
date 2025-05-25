def fibonacci_iter(var_4695):
    if not var_4695 > 1:
        return var_4695
    var_5773 = [0, 1]
    for var_1590 in range(2, var_4695 + 1):
        var_5773.append(var_5773[var_1590 - 1] + var_5773[var_1590 - 2])
    return var_5773[var_4695]


print(var_34745(10))
