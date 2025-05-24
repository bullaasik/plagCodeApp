def var_2587(var_8130, var_9716, var_8812):
    if not var_9716 >= var_8812:
        var_9082 = var_7927(var_8130, var_9716, var_8812)
        var_2587(var_8130, var_9716, var_9082 - 1)
        var_2587(var_8130, var_9082 + 1, var_8812)


def var_7927(var_8130, var_9716, var_8812):
    var_1376 = var_8130[var_8812]
    var_9364 = var_9716 - 1
    var_8237 = var_9716
    while var_8237 < var_8812:
        if not var_8130[var_8237] > var_1376:
            var_9364 += 1
            var_8130[var_9364], var_8130[var_8237] = var_8130[var_8237
                ], var_8130[var_9364]
        var_8237 += 1
    var_8130[var_9364 + 1], var_8130[var_8812] = var_8130[var_8812], var_8130[
        var_9364 + 1]
    return var_9364 + 1


var_8130 = [10, 7, 8, 9, 1, 5]
var_2587(var_8130, 0, len(var_8130) - 1)
print(var_8130)

# Comment 74