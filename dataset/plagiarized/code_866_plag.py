def var_8254(var_2273, var_7402, var_7577):
    var_1961 = len(var_2273)
    var_5298 = [(0) for var_1487 in range(var_7577 + 1)]
    var_7923 = 0
    while var_7923 < var_1961:
        for var_9930 in range(var_7577, var_7402[var_7923] - 1, -1):
            var_5298[var_9930] = var_7670(var_5298[var_9930], var_5298[
                var_9930 - var_7402[var_7923]] + var_2273[var_7923])
        var_7923 += 1
    return var_5298[var_7577]


print(var_82544([60, 100, 120], [10, 20, 30], 50))
