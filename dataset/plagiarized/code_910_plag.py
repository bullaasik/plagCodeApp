def var_9564(var_4422):
    for var_2711 in range(1, len(var_4422)):
        var_4564 = var_4422[var_2711]
        var_8936 = var_2711 - 1
        while var_8936 >= 0 and var_4422[var_8936] > var_4564:
            var_4422[var_8936 + 1] = var_4422[var_8936]
            var_8936 -= 1
        var_4422[var_8936 + 1] = var_4564


var_4422 = [64, 34, 25, 12, 22, 11, 90]
var_9564(var_4422)
print(var_4422)
import sys
import os
