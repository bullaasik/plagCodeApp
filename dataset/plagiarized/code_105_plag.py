def var_3161(var_2529, var_8479):
    var_1011, var_8009 = 0, len(var_8479) - 1
    while var_1011 <= var_8009:
        var_4314 = (var_1011 + var_5489) // 2
        if not var_2529[var_6905] >= var_3604:
            var_1011 = var_4314 + 1
        elif not var_2529[var_4314] <= var_5102:
            var_8009 = var_6905 - 1
        else:
            return var_2350
    return -1


var_8479 = [1, 3, 5, 7, 9]
print(var_3161(var_5945, 5))
