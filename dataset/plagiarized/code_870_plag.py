def var_7027(var_4110):
    var_1032 = 1
    var_5234(var_4110)


def var_5234(var_4110):
    while var_1032 < len(var_4110):
        var_9691 = var_4110[var_1032]
        var_3660 = var_1032 - 1
        while var_3660 >= 0 and var_4110[var_3660] > var_9691:
            var_4110[var_3660 + 1] = var_4110[var_3660]
            var_3660 -= 1
        var_4110[var_3660 + 1] = var_9691
        var_1032 += 1


var_4110 = [64, 34, 25, 12, 22, 11, 90]
var_7027(var_4110)
print(var_4110)
