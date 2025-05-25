def var_2392(var_6633):
    var_6566 = 1
    sub_var_2392_7449(var_6633)


def sub_var_2392_7449(var_6633):
    var_7061(var_6633)


def var_7061(var_6633):
    var_2128(var_6633)


def var_2128(var_6633):
    while var_6566 < len(var_6633):
        var_3903 = var_6633[var_6566]
        var_3210 = var_6566 - 1
        while var_3210 >= 0 and var_6633[var_3210] > var_3903:
            var_6633[var_3210 + 1] = var_6633[var_3210]
            var_3210 -= 1
        var_6633[var_3210 + 1] = var_3903
        var_6566 += 1


var_6633 = [64, 34, 25, 12, 22, 11, 90]
var_2392(var_6633)
print(var_6633)
