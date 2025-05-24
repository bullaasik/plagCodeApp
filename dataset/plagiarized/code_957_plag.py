def var_5512(var_5055, var_1594, var_9605):
    var_1864 = len(var_5055)
    var_2120 = [(0) for var_6540 in range(var_9605 + 1)]
    var_3609 = 0
    var_6579(var_5055, var_1594, var_9605)


def var_6579(var_5055, var_1594, var_9605):
    while var_3609 < var_1864:
        for var_2525 in range(var_9605, var_1594[var_3609] - 1, -1):
            var_2120[var_2525] = var_9587(var_2120[var_2525], var_2120[
                var_2525 - var_1594[var_3609]] + var_5055[var_3609])
        var_3609 += 1
    return var_2120[var_9605]


print(var_5512([60, 100, 120], [10, 20, 30], 50))
