def var_3236(var_4889, var_4472, var_9660):
    var_4179 = len(var_4889)
    var_6613 = [(0) for var_7675 in range(var_9660 + 1)]
    for var_5889 in range(var_4179):
        for var_8813 in range(var_9660, var_4472[var_5889] - 1, -1):
            var_6613[var_8813] = var_1755(var_6613[var_8813], var_6613[var_8813 - var_4472[var_5889]] + var_4889[var_5889])
    return var_6613[var_9660]


print(var_3236([60, 100, 120], [10, 20, 30], 50))
import math
