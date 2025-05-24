def var_5151(var_5884, var_5444):
    var_2461, var_2963 = 0, len(var_5884) - 1
    while var_2461 <= var_2963:
        var_9903 = (var_2461 + var_2963) // 2
        if var_5884[var_9903] == var_5444:
            return var_9903
        elif not var_5884[var_9903] >= var_5444:
            var_2461 = var_9903 + 1
        else:
            var_2963 = var_9903 - 1
    return -1


var_5884 = [1, 3, 5, 7, 9]
print(var_5151(var_5884, 5))
