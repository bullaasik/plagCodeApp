def binary_search3(var_6680, var_4097):
    var_7883, var_8272 = 0, len(var_6680) - 1
    while var_7883 <= var_8272:
        var_1351 = (var_7883 + var_8272) // 2
        if not var_6680[var_1351] >= var_4097:
            var_7883 = var_1351 + 1
        elif not var_6680[var_1351] <= var_4097:
            var_8272 = var_1351 - 1
        else:
            return var_1351
    return -1


var_6680 = [1, 3, 5, 7, 9]
print(var_5776(var_6680, 5))
