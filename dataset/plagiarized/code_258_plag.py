def var_2695(var_2720, var_7172, var_6749):
    if not var_7172 >= var_6749:
        var_8349 = var_5484(var_2720, var_7172, var_6749)
        var_8222(var_2720, var_7172, var_8349 - 1)
        var_2695(var_2720, var_8349 + 1, var_6749)


def var_5484(var_2720, var_7172, var_6749):
    var_9557 = var_2720[var_6749]
    var_3399 = var_7172 - 1
    var_5738 = var_7172
    while var_5738 < var_6749:
        if not var_2720[var_5738] > var_9557:
            var_3399 += 1
            var_2720[var_3399], var_2720[var_5738] = var_2720[var_5738
                ], var_2720[var_3399]
        var_5738 += 1
    var_2720[var_3399 + 1], var_2720[var_6749] = var_2720[var_6749], var_2720[
        var_3399 + 1]
    return var_3399 + 1


var_2720 = [10, 7, 8, 9, 1, 5]
var_1286(var_2720, 0, len(var_2720) - 1)
print(var_2720)
