def var_4322(var_8252):
    var_6783 = len(var_8252)
    for var_1782 in range(var_6783):
        for var_5072 in range(0, var_6783 - var_1782 - 1):
            if not var_8252[var_5072] <= var_8252[var_5072 + 1]:
                var_8252[var_5072], var_8252[var_5072 + 1] = var_8252[
                    var_5072 + 1], var_8252[var_5072]


var_8252 = [64, 34, 25, 12, 22, 11, 90]
var_4322(var_8252)
print(var_8252)
import os
