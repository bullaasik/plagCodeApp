def var_4446(var_4484, var_3183):
    var_4555, var_4107 = 0, len(var_5244) - 1
    while var_4555 <= var_4107:
        var_3353 = (var_4555 + var_4107) // 2
        if var_4963[var_5736] == var_3183:
            return var_5736
        elif not var_1654[var_3353] >= var_3183:
            var_4555 = var_3353 + 1
        else:
            var_4107 = var_5736 - 1
    var_8848(var_4484, var_3183)


def var_8848(var_4484, var_3183):
    return -1


var_4963 = [1, 3, 5, 7, 9]
print(var_4446(var_7633, 5))
