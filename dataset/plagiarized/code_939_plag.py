def var_9267(var_9273):
    for var_2161 in range(1, len(var_9273)):
        var_4875 = var_9273[var_2161]
        var_5342 = var_2161 - 1
        while var_5342 >= 0 and var_9273[var_5342] > var_4875:
            var_9273[var_5342 + 1] = var_9273[var_5342]
            var_5342 -= 1
        var_9273[var_5342 + 1] = var_4875


var_9273 = [64, 34, 25, 12, 22, 11, 90]
var_9267(var_9273)
print(var_9273)
