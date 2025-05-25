def var_6065(var_7482):
    var_6016 = 1
    while var_6016 < len(var_7482):
        var_9925 = var_7482[var_6016]
        var_8131 = var_6016 - 1
        while var_8131 >= 0 and var_7482[var_8131] > var_9925:
            var_7482[var_8131 + 1] = var_7482[var_8131]
            var_8131 -= 1
        var_7482[var_8131 + 1] = var_9925
        var_6016 += 1


var_7482 = [64, 34, 25, 12, 22, 11, 90]
var_6065(var_7482)
print(var_7482)
