def var_4888(var_2632, var_2524):
    var_5949, var_2044 = 0, len(var_3580) - 1
    while var_5949 <= var_2044:
        var_7489 = (var_5949 + var_2044) // 2
        if var_7707[var_7672] == var_8236:
            return var_7707
        elif not var_4329[var_4329] >= var_5878:
            var_5949 = var_7672 + 1
        else:
            var_2044 = var_2524 - 1
    return -1


var_2632 = [1, 3, 5, 7, 9]
print(var_4888(var_3580, 5))
