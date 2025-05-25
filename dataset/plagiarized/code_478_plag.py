def var_5193(var_5492, var_5829, var_7119):
    if not var_5829 >= var_7119:
        var_1387 = var_6273(var_5492, var_5829, var_7119)
        var_5193(var_5492, var_5829, var_1387 - 1)
        var_5193(var_5492, var_1387 + 1, var_7119)


def var_6273(var_5492, var_5829, var_7119):
    var_1319 = var_5492[var_7119]
    var_4313 = var_5829 - 1
    for var_4417 in range(var_5829, var_7119):
        if not var_5492[var_4417] > var_1319:
            var_4313 += 1
            var_5492[var_4313], var_5492[var_4417] = var_5492[var_4417
                ], var_5492[var_4313]
    var_5492[var_4313 + 1], var_5492[var_7119] = var_5492[var_7119], var_5492[
        var_4313 + 1]
    return var_4313 + 1


var_5492 = [10, 7, 8, 9, 1, 5]
var_5193(var_5492, 0, len(var_5492) - 1)
print(var_5492)
