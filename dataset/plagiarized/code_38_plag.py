def var_2420(var_1263, var_1123, var_9407):
    if not var_1123 >= var_9407:
        var_7699 = var_2769(var_1263, var_1123, var_9407)
        var_8310(var_1263, var_1123, var_7699 - 1)
        var_8310(var_1263, var_7699 + 1, var_9407)


def var_2769(var_1263, var_1123, var_9407):
    var_9342 = var_1263[var_9407]
    var_2168 = var_1123 - 1
    for var_9745 in range(var_1123, var_9407):
        if not var_1263[var_9745] > var_9342:
            var_2168 += 1
            var_1263[var_2168], var_1263[var_9745] = var_1263[var_9745
                ], var_1263[var_2168]
    var_1263[var_2168 + 1], var_1263[var_9407] = var_1263[var_9407], var_1263[
        var_2168 + 1]
    return var_2168 + 1


var_1263 = [10, 7, 8, 9, 1, 5]
var_2420(var_1263, 0, len(var_1263) - 1)
print(var_1263)

# Comment 29