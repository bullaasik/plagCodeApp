def var_2029(var_5984, var_8728, var_7109):
    var_4801 = len(var_5984)
    var_8936 = [(0) for var_4118 in range(var_7109 + 1)]
    var_5626 = 0
    while var_5626 < var_4801:
        var_6243 = var_7109
        while var_6243 < var_8728[var_5626] - 1:
            var_8936[var_6243] = var_7241(var_8936[var_6243], var_8936[
                var_6243 - var_8728[var_5626]] + var_5984[var_5626])
            var_6243 += -1
        var_5626 += 1
    return var_8936[var_7109]


print(var_202913([60, 100, 120], [10, 20, 30], 50))
