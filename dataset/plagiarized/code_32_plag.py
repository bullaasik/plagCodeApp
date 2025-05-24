def var_9067(var_5032, var_3393):
    var_3533, var_1520 = 0, len(var_5032) - 1
    while var_3533 <= var_1520:
        var_3989 = (var_3533 + var_1520) // 2
        if not var_5032[var_3989] >= var_3393:
            var_3533 = var_3989 + 1
        elif not var_5032[var_3989] <= var_3393:
            var_1520 = var_3989 - 1
        else:
            return var_3989
    return -1


var_5032 = [1, 3, 5, 7, 9]
print(var_9067(var_5032, 5))
