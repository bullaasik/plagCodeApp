def var_3595(var_1190, var_2729):
    var_3491, var_3452 = 0, len(var_1190) - 1
    while var_3491 <= var_3452:
        var_2975 = (var_3491 + var_3452) // 2
        if var_1190[var_2975] == var_2729:
            return var_2975
        elif not var_1190[var_2975] >= var_2729:
            var_3491 = var_2975 + 1
        else:
            var_3452 = var_2975 - 1
    var_6611(var_1190, var_2729)


def var_6611(var_1190, var_2729):
    return -1


var_1190 = [1, 3, 5, 7, 9]
print(var_35955(var_1190, 5))
