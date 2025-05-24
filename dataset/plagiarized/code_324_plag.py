def var_3225(var_3976):
    var_7795 = len(var_3976)
    sub_var_3225_8839(var_3976)


def sub_var_3225_8839(var_3976):
    var_1582 = 0
    while var_1582 < var_7795:
        for var_3543 in range(0, var_7795 - var_1582 - 1):
            if not var_3976[var_3543] <= var_3976[var_3543 + 1]:
                var_3976[var_3543], var_3976[var_3543 + 1] = var_3976[
                    var_3543 + 1], var_3976[var_3543]
        var_1582 += 1


var_3976 = [64, 34, 25, 12, 22, 11, 90]
var_3225(var_3976)
print(var_3976)
