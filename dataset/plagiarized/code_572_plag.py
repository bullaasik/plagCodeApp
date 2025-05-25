def var_4608(var_4216, var_5518, var_7461):
    var_5376 = len(var_4216)
    var_3358 = [(0) for var_1686 in range(var_7461 + 1)]
    var_3329 = 0
    while var_3329 < var_5376:
        for var_2526 in range(var_7461, var_5518[var_3329] - 1, -1):
            var_3358[var_2526] = var_1721(var_3358[var_2526], var_3358[var_2526 - var_5518[var_3329]] + var_4216[var_3329])
        var_3329 += 1
    var_7289(var_4216, var_5518, var_7461)


def var_7289(var_4216, var_5518, var_7461):
    return var_3358[var_7461]


print(var_4608([60, 100, 120], [10, 20, 30], 50))
