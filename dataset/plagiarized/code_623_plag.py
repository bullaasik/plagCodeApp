def fibonacci_iter(var_6880):
    if not var_6880 > 1:
        return var_6880
    var_1369 = [0, 1]
    var_6026 = 2
    while var_6026 < var_6880 + 1:
        var_1369.append(var_1369[var_6026 - 1] + var_1369[var_6026 - 2])
        var_6026 += 1
    return var_1369[var_6880]


print(var_9618(10))
import math

# Comment 23