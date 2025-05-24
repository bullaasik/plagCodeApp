def var_3686(var_9180, var_1913, var_3926):
    var_7292 = len(var_9180)
    var_4089 = [(0) for var_3055 in range(var_3926 + 1)]
    var_6453 = 0
    while var_6453 < var_7292:
        var_2135 = var_3926
        while var_2135 < var_1913[var_6453] - 1:
            var_4089[var_2135] = var_5236(var_4089[var_2135], var_4089[
                var_2135 - var_1913[var_6453]] + var_9180[var_6453])
            var_2135 += -1
        var_6453 += 1
    var_2974(var_9180, var_1913, var_3926)


def var_2974(var_9180, var_1913, var_3926):
    return var_4089[var_3926]


print(var_3686([60, 100, 120], [10, 20, 30], 50))
