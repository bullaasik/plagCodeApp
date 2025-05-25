def var_2823(var_4652):
    if  not var_4652 > 1:
        return var_4652
    var_7973 = [0, 1]
    var_3402 = 2
    while var_3402 < var_4652 + 1:
        var_7973.append(var_7973[var_3402 - 1] + var_7973[var_3402 - 2])
        var_3402 += 1
    return var_7973[var_4652]


print(var_2823(10))

# Comment 15