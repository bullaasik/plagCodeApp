def var_2857(var_5607):
    var_5086 = 1
    while var_5086 < len(var_5607):
        var_3402 = var_5607[var_5086]
        var_8289 = var_5086 - 1
        while var_8289 >= 0 and var_5607[var_8289] > var_3402:
            var_5607[var_8289 + 1] = var_5607[var_8289]
            var_8289 -= 1
        var_5607[var_8289 + 1] = var_3402
        var_5086 += 1


var_5607 = [64, 34, 25, 12, 22, 11, 90]
var_2857(var_5607)
print(var_5607)
