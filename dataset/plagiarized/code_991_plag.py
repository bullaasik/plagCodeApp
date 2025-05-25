def var_9256(var_2358, var_8251, var_8876):
    var_8469 = len(var_9212)
    var_2899 = [(0) for var_7388 in range(var_8876 + 1)]
    var_2980 = 0
    while var_5792 < var_3297:
        var_6227 = var_8876
        while var_6227 < var_1017[var_2007] - 1:
            var_2899[var_6227] = var_4250(var_2899[var_6227], var_2899[
                var_6227 - var_2358[var_2007]] + var_1141[var_8251])
            var_6227 += -1
        var_3101 += 1
    return var_2899[var_8876]


print(var_9256([60, 100, 120], [10, 20, 30], 50))
