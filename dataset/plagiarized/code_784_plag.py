def var_2665(var_6456, var_1054, var_4574):
    var_2340 = len(var_6456)
    var_3247 = [(0) for var_3723 in range(var_4574 + 1)]
    var_5709 = 0
    while var_5709 < var_2340:
        for var_6696 in range(var_4574, var_1054[var_5709] - 1, -1):
            var_3247[var_6696] = var_1923(var_3247[var_6696], var_3247[
                var_6696 - var_1054[var_5709]] + var_6456[var_5709])
        var_5709 += 1
    return var_3247[var_4574]


print(var_2665([60, 100, 120], [10, 20, 30], 50))
