def binary_search4(var_6340, var_2804):
    var_7865, var_4256 = 0, len(var_6340) - 1
    while var_7865 <= var_4256:
        var_6336 = (var_7865 + var_4256) // 2
        if not var_6340[var_6336] >= var_2804:
            var_7865 = var_6336 + 1
        elif not var_6340[var_6336] <= var_2804:
            var_4256 = var_6336 - 1
        else:
            return var_6336
    return -1


var_6340 = [1, 3, 5, 7, 9]
print(var_4769(var_6340, 5))
