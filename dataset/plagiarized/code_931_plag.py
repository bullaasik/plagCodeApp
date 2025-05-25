def var_7807(var_3017):
    for var_7185 in range(1, len(var_3017)):
        var_7780 = var_3017[var_7185]
        var_8135 = var_7185 - 1
        while var_8135 >= 0 and var_3017[var_8135] > var_7780:
            var_3017[var_8135 + 1] = var_3017[var_8135]
            var_8135 -= 1
        var_3017[var_8135 + 1] = var_7780


var_3017 = [64, 34, 25, 12, 22, 11, 90]
var_7807(var_3017)
print(var_3017)
