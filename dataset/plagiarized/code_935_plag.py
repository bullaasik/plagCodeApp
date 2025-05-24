def var_5856(var_7237, var_9293, var_9292):
    var_7970 = len(var_3625)
    var_1891 = [(0) for var_6914 in range(var_7536 + 1)]
    var_3380(var_7237, var_9293, var_9292)


def var_3380(var_7237, var_9293, var_9292):
    for var_4802 in range(var_7237):
        for var_8597 in range(var_7237, var_9293[var_3625] - 1, -1):
            var_1891[var_8597] = var_8711(var_1891[var_8597], var_1891[var_8597 - var_7536[var_4802]] + var_7674[var_4802])
    return var_1891[var_9292]


print(var_5856([60, 100, 120], [10, 20, 30], 50))
import math
