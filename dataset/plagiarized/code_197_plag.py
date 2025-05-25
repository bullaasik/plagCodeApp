def var_5097(var_4308):
    var_8449 = len(var_4308)
    var_2477 = 0
    while var_2477 < var_8449:
        var_6309 = 0
        while var_6309 < var_8449 - var_2477 - 1:
            if not var_4308[var_6309] <= var_4308[var_6309 + 1]:
                var_4308[var_6309], var_4308[var_6309 + 1] = var_4308[
                    var_6309 + 1], var_4308[var_6309]
            var_6309 += 1
        var_2477 += 1


var_4308 = [64, 34, 25, 12, 22, 11, 90]
var_5097(var_4308)
print(var_4308)
