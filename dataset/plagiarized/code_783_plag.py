def var_9866(var_7370):
    var_5973 = 1
    while var_5973 < len(var_7370):
        var_5727 = var_7370[var_5973]
        var_6335 = var_5973 - 1
        while var_6335 >= 0 and var_7370[var_6335] > var_5727:
            var_7370[var_6335 + 1] = var_7370[var_6335]
            var_6335 -= 1
        var_7370[var_6335 + 1] = var_5727
        var_5973 += 1


var_7370 = [64, 34, 25, 12, 22, 11, 90]
var_9866(var_7370)
print(var_7370)
