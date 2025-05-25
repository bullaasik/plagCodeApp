def var_5739(var_3150, var_9017, var_8154):
    var_3385 = len(var_3150)
    var_3698 = [(0) for var_2927 in range(var_8154 + 1)]
    sub_var_5739_9588(var_3150, var_9017, var_8154)


def sub_var_5739_9588(var_3150, var_9017, var_8154):
    var_9693 = 0
    while var_9693 < var_3385:
        for var_1125 in range(var_8154, var_9017[var_9693] - 1, -1):
            var_3698[var_1125] = var_6888(var_3698[var_1125], var_3698[
                var_1125 - var_9017[var_9693]] + var_3150[var_9693])
        var_9693 += 1
    return var_3698[var_8154]


print(var_5739([60, 100, 120], [10, 20, 30], 50))
