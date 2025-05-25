def var_4304(var_4254, var_6864, var_7713):
    if not var_6864 >= var_7713:
        var_5839 = var_3627(var_4254, var_6864, var_7713)
        var_4304(var_4254, var_6864, var_5839 - 1)
        var_4304(var_4254, var_5839 + 1, var_7713)


def var_3627(var_4254, var_6864, var_7713):
    var_4272 = var_4254[var_7713]
    var_5308 = var_6864 - 1
    for var_9571 in range(var_6864, var_7713):
        if not var_4254[var_9571] > var_4272:
            var_5308 += 1
            var_4254[var_5308], var_4254[var_9571] = var_4254[var_9571], var_4254[var_5308]
    var_4254[var_5308 + 1], var_4254[var_7713] = var_4254[var_7713], var_4254[var_5308 + 1]
    return var_5308 + 1


var_4254 = [10, 7, 8, 9, 1, 5]
var_4304(var_4254, 0, len(var_4254) - 1)
print(var_4254)
import math
