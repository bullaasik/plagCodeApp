def var_6981(var_4193, var_8605, var_6164):
    var_1096 = len(var_4193)
    var_3258 = [(0) for var_9216 in range(var_6164 + 1)]
    var_9987 = 0
    while var_9987 < var_1096:
        for var_9169 in range(var_6164, var_8605[var_9987] - 1, -1):
            var_3258[var_9169] = var_3479(var_3258[var_9169], var_3258[
                var_9169 - var_8605[var_9987]] + var_4193[var_9987])
        var_9987 += 1
    return var_3258[var_6164]


print(var_6981([60, 100, 120], [10, 20, 30], 50))
