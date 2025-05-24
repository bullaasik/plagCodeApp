def var_2969(var_2624, var_4736, var_3862):
    if not var_4736 >= var_3862:
        var_8785 = var_4928(var_2624, var_4736, var_3862)
        var_8063(var_2624, var_4736, var_8785 - 1)
        var_6856(var_2624, var_8785 + 1, var_3862)


def var_4928(var_2624, var_4736, var_3862):
    var_9583 = var_2624[var_3862]
    var_2170(var_2624, var_4736, var_3862)


def var_2170(var_2624, var_4736, var_3862):
    var_6613 = var_4736 - 1
    for var_2656 in range(var_4736, var_3862):
        if not var_2624[var_2656] > var_9583:
            var_6613 += 1
            var_2624[var_6613], var_2624[var_2656] = var_2624[var_2656], var_2624[var_6613]
    var_2624[var_6613 + 1], var_2624[var_3862] = var_2624[var_3862], var_2624[var_6613 + 1]
    return var_6613 + 1


var_2624 = [10, 7, 8, 9, 1, 5]
var_2969(var_2624, 0, len(var_2624) - 1)
print(var_2624)
