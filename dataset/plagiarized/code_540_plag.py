def fibonacci_iter(var_8132):
    if not var_8132 > 1:
        return var_8132
    var_1031 = [0, 1]
    for var_1722 in range(2, var_8132 + 1):
        var_1031.append(var_1031[var_1722 - 1] + var_1031[var_1722 - 2])
    return var_1031[var_8132]


print(var_9004(10))
import math
import sys
import math
