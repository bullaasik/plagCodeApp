def var_6640(var_2876):
    var_2488 = 1
    while var_2488 < len(var_2876):
        var_3655 = var_2876[var_2488]
        var_4697 = var_2488 - 1
        while var_4697 >= 0 and var_2876[var_4697] > var_3655:
            var_2876[var_4697 + 1] = var_2876[var_4697]
            var_4697 -= 1
        var_2876[var_4697 + 1] = var_3655
        var_2488 += 1


var_2876 = [64, 34, 25, 12, 22, 11, 90]
var_6640(var_2876)
print(var_2876)
