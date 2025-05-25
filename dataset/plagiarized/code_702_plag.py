def var_7091(var_1966, var_8599, var_2903):
    var_2079 = len(var_1966)
    var_1965 = [(0) for var_1016 in range(var_2903 + 1)]
    var_6757 = 0
    while var_6757 < var_2079:
        for var_2498 in range(var_2903, var_8599[var_6757] - 1, -1):
            var_1965[var_2498] = var_3916(var_1965[var_2498], var_1965[
                var_2498 - var_8599[var_6757]] + var_1966[var_6757])
        var_6757 += 1
    return var_1965[var_2903]


print(var_70911([60, 100, 120], [10, 20, 30], 50))

# Comment 11