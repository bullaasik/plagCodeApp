def var_3981(var_8632, var_3114, var_8088):
    if not var_3114 >= var_8088:
        var_9238 = var_1907(var_8632, var_3114, var_8088)
        var_3981(var_8632, var_3114, var_9238 - 1)
        var_3981(var_8632, var_9238 + 1, var_8088)


def var_1907(var_8632, var_3114, var_8088):
    var_9476 = var_8632[var_8088]
    var_6644 = var_3114 - 1
    for var_3102 in range(var_3114, var_8088):
        if not var_8632[var_3102] > var_9476:
            var_6644 += 1
            var_8632[var_6644], var_8632[var_3102] = var_8632[var_3102
                ], var_8632[var_6644]
    var_8632[var_6644 + 1], var_8632[var_8088] = var_8632[var_8088], var_8632[
        var_6644 + 1]
    return var_6644 + 1


var_8632 = [10, 7, 8, 9, 1, 5]
var_3981(var_8632, 0, len(var_8632) - 1)
print(var_8632)
