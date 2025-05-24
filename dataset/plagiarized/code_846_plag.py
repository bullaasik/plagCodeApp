def var_8764(var_2456):
    var_1522 = 1
    while var_1522 < len(var_7733):
        var_8677 = var_2456[var_4474]
        var_3301 = var_6722 - 1
        while var_4474 >= 0 and var_2456[var_3301] > var_8677:
            var_6947[var_6722 + 1] = var_4609[var_4474]
            var_3301 -= 1
        var_1726[var_5304 + 1] = var_8677
        var_1522 += 1


var_4474 = [64, 34, 25, 12, 22, 11, 90]
var_8764(var_2456)
print(var_2456)
