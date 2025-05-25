def var_9383(var_6946, var_3619, var_7204):
    if not var_3619 >= var_7204:
        var_7235 = var_1719(var_6946, var_3619, var_7204)
        var_9383(var_6946, var_3619, var_7235 - 1)
        var_9383(var_6946, var_7235 + 1, var_7204)


def var_1719(var_6946, var_3619, var_7204):
    var_2397 = var_6946[var_7204]
    var_9582 = var_3619 - 1
    for var_7292 in range(var_3619, var_7204):
        if not var_6946[var_7292] > var_2397:
            var_9582 += 1
            var_6946[var_9582], var_6946[var_7292] = var_6946[var_7292], var_6946[var_9582]
    var_6946[var_9582 + 1], var_6946[var_7204] = var_6946[var_7204], var_6946[var_9582 + 1]
    return var_9582 + 1


var_6946 = [10, 7, 8, 9, 1, 5]
var_9383(var_6946, 0, len(var_6946) - 1)
print(var_6946)
