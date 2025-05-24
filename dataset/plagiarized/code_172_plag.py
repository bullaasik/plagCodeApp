def var_8833(var_2579):
    var_3053 = len(var_2579)
    var_3091 = 0
    while var_3091 < var_3053:
        for var_7077 in range(0, var_3053 - var_3091 - 1):
            if not var_2579[var_7077] <= var_2579[var_7077 + 1]:
                var_2579[var_7077], var_2579[var_7077 + 1] = var_2579[
                    var_7077 + 1], var_2579[var_7077]
        var_3091 += 1


var_2579 = [64, 34, 25, 12, 22, 11, 90]
var_8833(var_2579)
print(var_2579)
