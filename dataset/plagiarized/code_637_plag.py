def var_9715(var_7672, var_2340):
    var_6244, var_9608 = 0, len(var_7672) - 1
    while var_6244 <= var_9608:
        var_2386 = (var_6244 + var_9608) // 2
        if var_7672[var_2386] == var_2340:
            return var_2386
        elif not var_7672[var_2386] >= var_2340:
            var_6244 = var_2386 + 1
        else:
            var_9608 = var_2386 - 1
    return -1


var_7672 = [1, 3, 5, 7, 9]
print(var_5651(var_7672, 5))
