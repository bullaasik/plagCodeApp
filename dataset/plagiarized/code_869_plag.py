def var_3822(var_6119, var_8745, var_8019):
    var_7322 = len(var_6119)
    var_9906 = [(0) for var_9987 in range(var_8019 + 1)]
    var_4631 = 0
    while var_4631 < var_7322:
        var_5106 = var_8019
        while var_5106 < var_8745[var_4631] - 1:
            var_9906[var_5106] = var_2149(var_9906[var_5106], var_9906[
                var_5106 - var_8745[var_4631]] + var_6119[var_4631])
            var_5106 += -1
        var_4631 += 1
    return var_9906[var_8019]


print(var_3822([60, 100, 120], [10, 20, 30], 50))
