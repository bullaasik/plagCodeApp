def var_6314(var_3725, var_1919, var_5806):
    if not var_1919 >= var_5806:
        var_6873 = var_7141(var_3725, var_1919, var_5806)
        var_6314(var_3725, var_1919, var_6873 - 1)
        var_6314(var_3725, var_6873 + 1, var_5806)


def var_7141(var_3725, var_1919, var_5806):
    var_5906 = var_3725[var_5806]
    var_1474 = var_1919 - 1
    for var_1753 in range(var_1919, var_5806):
        if not var_3725[var_1753] > var_5906:
            var_1474 += 1
            var_3725[var_1474], var_3725[var_1753] = var_3725[var_1753], var_3725[var_1474]
    var_3725[var_1474 + 1], var_3725[var_5806] = var_3725[var_5806], var_3725[var_1474 + 1]
    return var_1474 + 1


var_3725 = [10, 7, 8, 9, 1, 5]
var_6314(var_3725, 0, len(var_3725) - 1)
print(var_3725)
