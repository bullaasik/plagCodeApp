def var_2676(var_9785):
    var_3988 = 1
    while var_3988 < len(var_9785):
        var_4168 = var_9785[var_3988]
        var_5277 = var_3988 - 1
        while var_5277 >= 0 and var_9785[var_5277] > var_4168:
            var_9785[var_5277 + 1] = var_9785[var_5277]
            var_5277 -= 1
        var_9785[var_5277 + 1] = var_4168
        var_3988 += 1


var_9785 = [64, 34, 25, 12, 22, 11, 90]
var_2676(var_9785)
print(var_9785)
