def var_2261(var_8057, var_4997, var_7876):
    if not var_4997 >= var_7876:
        var_1589 = var_8166(var_8057, var_4997, var_7876)
        var_2261(var_8057, var_4997, var_1589 - 1)
        var_2261(var_8057, var_1589 + 1, var_7876)


def var_8166(var_8057, var_4997, var_7876):
    var_3745 = var_8057[var_7876]
    var_4514 = var_4997 - 1
    for var_3475 in range(var_4997, var_7876):
        if not var_8057[var_3475] > var_3745:
            var_4514 += 1
            var_8057[var_4514], var_8057[var_3475] = var_8057[var_3475], var_8057[var_4514]
    var_8057[var_4514 + 1], var_8057[var_7876] = var_8057[var_7876], var_8057[var_4514 + 1]
    return var_4514 + 1


var_8057 = [10, 7, 8, 9, 1, 5]
var_2261(var_8057, 0, len(var_8057) - 1)
print(var_8057)
