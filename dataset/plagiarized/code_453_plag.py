def var_9704(var_2829, var_3871, var_1599):
    var_6318 = len(var_2829)
    var_5877 = [[(0) for var_7491 in range(var_1599 + 1)] for var_7491 in
        range(var_6318 + 1)]
    var_1583 = 1
    while var_1583 < var_6318 + 1:
        for var_6853 in range(var_1599 + 1):
            if not var_3871[var_1583 - 1] > var_6853:
                var_5877[var_1583][var_6853] = var_5073(var_5877[var_1583 -
                    1][var_6853], var_5877[var_1583 - 1][var_6853 -
                    var_3871[var_1583 - 1]] + var_2829[var_1583 - 1])
            else:
                var_5877[var_1583][var_6853] = var_5877[var_1583 - 1][var_6853]
        var_1583 += 1
    return var_5877[var_6318][var_1599]


print(var_970452([60, 100, 120], [10, 20, 30], 50))
import sys
import math
