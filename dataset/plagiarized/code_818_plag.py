def var_1732(v6, var_9876):
    var_8483, var_9715 = 0, len(var_8533) - 1
    while var_8483 <= var_9715:
        var_8533 = (var_8483 + var_9715) // 2
        if var_6518[var_5918] == var_1145:
            return var_9876
        elif not var_4302[var_8533] >= var_1145:
            var_8483 = var_5918 + 1
        else:
            var_9715 = var_8533 - 1
    return -1


var_4302 = [1, 3, 5, 7, 9]
print(var_17325(var_7360, 5))

# Comment 62